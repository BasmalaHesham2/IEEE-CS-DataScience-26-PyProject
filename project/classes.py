import json
import os

DATA_FILE = "users.json"

def safe_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Oops! Negative numbers are not allowed. Try again.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")


def load_users():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(DATA_FILE, "w") as f:
        json.dump(users, f, indent=4)
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.total_score = 0
        self.streak = 0
        self.goals = {
            "prayers": 5,
            "quran_pages": 5,
            "dhiker": 100,
        }

    
    def calculate_score(self, prayers, quran_pages, dhikr, fasting_done):
        score = 0
        score += prayers * 100
        score += quran_pages * 20
        score += dhikr * 10
        if fasting_done:
            score += 200
        self.total_score += score
        return score


    def update_streak(self, fasting_done):
        if fasting_done:
            self.streak += 1
        else:
            self.streak = 0


    
def daily_log(username):
    users = load_users()
    user = users[username]

    print("\nDaily Worship Log")

    prayers = safe_int_input("How many prayers did you pray today? ")
    quran_pages = safe_int_input("How many Quran pages did you read today? ")
    dhikr = safe_int_input("How many times did you do dhikr today? ")

    fasting = input("Did you fast today? (y/n): ").lower() == "y"

    user["daily_log"] = {
        "prayers": prayers,
        "quran_pages": quran_pages,
        "dhikr": dhikr,
        "fasting": fasting
    }

    save_users(users)
    print("Daily log saved successfully")

def process_day(username):
    users = load_users()
    user_data = users[username]
    
    if "daily_log" not in user_data:
        print("You must log today's worship first!")
        return

    log = user_data["daily_log"]

    user = User(username, user_data["password"])
    user.total_score = user_data.get("total_score", 0)
    user.streak = user_data.get("streak", 0)

    
    gained = user.calculate_score(
        log.get("prayers", 0),
        log.get("quran_pages", 0),
        log.get("dhikr", 0),
        log.get("fasting", False)
    )

    
    user.update_streak(log.get("fasting", False))

    
    user_data["total_score"] = user.total_score
    user_data["streak"] = user.streak

    
    del user_data["daily_log"]

    save_users(users)

    
    print(f"You gained {gained} points today")
    print(f"Current streak: {user.streak}")

    goal_prayers = user.goals["prayers"]
    percentage = (log.get("prayers", 0) / goal_prayers) * 100
    print(f"You completed {percentage:.0f}% of your prayer goal today!")



def show_leaderboard():
    users = load_users()

    if not users:
        print("No players yet!")
        return

    
    ranking = sorted(
        users.items(),
        key=lambda item: item[1].get("total_score", 0),
        reverse=True
    )

    print("\nRamadan Spiritual Heroes Leaderboard ")
    print("*****------*****------******------****")

    position = 1
    for username, data in ranking:
        print(f"{position}. {username} - {data.get('total_score', 0)} pts")
        position += 1




