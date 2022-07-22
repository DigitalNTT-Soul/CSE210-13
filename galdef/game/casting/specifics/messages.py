from config import *
from game.casting.basics.actor import Actor
import os

class Messages(Actor):
    """The game stats."""

    def __init__(self):
        """Constructs a new Stats."""
        super().__init__()
        
        self._restart_message = "PRESS  R  TO  RESTART"
        self._game_start_message = "PRESS  ENTER  TO  START"
        self._exit_game_message = "PRESS  ESC  TO  EXIT"
        self._high_score = 0
        self._compare_score = ""
        self._high_level = 0
        self._game_over_message = f"GAME  OVER!\nTO  PLAY  AGAIN  PRESS  R\nOR  PRESS  ESC  TO  EXIT  THE  GAME\n \nTHE  HIGH  SCORE  TO  BEAT  IS:    {self._high_score}\n THE  HIGH  LEVEL  TO  BEAT  IS:    {self._high_level}"

    def compare_and_store(self, compare_score, compare_level):
        """ 
        Compares players score with the current high score. If the players high score in bigger stores the players score as the new high score in the High_Score.txt file. Updates class variables with the first name, last name, and hight score from the High_Score.txt file

        Args:
            self (High_score): An instance of High_score.
        """
        with open(HIGH_SCORE_FILE, "r") as file: # Open file
            high_score_info = file.readlines() # get the info from first line as a string and placed in the first index of a string.
            high_score_info = str(high_score_info[0]) # take the info in the first index of the list and make it a string
            high_score_info = high_score_info.split() # make a new list with each part of the string placed in a seperate index
            self._high_score = high_score_info[0] # get the hight score from list and update class high score variable
            self._compare_score = compare_score
            # file closes at this point

        if int(self._high_score) < int(compare_score): # compare current high score with player high score
            self._high_score = compare_score # make the player's high score the current high score
            self._high_level = compare_level # make the player's high level the current high level

            string_high_score = str(self._high_score) # make high score a string
            string_level = str(self._high_level) # make high level a string
            with open(HIGH_SCORE_FILE,'w') as file: # delete info on file
                pass
            with open(HIGH_SCORE_FILE, "w") as file: # Open file
                # file.truncate(0)  # delete the info in the file
                file.write(f"{string_high_score} {string_level}") # write new high score to file
                # file closes at this point
         
        with open(HIGH_SCORE_FILE, "r") as file: # Open file
            high_score_info = file.readlines() # get the info from first line as a string and placed in the first index of a string.
            high_score_info = str(high_score_info[0]) # take the info in the first index of the list and make it a string
            high_score_info = high_score_info.split() # make a new list with each part of the string placed in a seperate index
            self._high_score = high_score_info[0] # get the hight score from list and update class high score variable
            self._high_level = high_score_info[1] # get the level from list and update class high score variable
            # file closes at this point
            
    def retrieve_high_score(self):
        """ 
        Updates class variables with the first name, last name, and hight score from the High_Score.txt file

        Args:
            self (High_score): An instance of High_score.
        """

        with open(HIGH_SCORE_FILE, "r") as file: # Open file
            high_score_info = file.readlines() # get the info from first line as a string and placed in the first index of a string.
            high_score_info = str(high_score_info[0]) # take the info in the first index of the list and make it a string
            high_score_info = high_score_info.split() # make a new list with each part of the string placed in a seperate index
            self._high_score = high_score_info[0] # get the hight score from list and update class high score variable
            self._level = high_score_info[1] # get the level from list and update class high score variable
            # file closes at this point
            return high_score_info

    def get_game_over_message(self):
        return self._game_over_message
        
    def get_restart_message(self):
        return self._restart_message

    def get_game_start_message(self):
        return self._game_start_message

    def get_exit_game_message(self):
        return self._exit_game_message
