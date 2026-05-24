# Guess The Number Game

An interactive, logic-based desktop game built with Python and CustomTkinter. The application generates a secret random number, and the player tries to guess it using strategic hints, practicing clean state management and event-driven programming.

## 🚀 Key Features

- **Limited Attempts:** The player has exactly **8 attempts** to guess the correct number before the game ends.
- **Dynamic Proximity Hints:** Gives real-time feedback on every guess with tailored hints (e.g., *Too Low*, *Too High*, *Very Close*, *Warm/Cold*).
- **Clean Navigation System:** Multi-page frame switching routing (Welcome screen, Rules, Game loop) managed via a centralized controller.
- **Modern Dark-Themed UI:** A polished geometric user interface with consistent button parameters and color schemas.

## 🛠 Tech Stack

- **Language:** Python 3.11+
- **GUI Framework:** CustomTkinter
- **Architecture:** Object-Oriented Programming (OOP) with an event-driven `Controller` pattern.

## 📸 Preview

<img width="446" height="392" alt="image" src="https://github.com/user-attachments/assets/b5a9cc7f-e85d-4624-8679-351f33a24c54" />


## 💻 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com
   ```
2. Install dependencies:
   ```bash
   pip install customtkinter
   ```
3. Run the application:
   ```bash
   python main.py
   ```
