def interview_manager(case):
    print()
    print("Interviews:")
    count = 0
    for interview in case["interviews"]:
        count += 1
        print()
        print(f"{count}.")
        print("Name:",interview["suspect_name"])
        print("Suspects Statement:",interview["initial_response"])
        print("Investigation says:",interview["follow_up"])
