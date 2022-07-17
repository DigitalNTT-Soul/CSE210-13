# Greed

greed; noun
 
/grēd/

 An intense and selfish desire for something, especially wealth, power, food, or resources.

 "Greed motivated the miner to collect as many gems as possible, while leaving only the rocks for the other miners" 

---

Greed is a game in which the player seeks to gather as many falling gems as possible. The game continues as long as the player wants more!

## Getting Started

---

Make sure you have Python 3.10.4 or newer installed and running on your machine. Open terminal or PowerShell and
browse to the project's root folder. Start the program by running the following command.

```
pip install raylib
```

```
python3 greed
```

You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the
project folder. Select the main module inside the hilo folder and click the "run" button.

There are some rules to this game and are listed as follows:

- Gems (*) and rocks (o) randomly appear and fall from the top of the screen.
- The player (#) can move left or right along the bottom of the screen.
- If the player touches a gem they earn a point.
- If the player touches a rock they lose a point.
- Gems and rocks are removed when the player touches them.
- The game continues until the player closes the window.

The goal of the game is to collect as many falling gems as possible.

## Project Structure

---

```
root                          (project root folder)
+-- Greed                     (source code for game)
  +-- game                    (specific classes)
    +-- directing             
      +-- director.py         (Director class)
    +-- casting               
      +-- cast.py             (Cast class)
      +-- actor.py            (Actor class)
      +-- debris.py           (Debris class)
    +-- services              
      +-- keyboard_service.py (Keyboard services class)
      +-- video_service.py    (video_service class)
    +-- shared                
      +-- point.py            (Point class)
      +-- color.py            (Color class)
  +-- __main__.py             (program entry point)
  +-- config.py               (config class used to store config data for various game files to access)
+-- README.md                 (general info)
```

## Required Technologies

---

Python 3.10.4

## Authors

---

* Dylan Ruppell (ruppelld@byui.edu) (github: DigitalNTT-Soul):
  - Basic gravity (tunable via config, no floor yet for the player)
  - external config file
  - advised on other code
* Austin Donovan (iskarr9g@gmail.com) (github: Iskarr):
  - First draft of scoring system
  - First draft of Gem and Rock classes that were later merged into Debris class
  - advised on other code
* Matt Pellét (mattpellet@byui.edu) (github: m4j0rCSE):
  - Jump command
  - advised on other code
  - Some QA conducted
* Larry Brys (bry21010@byui.edu) (github: ljbrys):
  - Floor for player to stand on. (i.e. gravity can't push him through)
  - advised on other code
* Ryan Manthey (ryanscom@byui.edu) (github: ryanscom):
  - First Draft of deleting objects when they pass through the floor
  - advised on other code