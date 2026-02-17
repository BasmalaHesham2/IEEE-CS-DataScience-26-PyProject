class User:
    def __init__(self,username,passwd):
        self.username=username
        self.passwd=passwd
        self.total_score=0
        self.streak=0
        self.goals={
            "prayers":5,
            "quran_pages" :5,
            "dhiker" : 100,
        }

        def calculate_score(self,prayers,quran_pages,dhiker,fasting_done):
            score=0
            score+= prayers*100
            score += quran_pages * 20
            score += dhiker * 10

            if(fasting_done): score+=200

            self.total_score+=score

            return score
        
        def update_streak(self,fasting_done):
            if fasting_done:
                self.streak +=1
            else:
                self.streak=0

    
        
