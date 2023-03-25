def helloWorld():
    print("hello world")


def rpsGame():
    first = input("Enter rock(r), paper(p) or scissors(s) for Player 1: ")
    second = input("Enter rock(r), paper(p) or scissors(s) for Player 2: ")

    if first in ('r', 'p', 's') and second in ('r', 'p', 's'):
        if first == second:
            print(f"It's a tie!")
        elif first == "r":
            if second == "s":
                print("Rock smashes scissors! Player 1 win!")
            else:
                print("Paper covers rock! Player 2 wins!")
        elif first == "p":
            if second == "r":
                print("Paper covers rock! Player 1 wins!")
            else:
                print("Scissors cuts paper! Player 2 wins!")
        elif first == "s":
            if second == "p":
                print("Scissors cuts paper! Player 1 wins!")
            else:
                print("Rock smashes scissors! Player 2 wins!")

    else:
        print("Do you even know how to play?")


print("The moduleExercise module has been imported.")

if __name__ == "__main__":
    print("The moduleExercise module has been run directly.")
