# Midnight Mystery Case Investigation System

## About the Project

Midnight Mystery Case Investigation System is a Python-based console game where players act as investigators, examine evidence, interview suspects, build theories, and identify the culprit behind different mystery cases.

The game includes multiple difficulty levels, an attempt-based scoring system, and player progress tracking.

## Features

- **Player Authentication:** Sign up and sign in using a username and player ID.
- **Multiple Mystery Cases:** Investigate five cases with different levels of difficulty.
- **Incident Investigation:** Read the incident details and review the suspects.
- **Evidence Examination:** Examine evidence summaries and detailed information.
- **Suspect Interviews:** Read suspects' statements and follow-up responses.
- **Theory Building:** Create a theory based on the available evidence and interviews.
- **Culprit Identification:** Accuse a suspect within the allowed number of attempts.
- **Scoring System:** Earn points based on the attempt used to identify the culprit.
- **Level Progression:** Unlock subsequent levels after completing a case.
- **Progress Saving:** Store player progress and scores in a JSON file.
- **Investigation History:** Record investigation attempts and results in a CSV file.

## Technologies Used

- Python
- JSON for storing case information and player progress
- CSV for maintaining investigation history
- Git and GitHub for version control

## Project Structure

```text
Midnight-Mystery-Case-Investigation-System/
│
├── data/
│   ├── cases.json
│   ├── save_data.json
│   └── investigation_history.csv
│
├── functions/
│   ├── authorization.py
│   ├── case_manager.py
│   ├── evidence_manager.py
│   ├── history_manager.py
│   ├── interview_manager.py
│   └── scoring.py
│
├── main.py
├── .gitignore
└── README.md
```

## How to Run the Project

### Prerequisites

- Python 3 installed on your system.
- An IDE or code editor, such as PyCharm, or a terminal.

### Installation and Setup

**1. Clone the repository**

```bash
git clone https://github.com/MidnightDev024/Midnight-Mystery-Case-Investigation-System.git
```

**2. Open the project folder**

```bash
cd Midnight-Mystery-Case-Investigation-System
```

**3. Run the application**

```bash
python main.py
```

If your system uses the `py` command to run Python, you can use:

```bash
py main.py
```

## How to Play

1. Start the game.
2. Create an account or sign in with your existing credentials.
3. Read the incident details and review the suspects.
4. Examine the available evidence.
5. Interview the suspects and review their statements.
6. Build a theory based on the information collected.
7. Accuse the suspect you believe is responsible.
8. Earn points based on your attempt and progress through the levels.
9. Choose whether to continue to the next level or exit the game.

## Scoring System

The game uses an attempt-based scoring system:

| Outcome | Points |
|---|---:|
| Correct accusation on the first attempt | 10 |
| Correct accusation on the second attempt | 8 |
| Correct accusation on the third attempt | 5 |
| Case not solved within the allowed attempts | 0 |

## Data Storage

The project uses local files to store information:

- `cases.json` — stores the mystery cases, suspects, evidence, interviews, and case solutions.
- `save_data.json` — stores player information, unlocked levels, completed cases, and scores.
- `investigation_history.csv` — records investigation attempts, theories, accusations, outcomes, and scores.

## Learning Objectives

This project demonstrates practical use of Python concepts, including:

- Functions and modules
- Conditional statements and loops
- Lists and dictionaries
- File handling
- JSON data processing
- CSV file handling
- Exception handling, where implemented
- Basic application logic and state management

## Future Improvements

- Add a graphical user interface.
- Add more mystery cases and difficulty levels.
- Improve player statistics and investigation reports.
- Introduce more interactive investigation options.

## Author

**Akash Chawla**

GitHub: [@MidnightDev024](https://github.com/MidnightDev024)

---

*Midnight Mystery Case Investigation System — Every clue matters. Every accusation counts.*
