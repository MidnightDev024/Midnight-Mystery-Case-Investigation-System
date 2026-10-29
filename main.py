from functions.authorization import sign_up, sign_in
import json

with open("data/cases.json", "r") as file:
    cases = json.load(file)

levels = cases["levels"]

def main():
    print("="*60)
    print("Welcome to", cases["game_title"])
    print("="*60)
    print()
    print("Want to play a game? --> Start")
    print("Want to exit a game? --> Exit")

    while True:
        play = input("You want to play a game? (Start/Exit): ").upper().strip()
        if play == "START":
            print()
            print("Loading Game........")
            print()
            while True:
                print("Want to create an account?   --> SignUp Here")
                print("Already have a account?      --> SignIn Here")
                print()

                choice = input("Would you like to create an account? (SignUp/SignIn) ").upper().strip()

                if choice == "SIGNUP":
                    print()
                    print("SignUp")
                    print("`"*30)
                    sign_up()
                elif choice == "SIGNIN":
                    print()
                    print("LogIn")
                    print("`"*30)
                    sign_in()
                else:
                    print("Invalid Input. \nPlease enter either YES or NO.")
                    break
        elif play == "EXIT":
            break
        else:
            print("Invalid Input. \nPlease enter either Start or Exit.")

if __name__ == "__main__":
    main()
