# whack-a-mole
Whack-A-Mole is a fun and simple Python terminal game where you try to hit the mole before time runs out.
The game displays a 3x3 grid, and each turn, a mole randomly appears in one of the grid cells.
You type in the row and column numbers to guess the mole’s location. If you’re right → you score a point.

All scores and player names are saved in a database, so you can keep track of progress across multiple plays.

Group Members:
1: Martin Mbuba
2. Marcus Kaunda
3. Jeremy Amani
4. Brilliant Kimari
5. Umuro Woto

How to Play:

Clone this repository:
git clone https://github.com/martinmbuba/whack.a.mole.git
cd whack.a.mole/Game/app

## Features
- Player can enter their name before starting
- There's a timer to time the playtime
- There's a score saved at the end of the game
- The highscore tracking, which is saved in **SQLite** database



## Installation

1. **Clone the repository**
git clone https://github.com/martinmbuba/whack.a.mole.git
cd whack-a-mole


2. Create and activate a virtual environment:
python3 -m venv venv
source venv/bin/activate
     

3. Install dependencies
export PIPENV_VENV_IN_PROJECT=1
pipenv install


## Project Structure
WHACK.A.MOLE/
│-- README.md          
│-- sql_lite.py         
│-- whackamole.db      
│-- __pycache__/          

│-- game/                   
│   |-- Pipfile
│   |-- Pipfile.lock

│-- Game/               
    │-- main.py         
    │-- game.py         
    │-- alembic/        
    │   ├-- env.py
    │   |-- script.py.mako
    │   |-- versions/
    │       |-- ba726559d49a_initialize_tables.py
    │-- alembic.ini     
    │-- app/
        |-- __init__.py
        |-- play.py     
        |-- db.py       
        |-- models/
        │   |-- __init__.py
        │   |-- game.py
        │   |-- player.py

