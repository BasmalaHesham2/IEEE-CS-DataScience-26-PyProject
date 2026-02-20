import json
from classes import User, daily_log, process_day,show_leaderboard

data_file="users.json"

def load_users():
    try:
        with open(data_file,"r") as file:
            return json.load(file)
    except :
        return {}
    

def save_users(users):
    with open(data_file, "w") as file:
        json.dump(users, file, indent=4)

def signin():
    users= load_users()
    username= input("Enter your user name : \n").strip()
    passwd=input("Enter your user password : \n").strip()

    if not username or not passwd:
        print("Cannot enter an empty username or password please try again\n")
        return
    if username in users:
        print("username already exists choose anew one, be creative \n")
        return
    user = User(username,passwd)

    users[username] = {
        "password": passwd,
        "total_score": user.total_score,
        "streak": user.streak,
        "goals": user.goals
    }

    save_users(users)

    print("you signed in successfully")
def login():
    users=load_users()
    username= input("Enter your user name : \n").strip()
    passwd=input("Enter your user password : \n").strip()

    if username not in users:
        print("user not found please try again \n")
        return

    if users[username]["password"] != passwd:
        print("Incorrect password please try again \n")
        return

    print("you logged in successfully")
    return username

if __name__=="__main__":
         while True:
            print("\n Welcome to ramdan ")
            print("1. Sign in")
            print("2. Login")
            print("3. Exit")
           


            choice = input("Choose: ")

            if choice == "1":
                signin()
            elif choice == "2":
              username = login()
              if username:
                while True:
                 print(f"\nHello {username}! What do you want to do today?")
                 print("1. Log today's worship")
                 print("2. Process today's score")
                 print("3. Show Leaderboard")
                 print("4. Log out")
                 sub_choice = input("Choose: ")
            
                 if sub_choice == "1":
                   daily_log(username)
                 elif sub_choice == "2":
                    process_day(username)
                 elif sub_choice == "3":
                   show_leaderboard()
                 elif sub_choice == "4":
                   print("Logging out...")
                   break
                 else:
                  print("Invalid choice!")

            elif choice == "3":
                 break
            else:
                 print("Invalid choice!")