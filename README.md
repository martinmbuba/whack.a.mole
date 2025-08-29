# whack-a-mole
Whack a mole game

This is a simple **WHACK-A-MOLE** game built in Python.
It uses **SQLite** for storing player scores.

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

