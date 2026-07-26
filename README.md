# Rock Paper Scissors

A simple command-line Rock, Paper, Scissors game written in Python. Play against
the computer, see who wins each round, and keep playing until you decide to quit.

## Features

- Classic Rock / Paper / Scissors gameplay against a computer opponent
- Input validation (keeps asking until you give a valid choice)
- Play unlimited rounds in a loop
- Type `exit` at any time to quit

## Requirements

- Python 3.6+
- No external dependencies (uses only the Python standard library)

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/rock-paper-scissors.git
   cd rock-paper-scissors
   ```

2. Run the game:
   ```bash
   python rock_paper_scissors.py
   ```

## How to Play

- When prompted, enter `rock`, `paper`, or `scissors`.
- The computer will randomly pick one of the three options.
- The winner is displayed after each round.
- Enter `exit` at any prompt to quit the game.

## Running Tests

Unit tests cover the game logic (winner determination):

```bash
python -m unittest discover tests
```

## Project Structure

```
rock-paper-scissors/
├── rock_paper_scissors.py   # Main game script
├── tests/
│   └── test_rock_paper_scissors.py
├── README.md
├── LICENSE
├── requirements.txt
└── .gitignore
```

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file
for details.
