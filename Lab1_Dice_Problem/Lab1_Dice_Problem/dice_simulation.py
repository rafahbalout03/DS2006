import random

def roll_dice ():
    return random.randint(1, 6)

if __name__ == "__main__":
    print("Simulating a dice roll...")
    result = roll_dice()
    print(f"You rolled a {result}")
    