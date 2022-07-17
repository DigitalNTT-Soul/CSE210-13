# Galactic Defense
---

This game combines 80's nostalgia with Modern Python. If you loved Space Invaders (Atari fans anyone??), you'll appreciate this modern interpretation of an old classic. Game is set to actual locations in our universe (technically the truth - minuse the 80's synthwave location).


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

Fire you spaceship's guns at the approaching enemy aliens! Make sure to avoid their return fire, because with each hit your ship takes, it decreases your total lives by 1. If your total lives reach 0, the game is over.

The enemy will move east/west across the screen, dropping one level each time they reach a side, edging closer and closer to your ship.

## Project Structure
---

```
galdef                        
+--                           
  +-- game                    
    +-- directing             
      +-- director.py         
    +-- casting
        +-- basics               
          +-- actor.py 
          +-- animation.py
          +-- body.py
          +-- cast.py
          +-- image.py
          +-- label.py
          +-- rectangle.py
          +-- sound.py
          +-- text.py
        +-- specifics
          +-- alien.py
          +-- background.py
          +-- explosion.py
          +-- projectile.py
          +-- ship.py
          +-- stats.py
    +-- scripting
      +-- action.py
      +-- alien_fire_projective.py
      +-- bullet_collide_alien_action.py
      +-- bullet_collide_ship_action.py
      +-- control_ship_action.py
      +-- draw_actors_action.py
      +-- move_actors_action.py
      +-- move_alien_action.py
      +-- mute_unmute_action.py
      +-- player_fire_projectile_action.py
      +-- prune_explosions_action.py
      +-- prune_missed_shots_action_action.py
      +-- script.py       
    +-- services              
      +-- keyboard_service.py
      +-- physics_service.py
      +-- sound_service.py
      +-- video_service.py    
    +-- shared                
      +-- point.py
      +-- os_tool.py            
      +-- color.py            
  +-- __main__.py             
  +-- config.py               
  +-- README.md                 
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