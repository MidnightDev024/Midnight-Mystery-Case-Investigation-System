import json
from functions.case_manager import case_manager

with open("data/cases.json", "r") as file:
    cases = json.load(file)

levels = cases["levels"]
# print(levels[0])

with open("data/save_data.json", "r") as file:
    users = json.load(file)


def sign_up():
    player_name = input("Enter UserName: ")
    player_id = input("Enter User ID: ")
    index = 0
    user_exists = False

    for user in users["players"]:
        if user["player_name"] == player_name and user["player_id"] == player_id:
            index = user["index"]
            user_exists = True
            break

    print()
    print("processing....")

    if user_exists:
        print("User already exists.")
        print("loading data....")
        case_manager(users["players"][index], users)
    else:
        print("Signing Up")
        index = len(users["players"])
        # print(index)
        new_user = {
            "ID": len(users["players"]) + 1,
            "index": len(users["players"]),
            "player_name": player_name,
            "player_id": player_id,
            "unlocked_level": 1,
            "completed_cases": [],
            "score": 0
        }
        users["players"].append(new_user)
        case_manager(users["players"][index])

        with open("data/save_data.json", "w") as file:
            json.dump(users, file, indent=4)

def sign_in():
    player_name = input("Enter UserName: ")
    player_id = input("Enter User ID: ")
    index = 0
    user_exists = False

    for user in users["players"]:
        if user["player_name"] == player_name and user["player_id"] == player_id:
            user_exists = True
            index = user["index"]
            # print(index)
            break

    print()
    print("Processing.....")

    if user_exists:
        print("User Found")
        case_manager(users["players"][index], users)
    else:
        print("! User Not Found !")
        print("Please create an account using SignUp.")