﻿
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define MC = Character("[name]")
define NPC = Character("Student")
define fPronouns = 0
define mPronouns = 0
define nbPronouns = 0

$ appearance = undefined

image character = ConditionSwitch(
    "appearance == 'female'", "images/fem.png",
    "appearance == 'male'", "images/male.png"
    )
    

screen charaselect():
    imagemap:
        idle "images/charaselect_idle.png"
        hover "images/charaselect_hover.png"
        
        hotspot (286, 85, 614, 991) action Jump("male")
        hotspot (1072, 118, 533, 962) action Jump("female")
        

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.
    "I look at myself in the mirror."
    
    call screen charaselect()
    
label female:
    hide screen charaselect
    $ appearance = "female"
    
    show character
    
    "I'm quite beautiful."
    jump name
    
label male:
    hide screen charaselect
    $ appearance = "male"
    
    show character
    
    "I'm quite handsome."
    jump name
 
label name:
    hide character
    
    NPC "Pardon me, but what is your name?"
    python:
        name = renpy.input("What is your name?")
        name = name.strip() or Alex

    NPC "Oh? [name]? It is a pleasure to finally meet you."

    menu:
        NPC "Pardon me for asking again, but how would you like me to refer to you?"

        "My Lady":
            jump choice_F

        "My Lord":
            jump choice_M

        "Your Highness":
            jump choice_NB

label choice_F:
    $ fPronouns = True

    NPC "As you wish, My Lady! Welcome, let me lead you to your chambers"
    jump Intro

label choice_M:
    $ mPronouns = True

    NPC "As you wish, My Lord. Welcome, let me see you to your room."
    jump Intro

label choice_NB:
    $ nbPronouns = True

    NPC " As you wish, Your Highness. Welcome, let me lead you to your room."
    jump Intro

label Intro:
    "You follow the NPC around and see other students staring at you"

    if fPronouns:
        "Student 1" "Whoa, look at her! so pretty!"
    else:
            if mPronouns:
                "Student 1" "Oh my, look at him! Is he new here?"

            else:
                "Student 1" "Whoa, it's a new student!"


    # This ends the game.

    return
