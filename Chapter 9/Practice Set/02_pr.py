import random

def game():
    print("You are playing the game..")
    score = random.randint(1, 100)

    # Fetch the hiscore
    try:
        with open("hiscore.txt", "r") as f:
            hiscore = f.read()
            if hiscore.strip() == "":
                hiscore = 0
            else:
                hiscore = int(hiscore)
    except FileNotFoundError:
        hiscore = 0

    print(f"Your score: {score}")

    if score > hiscore:
        print("New high score!")
        with open("hiscore.txt", "w") as f:
            f.write(str(score))

    return score

game()
                # confused in this code!!
