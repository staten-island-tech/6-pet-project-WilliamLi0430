class pest():  

    def __init__(self, name, happiness, hunger):
        self.name = name 
        self.__happiness = happiness 
        self.hunger = hunger

    def show_status(self):
        print(f"{self.name}'s happiness is now {self.__happiness}. ")

    def show_status2(self):
        print(f"{self.name}'s hunger level is now {self.hunger}. ")

    def play(self):
        while True:
            playtime = input("Write 'play' to play with your pet! ")
            mealtime = input("Write 'feed' to feed your pet! ")
            if  playtime == "play":
                print(f"{self.name} is playing fetch!")
                self.__happiness += 10
                self.hunger -= 10
                self.show_status()
                self.show_status2()
                if self.__happiness == 100:
                    print(f"{self.name} is at the maximum happiness level. ")
                    break
            else:
                print(f"{self.name}'s happiness is still {self.__happiness}. ")
            if mealtime == "feed":
                print(f"{self.name} is eating food!")
                self.hunger += 5
                

pestname = input("What is your pet's name? ")
pest = pest(pestname, 0, 50)
pest.play()
pest.show_status()