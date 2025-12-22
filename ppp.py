import time
import random

class pest():  

    def __init__(self, name, happiness, hunger, exhaustion, level, health):
        self.name = name 
        self.__happiness = happiness 
        self.hunger = hunger
        self.exhaustion = exhaustion
        self.level = level
        self.health = health

    def show_status(self):
        print(f"{self.name}'s happiness is now {self.__happiness}.")

    def show_status2(self):
        print(f"{self.name}'s hunger level is now {self.hunger}.")

    def show_status3(self):
        print(f"{self.name}'s exhaustion level is now {self.exhaustion}.")

    def show_status4(self):
        print(f"{self.name} is now level {self.level}!")

    def play(self):
        while True:
            day_number = 1
            self.level = 0
            playtime = input("play sleep feed ")
            playchance = [0, 0, 1, 1, 2, 2, 3]
            if  playtime == "play":
                if random.choice(playchance) == 0:
                    print(f"{self.name} is playing fetch!")
                    self.__happiness += 10
                    self.hunger -= 10
                    self.exhaustion += 10
                    self.level += 10
                    self.show_status()
                    self.show_status2()
                    self.show_status3()
                    if self.hunger <= 0:
                        messages = [
                            "...",
                            f"{self.name} has died.",
                            f"You did not feed {self.name} enough.",
                            "Do you know what you've done?",
                            f"You've starved {self.name}.",
                            f"{self.name}'s dead.",
                            "You're a monster.",
                            "An idiotic monster.",
                            "You can't tell me that you didn't know,",
                            "that your pet could die from starvation.",
                            "Are you allergic to common sense?",
                            "Look at what you are playing right now.",
                            "A pet simulator game.",
                            "Why would you ever play this game in the first place?",
                            f"So you can neglect {self.name}?",
                            f"So you can abuse {self.name}?",
                            f"So you can starve {self.name}?",
                            f"If you can so willingly kill {self.name},",
                            "tell me why you can't come back and kill more pets.",
                            f"{self.name} will never come back.",
                            "You know that, don't you?",
                            f"{self.name}'s corpse lies at your feet.",
                            "Look at its thin, raggedy body.",
                            "Go ahead.",
                            "Take a look.",
                            "Do you not feel even a bit of remorse?",
                            "Regret?",
                            "Guilt?",
                            "I thought not.",
                            "Remember the horror that you've done today.",
                            "I won't forget this.",
                            "Goodbye."
                        ]
                        for line in messages:
                            time.sleep(3)
                            print(line)
                        break
                    if self.exhaustion <= 0:
                        messages = [
                            "...",
                            f"{self.name} has died.",
                            f"You did not allow {self.name} to rest enough.",
                            "Do you know what you've done?",
                            f"You've overworked {self.name}.",
                            f"{self.name}'s dead.",
                            "You're a monster.",
                            "An idiotic monster.",
                            "You can't tell me that you didn't know,",
                            "that your pet could die from exhaustion.",
                            "Are you allergic to common sense?",
                            "Look at what you are playing right now.",
                            "A pet simulator game.",
                            "Why would you ever play this game in the first place?",
                            f"So you can overwork {self.name}?",
                            "So you can force playtime for your own happiness?",
                            f"So you can make {self.name} do whatever you want?",
                            f"If you can so willingly kill {self.name},",
                            "tell me why you can't come back and kill more pets.",
                            f"{self.name} will never come back.",
                            "You know that, don't you?",
                            f"{self.name}'s corpse lies at your feet.",
                            "Look at its limp, broken body.",
                            "Go ahead.",
                            "Take a look.",
                            "Do you not feel even a bit of remorse?",
                            "Regret?",
                            "Guilt?",
                            "I thought not.",
                            "Remember the horror that you've done today.",
                            "I won't forget this.",
                            "Goodbye."
                        ]
                        for line in messages:
                            time.sleep(3)
                            print(line)
                        break
                elif random.choice(playchance) == 1:
                    print(f"{self.name} is playing tug of war!")
                elif random.choice(playchance) == 2:
                    print(f"{self.name} is playing with Luke's code!")
                elif random.choice(playchance) == 3:
                    print(f"Oh no! {self.name} got hurt playing with you!")

            elif playtime == "feed":
                print(f"{self.name} is eating food!")
                self.hunger += 10
                self.show_status2()
                print(f"{self.name}'s happiness is still {self.__happiness}. ")
                if self.hunger >= 100:
                    messages = [
                        "...",
                        f"{self.name} has died.",
                        f"You fed {self.name} too much.",
                        "Do you know what you've done?",
                        f"You've overfed {self.name}.",
                        f"{self.name}'s dead.",
                        "You're a monster.",
                        "An idiotic monster.",
                        "You can't tell me that you didn't know,",
                        "that your pet could die from overeating.",
                        "Are you allergic to common sense?",
                        "Look at what you are playing right now.",
                        "A pet simulator game.",
                        "Why would you ever play this game in the first place?",
                        f"So you can stuff {self.name}?",
                        f"So you can overlook {self.name}?",
                        "So you can go without trouble in your life?",
                        f"If you can so willingly kill {self.name},",
                        "tell me why you can't come back and kill more pets.",
                        f"{self.name} will never come back.",
                        "You know that, don't you?",
                        f"{self.name}'s corpse lies at your feet.",
                        "Look at its stuffed, bloated body.",
                        "Go ahead.",
                        "Take a look.",
                        "Do you not feel even a bit of remorse?",
                        "Regret?",
                        "Guilt?",
                        "I thought not.",
                        "Remember the horror that you've done today.",
                        "I won't forget this.",
                        "Goodbye."
                    ]
                    for line in messages:
                        time.sleep(3)
                        print(line)
                    break

            elif playtime == "sleep":
                print("The day is over.")
                day_number += 1
                self.exhaustion -= 20
                self.hunger -= 5
                self.happiness -= 10
                print(f"It is now day {day_number}.")

            elif playtime == "level":
                print(f"{self.name}'s level is {self.level}.")

            else:
                print(f"{self.name}'s happiness is still {self.__happiness}. ")
                print(f"{self.name}'s hunger level is still {self.hunger}. ")  

pestname = input("What is your pet's name? ")
#intro text here
pest = pest(pestname, 50, 50, 0, 1, 100)
pest.play()

#add evo, chests, levels, cookie gambling, limit amount of actions per day