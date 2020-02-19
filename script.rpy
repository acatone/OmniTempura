# Declare characters used by this game. The color argument colorizes the
# name of the character.
define MC = Character("[name]")
define NPC = Character("Student")
define U = Character("???")
define A = Character ("Amiel")
define D = Character ("Demir")
define C = Character ("Cassiel")
define M = Character ("Marie")
define R = Character("Retainer")

# Where the pronoun Magic Happens

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
    In a world where technology and magic advance side by side, the school invites nobles and royalties from all over the world. And so, the Arthame School of Arts was born."
    "Through the years, the school has become renowned for being the alma mater of many distinguished leaders, and so plenty of royalties and nobbles alike sent their heirs to study there."

    "About a year ago, I was appointed as one of the heirs of my family. Soon after, I was enrolled into the Arthame Academy to study the ins and outs about running our growing empire."
    "Today was the day where I bid my family a temporary farewell. I freshened up myself and sat in front of the mirror after getting dressed."
    "I look at myself in the mirror,"

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
    "At least, that was what the people said when they wanted to please me. Whether it is sincerity or pleasantries, only the Goddess could tell."
    "I walked down the stairs to see the carriage already waiting for me. My items already packed neatly into a few suitcases. I climbed on the carriage and bid farewell to my mother."
    "My Father, being a major figure of the empire, and his presence is required within the court, and so he could not see me off on this day."
    "The trip to the academy took a few hours, which I spent reading the book in preparation for the classes. When we arrived, my retainer, ___, knocked on the carriage door."
    "He offered his hand to help me descend the carriage, while the coach helped carry my suitcases from the carriage."
    R "We have arrived in the Arthame academy, Your Royal Highness."
    "I stepped down the carriage and saw a man approaching me with a list. That must be the new students' names."
    U "Oh! I recognize that family crest! Welcome, welcome! Welcome to the Arthame Academy! I have heard that the one of the three children of The Empire would be enrolling to this academy."
    "I can tell from a glance that this man was trying to gain my favour. How despicable."
    "My retainer glared at him and the man shrunk away in fear before asking me for his name"
    U "Uh, um. Forgive me for my ignorance, this humble one does not recognize his place and stepped out of bounds. For formality's sake, may I ask for your name, Your Highness?"
    python:
        name = renpy.input("What is your name?")
        name = name.strip() or Maine

    U "Oh? [name]? It is a pleasure to finally meet you! Welcome to the Arthame Academy- "

    menu:
        U "Ha ha, Pardon me for my rudeness again, but how would you like me to refer to you?"

        "My Lady":
            jump choice_F

        "My Lord":
            jump choice_M

        "Your Highness":
            jump choice_NB

label choice_F:
    $ fPronouns = True

    U "As you wish, My Lady! Welcome, let me lead you to the main hall for the opening ceremony."
    jump Intro

label choice_M:
    $ mPronouns = True

    U "As you wish, My Lord. Welcome, let me lead you to the main hall for the opening ceremony."
    jump Intro

label choice_NB:
    $ nbPronouns = True

    U " As you wish, Your Highness. let me lead you to the main hall for the opening ceremony."
    jump Intro

label Intro:
    "I follow him into the main hall to see everyone waiting in a large hall. In there, you see a couple of other students staring at you"

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



    "Student1" "I see, they've finally chosen the heir to The Empire. I wonder if [they] will end up like [their] father?"
    "Student2" "shh, keep your voice down, it is rude to speak out of turn,"
    R "[title], do not pay them any heed. People have always scorned the unknown, you have done them no wrong."
    "I turned to look at my retainer and nodded."
    R "Perhaps it is wrong to enroll you into this academy, such loose mouths shows me this school is not fit for you, [title]."
    MC "It's alright, many of the students are here to seek knowledge and learn the workings of the world, you cannot expect too much yet. This is just the first day"
    R "Your are too forgiving, [title]."

    # Stuff happens here, Imma just skip to the greenhouse
    "heehoo lesson time and shit happens anyway lets skip to the greenhouse "
    jump GH1


    label GH1:
    MC "Hey! Wait! You don't have to!"
    "I didn't think that he was serious about going to the greenhouse to harvest some enchanted fruits."
    menu:
        "Follow him to the greenhouse":
            "I didn't want him to get in trouble for taking fruits from the greenhouse so I followed after him."
            jump greenhouse_1
        "Wait for him to come back":
            "I sighed, and decide to wait for him to come back.{p} Hopefully he won't get into too much trouble."
            jump greenhouse_0

    label greenhouse_1:
    screen greenhouse_day
    "I ran after him, and found myself in the greenhouse. There, I see him talking with another student who seemed to have been taking a nap in the greenhouse"
    show amiel smile at right
    A "Demir Osman, sorry did I wake you?"
    D "It's alright,"
    "The taller man gives him a lopsided smile. He gets up and dusts himself off."
    D "Are you going to eat all that yourself? That's quite a lot"
    A "Yes! I was going to spare you some, of course"
    D "That's very nice, Amiel"
    "You saw another man enter the greenhouse from a different door."
    U "Ah, my two favourites students, {p}Doing some gardening?"
    D "Amiel was, I just happened to choose the greenhouse to nap in today"
    A "I'm not actually sure what effects my spell had on the fruits, so I wanted to do a little inspection and experiments before consuming them."
    A"I wonder if we can have cakes or tarts on the menu today. I'll give some to the pantry as a little hint."
    U "I see, it's pretty warm in here so don't fall asleep before class, Demir. {p}And Amiel, your gardening skills are blooming beautifully."
    "I watched as the white-haired man pat the two boys on the head gently."
    D "Yes, Professor."
    "Amiel nodded as well"
    D "Talking about fruit tarts, I saw some fruit tarts being made this morning... {p}Or if you preferred cakes, I could whip up some cakes too if you'd like."
    A "You would? That would be lovely!{p} However.... class begins in an hour or so, maybe this afternoon shall do?"
    D "Ah, you’re right. Then this afternoon will do!"
    U "If you make cakes, I’d love to try some."
    "You saw the white haired man reach out towards the flowers and perhaps it was a trick of the eye, but they seem to bend in his direction"
    "Amiel was too distracted by the idea of fruit desserts, but Demir seems to notice as well, but does not say anything"
    D "I’ll save some for you then, Professor"
    U "Great, see you at class,"
    hide amiel
    "The white haired professor gently patted their heads before the two other students headed in different directions"
    "Amiel paces towards the pantry, admiring the halls and pays attention to all the flower vases that he passes by, saying hello and thanking them in his head"
    "While Demir goes to his chambers to change clothes, fix his hair... he looked like a mess in the greenhouse. That wasn’t proper of him."

    menu:
        MC "It seems that I was worried for nothing, Where should I go now?"


        "Stay in the greenhouse":
            "I decided to approach the white-haired professor"

        "Follow Amiel to the pantry":
            "I decided to follow Amiel to the pantry"

        "Follow Demir to the dorms":
            "I decided to follow Demir to the dorms"

    label greenhouse_0:
    "(I guess MC meets Marie here instead?)"
    # This ends the game.

    return
