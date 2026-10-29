import csv
import os
from datetime import datetime

file_path = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "data",
    "investigation_history.csv"
)

fieldnames = [
    "user_identifier",
    "user_name",
    "user_id",
    "case_id",
    "level",
    "case_title",
    "attempt_number",
    "theory",
    "accused_suspect",
    "actual_culprit",
    "attempt_result",
    "case_result",
    "level_score",
    "total_score",
    "completed_at"
]


def save_attempt(user, case, attempt_number, theory,
                 accused_suspect, attempt_result,
                 case_result="In Progress",
                 level_score="", total_score=""):

    user_identifier = user.get(
        "user_identifier",
        f"USER{user['index'] + 1:03d}"
    )

    record = {
        "user_identifier": user_identifier,
        "user_name": user["player_name"],
        "user_id": user["player_id"],
        "case_id": case["case_id"],
        "level": case["level"],
        "case_title": case["title"],
        "attempt_number": attempt_number,
        "theory": theory,
        "accused_suspect": accused_suspect,
        "actual_culprit": case["culprit"],
        "attempt_result": attempt_result,
        "case_result": case_result,
        "level_score": level_score,
        "total_score": total_score,
        "completed_at": (
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if case_result in ("Solved", "Failed")
            else ""
        )
    }

    file_exists = os.path.exists(file_path)

    with open(file_path, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists or os.path.getsize(file_path) == 0:
            writer.writeheader()

        writer.writerow(record)
