# Galactic Defense
---

This game combines 80's nostalgia with Modern Python. If you loved Space Invaders (Atari fans anyone??), you'll appreciate this modern interpretation of an old classic.


## Getting Started
---

Make sure you have Python 3.10.4 or newer installed and running on your machine. Open terminal or PowerShell and
browse to the project's root folder. Start the program by running the following command"

```
python galdef or python3 galdef
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
raylib


## Authors
---

* Dylan Ruppell (ruppelld@byui.edu) (github: DigitalNTT-Soul)
* Austin Donovan (iskarr9g@gmail.com) (github: Iskarr)
* Matt Pellét (mattpellet@byui.edu) (github: m4j0rCSE)
* Larry Brys (bry21010@byui.edu) (github: ljbrys)
* Ryan Manthey (ryanscom@byui.edu) (github: ryanscom)