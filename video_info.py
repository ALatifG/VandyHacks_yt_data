"""This class creates instances of the data fields to be displayed"""

class videoInfo:
    def __init__(self, likes, dislikes, sentiment):
        self.likes = likes
        self.dislikes = dislikes
        self.sentiment = sentiment
        
    def display_stats(self):
        print(self.likes, 'likes')
        print(self.dislikes, 'dislikes')

        if(self.sentiment < 0):
            print("General positive sentiment")
        elif(self.sentiment == 0):
            print("General neutral sentiment")
        else:
            print("General Negative sentiment")

    