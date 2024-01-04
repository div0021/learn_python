import guess_number
import rps
import sys


def arcade(name="PersonOne"):
    flag = True

    def arcade_choose():
        nonlocal name
        nonlocal flag

        if flag:
            print(f"{name}, welcome to the Arcade! 👻🎮🕹️\n")
        else:
            print(f"{name}, welcome back to the Arcade menu.")

        print(
            f"\nPlease choose a game:\n1 = Rock Paper Scissors \n2 = Guess My Number\n\n"
        )

        print(f"Or press \"x\" to exit the Arcade.\n\n")

        player_choice = input("")
        if player_choice.lower() == "x":
            print("\nSee you next time!")
            sys.exit(f"\nBye {name}! 👋")

        if player_choice not in ["1", "2"]:
            print("\n Invalid option!\n")
            arcade_choose()

        if player_choice == "1":
            play = rps.rps(name)
            play()
        elif player_choice == "2":
            play = guess_number.guess_number(name)
            play()

        flag = False

        arcade_choose()

    arcade_choose()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="This is were argument are passed")

    parser.add_argument("-n",
                        "--name",
                        metavar="name",
                        required=True,
                        help="The name of person to greet.")

    arg = parser.parse_args()

    arcade(arg.name)
