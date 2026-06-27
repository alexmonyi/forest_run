**Forest Run**  
A 2D side-scrolling forest escape game built with **Pygame Zero** — dodge a wolf and a bat, collect coins, and make it out alive.  
**Story**  
This a forest advenure with two things chasing you and a handful of coins scattered along the way. Grab every coin to win, but watch your health — three hits from the wolf or the bat and it's game over.  
**Features**  
- Side-scrolling movement with jumping and gravity  
- Two animated enemies (wolf and bat) patrolling fixed zones  
- Coin collection with a win condition  
- Health system with collision-based damage  
- Sound effects (jump, coin pickup, hit, win) and background music  
- Menu screen with a music on/off toggle  
- Win/Game Over screens, with automatic return to the menu after winning  
**Controls**  
| | |  
|-|-|  
| **Key** | **Action** |   
| Left / Right Arrow | Move |   
| Spacebar | Jump |   
| Mouse Click | Interact with menu buttons |   
   
**How to Run**  
**1. Clone the repository**  
git clone https://github.com/alexmonyi/forest_run.git  
 cd forest_run  
   
**2. Set up a virtual environment (recommended)**  
python -m venv .venv  
 source .venv/bin/activate  
   
**3. Install dependencies**  
pip install -r requirements.txt  
   
**4. Run the game**  
pgzrun game.py  
   
**Project Structure**  
forest_run/  
 ├── game.py  
 ├── images/  
 ├── sounds/  
 ├── music/  
 ├── fonts/  
 ├── requirements.txt  
 └── README.md  
   
**Objective**  
Collect all 5 coins scattered around the forest while avoiding the wolf and bat. Reach 0 health and it's game over. Collect every coin and you win — the game automatically returns to the main menu a few seconds later so you can play again.  
**Built With**  
- [Python](https://www.python.org/ "https://www.python.org/")  
- [Pygame Zero](https://pygame-zero.readthedocs.io/ "https://pygame-zero.readthedocs.io/")  
**Author**  
Alex Imbukule Monyi  
