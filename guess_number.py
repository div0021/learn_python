import sys
import random


def guess_number(name="PlayerOne"):
    game_count = 0
    player_win = 0
    player_win_percentage = 0

    def play_guess_number():
        nonlocal game_count
        nonlocal name
        nonlocal player_win
        nonlocal player_win_percentage

        player_choice = input(
            f"\n{name}, guess which number I'm thinking of... 1, 2, or 3.\n")

        if player_choice not in ["1", "2", "3"]:
            print(f"\n{name}, please enter 1, 2, or 3.")
            return play_guess_number()

        computer_choice = int(random.choice("123"))

        print(f"\n{name}, you chose {player_choice}.")
        print(f"\nI was thinking about the number {computer_choice}.")

        game_count += 1

        if int(player_choice) == computer_choice:
            print(f"🎉🎉 {name}, you win!")
            player_win += 1
        else:
            print(f"Sorry, {name}. Better luck next time. 😓")

        print(f"\nGame count: {game_count}")
        print(f"\n{name}'s wins: {player_win}")
        print(
            f"\nYour winning percentage: {round((player_win / game_count) * 100,3)}%"
        )

        print(f"\nPlay again, {name}?")

        while True:
            playagain = input("\nY for Yes or \nQ to Quit.\n")

            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_guess_number()
        else:
            print("\n🎉🎉🎊🎊🎉")
            print("Thank you for playing!\n")
            #sys.exit(f"Bye {name}! 👋👋👋")

    return play_guess_number


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provide a personal greeting.")

    parser.add_argument("-n",
                        "--name",
                        metavar="name",
                        required=True,
                        help="The name of the person to greet.")

    args = parser.parse_args()
    play = guess_number(args.name)
    play()
