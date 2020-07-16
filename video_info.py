"""This class creates instances of the data fields to be displayed"""

class videoInfo:
    def __init__(self, likes, dislikes, sentiment):
        self.likes = likes
        self.dislikes = dislikes
        self.sentiment = sentiment
        
    # def set_likes(self, num_likes):
    #     """sets class obj to num of thumbs up"""
    #     self.likes = num_likes

    # def set_dislikes(self, num_dislikes):
    #     """sets class obj to num of thumbs down"""
    #     self._dislikes = num_dislikes
    
    # def set_sentimenent(self, num_sentiments):
    #     """get's the sentiments from video and sets it to the class obj"""
    #     self._sentiment = num_sentiments

    def display_stats(self):
        print(self.likes, 'likes')
        print(self.dislikes, 'dislikes')

        if(self.sentiment > 0):
            print("General positive sentiment")
        elif(self.sentiment == 0):
            print("General neutral sentiment")
        else:
            print("General Negative sentiment")

    