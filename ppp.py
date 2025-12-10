import time

class pest():  

    def __init__(self, name, happiness, hunger, exhaustion):
        self.name = name 
        self.__happiness = happiness 
        self.hunger = hunger
        self.exhaustion = exhaustion

    def show_status(self):
        print(f"{self.name}'s happiness is now {self.__happiness}.")

    def show_status2(self):
        print(f"{self.name}'s hunger level is now {self.hunger}.")

    def show_status3(self):
        print(f"{self.name}'s exhaustion level is now {self.exhaustion}.")

    def play(self):
        while True:
            day_number = 1
            playtime = input("play sleep feed ")

            if  playtime == "play":
                print(f"{self.name} is playing fetch!")
                self.__happiness += 10
                self.hunger -= 10
                self.exhaustion += 10
                self.show_status()
                self.show_status2()
                if self.hunger <= 0:
                    time.sleep(3)
                    print("...")
                    time.sleep(3)
                    print(f"{self.name} has died.")
                    time.sleep(3)
                    print(f"You did not feed {self.name} enough.")
                    time.sleep(3)
                    print("Do you know what you've done?")
                    time.sleep(3)
                    print(f"You've starved {self.name}.")
                    time.sleep(3)
                    print(f"{self.name}'s dead.")
                    time.sleep(3)
                    print("You're a monster.")
                    time.sleep(3)
                    print("An idiotic monster.")
                    time.sleep(3)
                    print("You can't tell me that you didn't know,")
                    time.sleep(3)
                    print("that your pet could die from starvation.")
                    time.sleep(3)
                    print("Are you allergic to common sense?")
                    time.sleep(3)
                    print("Look at what you are playing right now.")
                    time.sleep(3)
                    print("A pet simulator game.")
                    time.sleep(3)
                    print("Why would you ever play this game in the first place?")
                    time.sleep(3)
                    print(f"So you can neglect {self.name}?")
                    time.sleep(3)
                    print(f"So you can abuse {self.name}?")
                    time.sleep(3)
                    print(f"So you can starve {self.name}?")
                    time.sleep(3)
                    print(f"If you can so willingly kill {self.name},")
                    time.sleep(3)
                    print("tell me why you can't come back and kill more pets.")
                    time.sleep(3)
                    print(f"{self.name} will never come back.")
                    time.sleep(3)
                    print("You know that, don't you?")
                    time.sleep(3)
                    print(f"{self.name}'s corpse lies at your feet.")
                    time.sleep(3)
                    print("Look at its thin, raggedy body.")
                    time.sleep(3)
                    print("Go ahead.")
                    time.sleep(3)
                    print("Take a look.")
                    time.sleep(3)
                    print("Do you not feel even a bit of remorse?")
                    time.sleep(3)
                    print("Regret?")
                    time.sleep(3)
                    print("Guilt?")
                    time.sleep(3)
                    print("I thought not.")
                    time.sleep(3)
                    print("Remember the horror that you've done today.")
                    time.sleep(3)
                    print("I won't forget this.")
                    time.sleep(3)
                    print("Goodbye.")
                    break

            elif playtime == "feed":
                print(f"{self.name} is eating food!")
                self.hunger += 100
                self.show_status2()
                print(f"{self.name}'s happiness is still {self.__happiness}. ")
                if self.hunger >= 100:
                    time.sleep(3)
                    print("...")
                    time.sleep(3)
                    print(f"{self.name} has died.")
                    time.sleep(3)
                    print(f"You fed {self.name} too much.")
                    time.sleep(3)
                    print("Do you know what you've done?")
                    time.sleep(3)
                    print(f"You've overfed {self.name}.")
                    time.sleep(3)
                    print(f"{self.name}'s dead.")
                    time.sleep(3)
                    print("You're a monster.")
                    time.sleep(3)
                    print("An idiotic monster.")
                    time.sleep(3)
                    print("You can't tell me that you didn't know,")
                    time.sleep(3)
                    print("that your pet could die from overeating.")
                    time.sleep(3)
                    print("Are you allergic to common sense?")
                    time.sleep(3)
                    print("Look at what you are playing right now.")
                    time.sleep(3)
                    print("A pet simulator game.")
                    time.sleep(3)
                    print("Why would you ever play this game in the first place?")
                    time.sleep(3)
                    print(f"So you can stuff {self.name}?")
                    time.sleep(3)
                    print(f"So you can overfeed {self.name}?")
                    time.sleep(3)
                    print("So you can can go without trouble in your life?")
                    time.sleep(3)
                    print(f"If you can so willingly kill {self.name},")
                    time.sleep(3)
                    print("tell me why you can't come back and kill more pets.")
                    time.sleep(3)
                    print(f"{self.name} will never come back.")
                    time.sleep(3)
                    print("You know that, don't you?")
                    time.sleep(3)
                    print(f"{self.name}'s corpse lies at your feet.")
                    time.sleep(3)
                    print("Look at its stuffed, bloated body.")
                    time.sleep(3)
                    print("Go ahead.")
                    time.sleep(3)
                    print("Take a look.")
                    time.sleep(3)
                    print("Do you not feel even a bit of remorse?")
                    time.sleep(3)
                    print("Regret?")
                    time.sleep(3)
                    print("Guilt?")
                    time.sleep(3)
                    print("I thought not.")
                    time.sleep(3)
                    print("Remember the horror that you've done today.")
                    time.sleep(3)
                    print("I won't forget this.")
                    time.sleep(3)
                    print("Goodbye.")
                    break

            elif playtime == "sleep":
                print("The day is over.")
                day_number += 1
                self.exhaustion -= 20
                self.hunger -= 5
                self.happiness -= 10
                print(f"It is now day {day_number}.")

            else:
                print(f"{self.name}'s happiness is still {self.__happiness}. ")
                print(f"{self.name}'s hunger level is still {self.hunger}. ")  

pestname = input("What is your pet's name? ")
pest = pest(pestname, 0, 50, 0)
pest.play()