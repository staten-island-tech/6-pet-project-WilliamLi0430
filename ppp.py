import time

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
            if  playtime == "play":
                print(f"{self.name} is playing fetch!")
                self.__happiness += 10
                self.hunger -= 40
                self.show_status()
                self.show_status2()
                if self.hunger <= 0:
                    time.sleep(2)
                    print("...")
                    time.sleep(2)
                    print(f"{self.name} has died.")
                    time.sleep(2)
                    print(f"You did not feed {self.name} enough.")
                    time.sleep(2)
                    print("Do you know what you've done?")
                    time.sleep(2)
                    print(f"You've starved {self.name}.")
                    time.sleep(2)
                    print("You're a monster.")
                    time.sleep(2)
                    print("Why would you play this game in the first place?")
                    time.sleep(2)
                    print(f"{self.name}'s corpse lies at your feet.")
                    time.sleep(2)
                    print("Take a look at its thin, raggedy body.")
                    time.sleep(2)
                    print("Do you not feel even a bit of remorse?")
                    time.sleep(2)
                    print("Regret?")
                    time.sleep(2)
                    print("Guilt?")
                    time.sleep(2)
                    print("I thought not.")
                    time.sleep(2)
                    print("Remember the horror that you've done today.")
                    time.sleep(2)
                    print("I won't forget this.")
                    time.sleep(2)
                    print("Goodbye.")
                    break

            elif playtime == "feed":
                print(f"{self.name} is eating food!")
                self.hunger += 5
                self.show_status2()
                print(f"{self.name}'s happiness is still {self.__happiness}. ")

            else:
                print(f"{self.name}'s happiness is still {self.__happiness}. ")
                print(f"{self.name}'s hunger level is still {self.hunger}. ")  

pestname = input("What is your pet's name? ")
pest = pest(pestname, 0, 50)
pest.play()