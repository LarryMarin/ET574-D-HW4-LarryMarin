# Name: Larry Marin
# QCC ID: 23656183
# ET574 HW4: Dice Game Simulator

import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        #returns a random integer between 1 and the number of sides
        return random.randint(1, self.sides)

class DiceGame:
    def __init__(self):
        self.die1 = Die()
        self.die2 = Die()

    def evaluate_roll(self, total):
        #returns win, lose, or roll again depending on outcome
        if total in (7, 11):
            return "Win"
        if total in (2, 3, 12):
            return "Lose"
        return "Roll Again"

    def play_round(self):
        #rolls both dice and then returns roll1, roll2, total, and result
        roll1 = self.die1.roll()
        roll2 = self.die2.roll()
        total = roll1 + roll2
        result = self.evaluate_roll(total)
        return roll1, roll2, total, result

def main():
    game = DiceGame()
    while True:
        print("\nDice Game")
        print("1. Play a round")
        print("2. Exit")
        choice = input("Choose an option: ").strip()
 
        if choice == "1":
            roll1, roll2, total, result = game.play_round()
            print(f"Die 1: {roll1}")
            print(f"Die 2: {roll2}")
            print(f"Total: {total}")
            print(f"Result: {result}")
        elif choice == "2":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")
 
 
if __name__ == "__main__":
    main()