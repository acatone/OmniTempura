# Declare characters used by this game. The color argument colorizes the
# name of the character.
define MC = Character("[name]")
define NPC = Character("Student")
define U = Character("???")
define A = Character ("Amiel")
define D = Character ("Demir")
define C = Character ("Cassiel")
define M = Character ("Marie")

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
    jump name
label name:
    "After admiring myself for a few good seconds, I grabbed my suitcase and took the ride that would lead me to the Arthame Academy."
    "I find myself in front of a massive gate that lead to the school.
    As I was going to cross the gates, a guardsman stopped me on my tracks"
    "Guardsman" "Pardon me, This area is restricted to the students of the Academy, are you perhaps a new student?"
    "I nodded"
    "The Guardsman took out a small device, and soon another man came running out with a file of papers on hand"
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



    "Student1" "Wow, another new student? [Theyre] pretty late, [they] missed the entire opening ceremony"
    "Student2" "Not that it matters, it was just boring shit like speeches and all anyway. It's good that [they] missed it"
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
    A "Demir Osman II, sorry did I wake you?"
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
