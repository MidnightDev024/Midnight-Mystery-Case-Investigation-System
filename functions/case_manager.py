import json
from functions.evidence_manager import evidence_manager
from functions.interview_manager import interview_manager
from functions.history_manager import save_attempt

# with open("data/save_data.json", "r") as file:
#     users = json.load(file)

with open("data/cases.json", "r") as file:
    cases = json.load(file)

levels = cases["levels"]

def case_manager(user, users):
    # print(user)
    print()
    print("="*50)
    print(cases["game_title"])
    print("="*50)
    print()
    print("Welcome Casebreaker", user["player_name"])
    print("Player ID:", user["player_id"])
    print()
    case_index = 0
    theory = ""
    attempt_number = 0
    case_completed = False

    while True:
        for level in levels:
            if level["level"] == user["unlocked_level"]:
                # print("Case: ",level["title"])
                case_index = level["level"] - 1
                break
        print("Current Level:", user["unlocked_level"] and levels[case_index]["level"])

        print()
        print("GAME MENU")
        print("-" * 60)
        print("Step1. Understand the Incident")
        print("Step2. Examine the Evidences")
        print("Step3. Interview Suspects")
        print("Step4. Build your Theory")
        print("Step5. Accuse the Culprit")
        print("Step6. Sign Out")
        print("-" * 60)

        while True:
            choice = input("Select the step (1, 2, 3, 4, 5, 6): ")
            if choice == "1":
                print("Step 1: Understand the Incident")
                print()
                print("Incident:",levels[case_index]["title"])
                print()
                print("Brief:",levels[case_index]["incident"])
                print()
                print("Suspects: ")
                print("`"*30)
                count = 0

                for suspect in levels[case_index]["suspects"]:
                    count += 1
                    print(f"{count}.")
                    print("Name:",suspect["name"])
                    print("Role:",suspect["role"])
                    print()

            if choice == "2":
                evidence_manager(levels[case_index])

            if choice == "3":
                interview_manager(levels[case_index])

            if choice == "4":
                print()
                print("Step 4: Build Your Theory")
                print("-" * 30)

                theory = input("Enter your theory: ").strip()

                if theory == "":
                    print("Theory cannot be empty.")
                else:
                    print("Your theory has been saved for this investigation.")

            if choice == "5":
                print()
                print("Step 5: Accuse the Culprit")
                print("-" * 30)

                if case_completed:
                    print("You have already completed this case.")
                elif theory == "":
                    print("Please build your theory in Step 4 first.")
                else:
                    print("Suspects:")

                    for i, suspect in enumerate(levels[case_index]["suspects"], start=1):
                        print(f"{i}. {suspect['name']}")

                    suspect_choice = input("Enter suspect number: ").strip()

                    if not suspect_choice.isdigit():
                        print("Invalid input. Please enter a suspect number.")
                    elif int(suspect_choice) < 1 or int(suspect_choice) > len(levels[case_index]["suspects"]):
                        print("Invalid suspect number.")
                    else:
                        accused_suspect = levels[case_index]["suspects"][int(suspect_choice) - 1]["name"]
                        actual_culprit = levels[case_index]["culprit"]

                        attempt_number += 1

                        if accused_suspect == actual_culprit:
                            attempt_result = "Correct"
                            case_result = "Solved"
                            case_completed = True

                            score = cases["scoring"]["correct_on_attempt"][str(attempt_number)]

                            user["score"] += score
                            user["completed_cases"].append(levels[case_index]["case_id"])

                            print("Correct! You identified the culprit.")
                            print("Points earned:", score)
                        else:
                            attempt_result = "Incorrect"
                            print("Incorrect accusation.")
                            print()
                            print(f"You are left with {3 - attempt_number}")

                            if attempt_number == cases["max_attempts"]:
                                case_result = "Failed"
                                case_completed = True
                                score = cases["scoring"]["incorrect_after_max_attempts"]

                                print("You have used all your attempts.")
                                print("The actual culprit was:", actual_culprit)
                                print("Points earned:", score)
                            else:
                                case_result = "In Progress"
                                score = ""

                        if case_completed:
                            user["unlocked_level"] += 1

                        save_attempt(
                            user,
                            levels[case_index],
                            attempt_number,
                            theory,
                            accused_suspect,
                            attempt_result,
                            case_result,
                            score if case_completed else "",
                            user["score"] if case_completed else ""
                        )

                        with open("data/save_data.json", "w") as file:
                            json.dump(users, file, indent=4)

                        if case_completed:
                            print()
                            print("You have successfully completed this case.")

                            next_choice = input("Want to continue Game (NEXT/EXIT): ").upper().strip()

                            if next_choice == "NEXT":
                                if user["unlocked_level"] <= len(levels):
                                    print("Loading next level...")
                                    break
                                else:
                                    print("Congratulations! You have completed all levels.")
                                    break

                            elif next_choice == "EXIT":
                                print("Signing OFF...")
                                return

                            else:
                                print("Invalid input. Please enter NEXT or EXIT.")


            if choice == "6":
                print("Signing OFF")
                return

