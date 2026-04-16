#  gussing the right number game in python 
import random

def get_lives():
    level = input("Choose difficulty (easy/medium/hard): ")

    if level == "easy":
        return 10
    elif level == "medium":
        return 7
    else:
        return 3


def load_high_score():
    try:
        with open("score.txt", "r") as file:
            return int(file.read())
    except:
        return None


def save_high_score(score):
    with open("score.txt", "w") as file:
        file.write(str(score))


while True:
    number = random.randint(1, 100)
    lives = get_lives()
    attempts = 0

    print("\n🎮 NEW GAME STARTED!")

    high_score = load_high_score()
    if high_score:
        print(f"🏆 Best score: {high_score} attempts")

    while lives > 0:
        guess = int(input("Guess a number between 1 and 100: "))

        if guess < 1 or guess > 100:
            print("⚠️ Enter number between 1-100")
            continue

        attempts += 1
        lives -= 1

        if guess > number:
            print("Too high 📈")
        elif guess < number:
            print("Too low 📉")
        else:
            print(f"\n🎉 Correct! You won in {attempts} attempts!")

            if high_score is None or attempts < high_score:
                print("🏆 NEW HIGH SCORE!")
                save_high_score(attempts)

            break

        print(f"💔 Lives left: {lives}")

    else:
        print(f"\n😢 Game Over! The number was {number}")

    play_again = input("\n🔁 Play again? (yes/no): ").lower()
    if play_again != "yes":
        print("👋 Thanks for playing!")
        break
