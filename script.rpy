# Declare characters used by this game. The color argument colorizes the
# name of the character.

define MC = Character("[name]")
define NPC = Character("Student")
define U = Character("???")
define fPronouns = 0
define mPronouns = 0
define nbPronouns = 0
default Their = "Their"
default their = "their"
default Theirs = "Theirs"
default theirs = "theirs"
default They = "They"
default they = "they"
default Themself = "Themself"
default themself = "themself"
default Them = "Them"
default them = "them"
default Theyre = "They're"
default theyre = "they're"
default TheyWere = "They were"
default theyWere = "they were"
default Title = "Your Highness"

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

    scene bg castle
    "The Moncalieri Castle was a building that stood against time, once owned by the House of Savoy.
    It resided in Romar, a little bit north of the Capital, secluded yet not far from life."
    "Though as time grew on the Savoys had no use for the castle and thus the residence was passed down to the Hofmanns, an Aldovian noble family."
    "Many years ago, a man named Christoph Hoffmann, the youngest son of the noble family sought to use the castle grounds to create a unique school fit for nobles and royalties alike."

    "Through the means of magic, the school works with the heavens and other realms alike.
    In a world where technology and magic advance side by side, the school invites nobles and royalties from all over the world "
    "through means of time travel, apparitions, and many other magical transportations, the Arthame School of Arts was born.
    Through the years, the school has become renowned for being the alma mater of many distinguished leaders."

    "Just a few months ago, I received an invitation to study at this prominent academy,
    Today was the day where I bid my family a temporary farewell and find ways to educate myself of the ins and outs of running an empire."
    "After a quick bath, I look at myself in the mirror,"

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

    "After admiring myself for a few good seconds, I grabbed my suitcase and took the ride that would lead me to the Arthame Academy."
    "I find myself in front of a massive gate that lead to the school.
    As I was going to cross the gates, a guardsman stopped me on my tracks"
    "Guardsman" "Pardon me, This area is restricted to the students of the Academy, are you perhaps a new student?"
    "I nodded"
    "The Guardsman took out a small device, and soon another man came running out with a file of papers on hand"
    jump name
label name:
    hide character

    U "Oh! One of the new students are here! May I ask what you name is?"
    python:
        name = renpy.input("What is your name?")
        name = name.strip() or Alex

    U "Oh? [name]? It is a pleasure to finally meet you! Welcome to the Arthame Academy- "

    menu:
        U "Pardon me for asking again, but how would you like me to refer to you?"

        "My Lady":
            jump choice_F

        "My Lord":
            jump choice_M

        "Your Highness":
            jump choice_NB

label choice_F:
    $ fPronouns = True

    U "As you wish, My Lady! Welcome, let me lead you to the main hall, the rest of the students are already gathered there. You're a little bit late, you see..."
    jump Intro

label choice_M:
    $ mPronouns = True

    U "As you wish, My Lord. Welcome, let me lead you to the main hall, the rest of the students are already gathered there. You're a little bit late, you see..."
    jump Intro

label choice_NB:
    $ nbPronouns = True

    U " As you wish, Your Highness. let me lead you to the main hall, the rest of the students are already gathered there. You're a little bit late, you see..."
    jump Intro

label Intro:
    "You follow the him into the main hall to see everyone waiting in a large hall. In there, you see a couple of other students staring at you"

    if fPronouns == True:
        $ Their = "Her"
        $ their = "her"
        $ Theirs = "Her"
        $ theirs = "her"
        $ They = "She"
        $ they = "she"
        $ Themself = "Herself"
        $ themself = "herself"
        $ Them = "Her"
        $ them = "her"
        $ Theyre = "She's"
        $ theyre = "she's"
        $ TheyWere = "She was"
        $ theyWere = "she was"
        $ title = "My Lady"
    else:
            if mPronouns == True:
                $ Their = "His"
                $ their = "his"
                $ Theirs = "His"
                $ theirs = "his"
                $ They = "He"
                $ they = "he"
                $ Themself = "Himself"
                $ themself = "himself"
                $ Them = "Him"
                $ them = "him"
                $ Theyre = "He's"
                $ theyre = "he's"
                $ TheyWere = "He was"
                $ theyWere = "he was"
                $ title = "My Lord"
            else:
                pass



    NPC "Wow, is that the new student? [Theyre] really good looking!"
    NPC "My heart is beating so fast just from looking at [them]"
    # This ends the game.

    return
