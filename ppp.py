class pest():  

    def __init__(self, name, happiness):
        self.name == name 
        self.__happiness == happiness 

    def play(self):
        while True:
            playtime = input("Write 'play' to play with your pet!")
            if  playtime == "play":
                print(f"{self.name} is playing fetch!")
                self.__happiness += 10

    def show_status(self):
        print(f"{self.name}'s happiness is now {self.__happiness}")

pest = ("brian")
pest.play()