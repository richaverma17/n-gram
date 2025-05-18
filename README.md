# N-Gram Character-Level Auto-Completion System

This project implements a **character-level N-Gram language model** for real-time word auto-completion in a terminal-based interface. The model predicts the next possible word(s) based on a given prefix using statistical probabilities derived from character sequences in a training corpus.


## Features

- Character-level N-Gram model (supports n = 2 to 10).
- Predicts word completions in real time based on prefix.
- Interactive terminal UI with:
  - Live suggestions after each keystroke.
  - Tab key to cycle through suggestions.
  - Enter to select a suggestion.
  - ESC to exit interface.
- Logs metrics like:
  - Total keystrokes and tab presses.
  - Average letters typed per word.
  - Average tab usage per word.


## Requirements

- Python 3.x
- No external libraries required


## How It Works

1. The model is trained on a text corpus provided in `text_content.txt`.
2. It learns frequency-based probabilities for character sequences up to N-grams.
3. During typing, it uses this model to predict completions based on typed prefixes.


## How to Run

Make sure your corpus file (e.g., `text_content.txt`) is in a folder.

```bash
python user_interface.py <path_to_corpus_folder>
```

**Example:**
```bash
python user_interface.py ./data/
```

## Controls

- Type to enter characters.
- Press `Tab` to cycle through word predictions.
- Press `Enter` to auto-complete the selected word.
- Press `Esc` to exit the application.


## Metrics Collected

| Metric                          | Description                                           |
|--------------------------------|-------------------------------------------------------|
| Total letter keys typed        | Raw keystrokes excluding suggestions                 |
| Total tab key presses          | Number of times suggestions were cycled              |
| Avg letters typed per word     | Typing efficiency = (keys / word length)             |
| Avg tab presses per word       | Suggestion reliance metric                           |

All these metrics are logged inside the UI for performance analysis.
