# rock-paper-scissors-exercise
This repo contains a basic command-line game of rock-paper-scissors. 
## Installation
Clone or download this repo onto your local computer. Once the repo is cloned/downloaded, navigate there from the command line. (see below for reference)
```
cd rock-paper-scissors-exercise
```
## Setting up
You have the option of Setting up a virtual environment. 
```
conda create -n my-rps-game-env python=3.8
conda activate my-rps-game-env
```
Be sure to install the required packages:
```
pip install -r requirements.txt
```
### Configuring Environment Variables
Add a new ".env" file to the root directory of this repo, and assign the desired player name. See below for an example.
```
PLAYER_NAME="Steven"
```
## Running the Game
To run the game:
```
python game.py

Note: when prompted to choose between "rock", "paper" and "scissors" be sure to respond in lower case.


