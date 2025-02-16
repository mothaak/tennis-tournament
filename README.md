# Tennis Scoring System

A sophisticated tennis scoring system implementation that follows official tennis rules and demonstrates clean code principles.

Author: Moditha Akalanka

## Overview

This project implements a tennis scoring system that handles:
- Game scoring (0, 15, 30, 40, Deuce, Advantage)
- Set scoring with 6-game wins
- Tiebreak scenarios at 6-6
- Score tracking and reporting

## Development Journey

### The Challenge

The main challenges in implementing a tennis scoring system were:

1. **Complex Scoring Rules** - Tennis has unique scoring terminology and rules that don't follow typical numerical progression. Converting between internal point representation and tennis-specific scoring terms required careful design.

2. **State Management** - Tracking game states (regular play, deuce, advantage) and set states (regular games, tiebreak) needed clear separation of concerns.

3. **Edge Cases** - Handling scenarios like:
   - Multiple deuce-advantage sequences
   - Tiebreak initiation at 6-6
   - Set winning conditions (6-0 vs 7-5 vs 7-6)

### Design Decisions

1. **Class Structure**
   - `Match`: Top-level coordinator
   - `Set`: Manages games and tiebreak
   - `Game`: Handles individual game scoring
   - `TieBreak`: Specialized scoring for tiebreaks

2. **Type Safety**
   - Custom types for player names
   - Strict return types
   - Exception handling for invalid players

3. **Constants Management**
   - Centralized scoring constants
   - String formatting templates
   - Game/Set thresholds

### Compromises & Tradeoffs

1. **Validation**: Following requirements, minimal input validation is implemented, assuming correct data.

2. **State Representation**: Chose simple integer counting over state enums for readability.

3. **Score Format**: Selected string representation that balances readability with parsing simplicity.

## Technical Details

### Requirements

- Python 3.8+
- pytest for testing
- flake8 for linting

### Project Structure

```
tennis/
├── __init__.py
├── constants.py
├── game.py
├── match.py
├── set.py
└── tiebreak.py

tests/
├── __init__.py
├── test_game.py
├── test_match.py
├── test_set.py
└── test_tiebreak.py
```

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/tennis-scoring.git
cd tennis-scoring
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install pytest flake8
```

### Git Hooks

The project uses git hooks for code quality:
- Pre-commit hook runs flake8 to ensure code style compliance

### Running Tests

Run all tests:
```bash
pytest
```

Run specific test file:
```bash
pytest tests/test_match.py
```

Run with coverage:
```bash
pytest --cov=tennis tests/
```

### Linting

Check code style (automatically runs on commit):
```bash
flake8 tennis/ tests/
```

### Usage Example

```python
from tennis import Match

match = Match("player 1", "player 2")

# Score a point
match.point_won_by("player 1")
print(match.score())  # "0-0, 15-0"

# Score multiple points
match.point_won_by("player 2")
match.point_won_by("player 1")
match.point_won_by("player 1")
print(match.score())  # "0-0, 40-15"
```

## Code Quality

The project follows these principles:
- SOLID design principles
- DRY (Don't Repeat Yourself)
- Clear separation of concerns
- Comprehensive test coverage
- Type hints throughout
- Consistent code style (flake8)

## License

MIT License - See LICENSE file for details 