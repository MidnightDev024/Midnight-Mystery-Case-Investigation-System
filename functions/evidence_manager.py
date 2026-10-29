def evidence_manager(case):
    print()
    print("Evidences:")
    for evidence in case["evidences"]:
        print()
        print(evidence["id"])
        print("Summary:",evidence["summary"])
        print("Details:",evidence["detail"])
        print()
