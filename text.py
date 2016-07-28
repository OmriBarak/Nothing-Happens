import enum
from enum import Enum
class Justify(Enum):
    LEFT = 1
    CENTER = 2
    RIGHT = 3

import curses
import colorama
from colorama import Fore, Back
colorama.init() #If this is a bug, then do "from colorama import init" as well


#TODO: Figure out how to create a window that behaves like a normal console would.
'''
Each text object is a quintuple, stored as ("text", UID, POS, JUSTIFY).

"UID" is a three-digit number that allows you to access the text to change its properties and position other text relative to it:
    - 000 is a reserved (and unused) UID.
    - UIDs with low numerical values are generally reserved for static text
    - If the text is part of the player's input and feedback, then * is placed at the front of it.
        This indicates that whenever the user presses enter it is to scroll up with the rest of the text.

"POS" is the position of the text, and is formatted as a triple: ("[!|%]y", "[!|%]x", rel)
    ! indicates an absolute number of characters away,
    % indicates the percentage of the screen away.
    rel is the UID of another text object if you want to anchor it relative to that.
        
JUSTIFY indicates whether the text is left-justified, centered, or right-justified.
    You have Justify.LEFT, Justify.CENTER, and Justify.RIGHT.

Bold text is written inside !exclamation marks!.
Colored text is written using colorama.

OBVIOUS DO-NOTS:
    - Do not position text relative to itself
    - Close all your formats!
'''

#TODO: great, now implement it.

#this keeps track of all the text that we have onscreen
_onScreenText = []

#resets the display to a blank slate
#the maxUID parameter instructs the display to keep all text with a UID below what is specified.
def clear_display(maxUID = 999):
    pass

#refreshes the display
#if the terminal window is resized, this updates all positions with percentage values
#unconditionally removes all objects that are entirely off-screen.
def refresh_display():
    #first updates text whose position is NOT relative, and then text whose position is relative.
    pass

#Adds a string to the display.
#If the position is left as default, it treats it like a print command and scrolls the rest of the text up a line
def add_string(text, uid, justify = Justify.LEFT, pos = "0x0x0"):
    pass

#Removes a string from the display.
def remove_string(uid):
    pass

#Changes a string's position in the display
def change_string_position(uid, pos):
    #check if position is a valid string
    
    pass

#Changes a string's text in the display
def change_string_text(uid, text):
    pass

#Changes a string's justification in the display
def change_string_justify(uid, justify):
    pass

def make_string_relative(uid, rel):
    pass

#Gets all the UIDs of the string objects. Used for functions in the same vein as clear_display(maxUID)
def get_all_uids():
    pass

#Get user input for commands, etc.
def user_input():
    pass
