"""
File: CollectNewspaperKarel.py
Name: Rachel
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

from karel.stanfordkarel import *


def main():
    """
    Pre-condition: Karel is standing at Street 4,Avenue 3,facing East.
    Post-condition: Karel goes all the way to Street3, Avenue 6,picks up beeper(AKA the newspaper and brings beeper home.
                    Home location is at Street 4,Avenue 3.

    """
    move_to_beeper()
    bring_beeper_home()


def move_to_beeper():
    """
    Pre-condition: Karel is standing at Street 4,Avenue 3,facing East.
    Post-condition: Karel moves toward East twice,turns right,moves on time,turns right and picks up beeper.
    """
    move()
    move()
    turn_right()
    move()
    turn_left()
    move()
    pick_beeper()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def bring_beeper_home():
    """
       Pre-condition: Karel is standing at Street3, Avenue 6,facing East.
       Post-condition: Karel wants to home. (Home location: Street 4,Avenue 3)
                       Instructions: Turn left twice,move once, turn right, move twice,turn left, move twice.

       """
    turn_left()
    turn_left()
    move()
    move()
    move()
    turn_right()
    move()
    turn_right()
    put_beeper()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)

