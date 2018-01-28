# The script of the game goes in this file.

#Global variables
define isMorning = True

#Characters
define you = Character("[name]")
define moth = Character("Mother")
define fath = Character("Father")
define uncl = Character("Uncle")
define aunt = Character("Aunt")
define shop = Character("Shop Owner")
define sold = Character("Soldier")
define thief = Character("Thief")
define mech = Character("Mechanic")
define beggar = Character("Beggar")
define rel = Character("Religious Leader")
define lover = Character("Lover")
define friend = Character("Friend")
define fortune = Character("Fortune Teller")
define ruler = Character("Ruler")

#Foo's sprites
# image happy foo = "default/Expression18 - Melissa.png"
# define height = 1457
# define width = 703
# image mom = im.Scale("default/Expression75 - Melissa.png", width*.4,height*.4)
define height = 1150
define width = 640
define scaler = 0.5
image beg1 = im.Scale("sprites/Begger1.png", width*scaler, height*scaler)
image beg2 = im.Scale("sprites/Begger2.png", width*scaler, height*scaler)
image fath1 = im.Scale("sprites/Father1.png", width*scaler, height*scaler)
image fath2 = im.Scale("sprites/Father2.png", width*scaler, height*scaler)
image ft1 = im.Scale("sprites/FortuneTeller1.png", width*scaler, height*scaler)
image ft2 = im.Scale("sprites/FortuneTeller2.png", width*scaler, height*scaler)
image fr1 = im.Scale("sprites/Friend1.png", width*scaler, height*scaler)
image fr2 = im.Scale("sprites/Friend2.png", width*scaler, height*scaler)
image hm1 = im.Scale("sprites/Harem1.png", width*scaler, height*scaler)
image hm2 = im.Scale("sprites/Harem2.png", width*scaler, height*scaler)
image mech1 = im.Scale("sprites/Mechanic1.png", width*scaler, height*scaler)
image mech2 = im.Scale("sprites/Mechanic2.png", width*scaler, height*scaler)
image rel1 = im.Scale("sprites/Religious1.png", width*scaler, height*scaler)
image rel2 = im.Scale("sprites/Religious2.png", width*scaler, height*scaler)
image rule1 = im.Scale("sprites/Ruler1.png", width*scaler, height*scaler)
image rule2 = im.Scale("sprites/Ruler2.png", width*scaler, height*scaler)
image shop1 = im.Scale("sprites/Shopkeeper1.png", width*scaler, height*scaler)
image shop2 = im.Scale("sprites/Shopkeeper2.png", width*scaler, height*scaler)
image sold1 = im.Scale("sprites/Soldier1.png", width*scaler, height*scaler)
image sold2 = im.Scale("sprites/Soldier2.png", width*scaler, height*scaler)
image thief1 = im.Scale("sprites/Theif1.png", width*scaler, height*scaler)
image thief2 = im.Scale("sprites/Theif2.png", width*scaler, height*scaler)
image uncl1 = im.Scale("sprites/Uncle2.png", width*scaler, height*scaler)
image uncl2 = im.Scale("sprites/Uncle1.png", width*scaler, height*scaler)

#Backgrounds
# image default_bg = im.Scale("default/demoScene.jpg", 1066, 600)
image bedroom_bg = im.Scale("scenes/ROOM.jpg", 1066, 600)
image home_bg = im.Scale("scenes/NICEROOM.jpg", 1066, 600)
image marketplace_bg = im.Scale("scenes/MARKETPLACE.jpg", 1066, 600)
image uncle_bg = im.Scale("scenes/UNCLE.jpg", 1066, 600)
image woodshop_bg = im.Scale("scenes/WOODSHOP.jpg", 1066, 600)
image church1_bg = im.Scale("scenes/CHURCH1.jpg", 1066, 600)
image church2_bg = im.Scale("scenes/CHURCH2.jpg", 1066, 600)
image church3_bg = im.Scale("scenes/CHURCH3.jpg", 1066, 600)
image church4_bg = im.Scale("scenes/CHURCH4.jpg", 1066, 600)
image alley_bg = im.Scale("scenes/ALLEYWAY.jpg", 1066, 600)
image brothel_bg = im.Scale("scenes/BROTHEL.jpg", 1066, 600)
image garage_bg = im.Scale("scenes/GARAGE.jpg", 1066, 600)
image fortune_bg = im.Scale("scenes/FORTUNE.jpg", 1066, 600)
image jail_bg = im.Scale("scenes/JAIL.jpg", 1066, 600)
image royal_bg = im.Scale("scenes/ROYALHOUSE.jpg", 1066, 600)
image street1_bg = im.Scale("scenes/SIDESTREET1.jpg", 1066, 600)
image street2_bg = im.Scale("scenes/SIDESTREET2.jpg", 1066, 600)
image street3_bg = im.Scale("scenes/SIDESTREET3.jpg", 1066, 600)
image desert_bg = im.Scale("scenes/DESERT.jpg", 1066, 600)
image hideout_bg = im.Scale("scenes/HIDEOUT.jpg", 1066, 600)

#Transformation
transform furtherLeft:
    xalign 0.25
    yalign 1.4
transform furtherRight:
    yalign 1.4    
 
init python:
    items = [] 
    have = ""
    need = ""
    requiredItems = ["a wire", "a piece of wood", "a horn", "some gears", "an antenna", "a handcrank"]
    showitems = True
   
    def display_items_overlay():
        if showitems:
            ui.frame()
            ui.text("Inventory: " + ", ".join(items))
    def addItem(item):
        if item not in items:
            items.append(item)
    def removeItem(item):
        if item in items:
            items.remove(item)
    def resetInventory():
        items = []
    def iHave():
        have = ""
        for i in range(len(items)):
            if i == len(items)-1:
                have += "and " + items[i]
            else:
                have += items[i] + ", "
        return have
    def iNeed():
        need = ""
        needed = []
        for req in requiredItems:
            if not(req in items):
                needed += [req]
        for i in range(len(needed)):
            if i == len(needed)-1:
                need += "and " + needed[i]
            else:
                need += needed[i] + ", "
        return need
    config.overlay_functions.append(display_items_overlay)
##
$ showitems = False #when you don't want to show the inventory onscreen (cutscenes and the like)
$ showitems = True #when you want to reshow the inventory after the cutscene is over

# The game starts here.

label start:
    $ resetInventory()
    jump main
    return
label main:
    ##### Fade in #####
    show bedroom_bg with Dissolve(0.5)
    $ items = []

    $ name = renpy.input(prompt="What is your name?", default='Mikhayiyl')
    ##### Father wakes you #####
    show fath2 with Dissolve(0.5)
    fath "[name], wake up! Hurry!" 
    hide fath2 with Dissolve(0.5)

    ##### Making the transmitter #####
    show home_bg with Dissolve(0.5)
    hide bedroom_bg with Dissolve(0.5)
    "The two of us work tirelessly throughout the morning. Our shop was small but successful. We create transmitters for people throughout the city..."
    "To think even the Ruler had heard of us!"
    show fath1 at right with Dissolve(1.0)
    "The Ruler ruled over with care, but it was knows that he had an unforgiving disposition. If we messed up our task, death would be a gift."
    hide fath1 with Dissolve(0.5)
    "We finished the transmitter early into the afternoon."
    show fath2 at left with Dissolve(0.25)
    "Father gripped me by the shoulders, tightly."
    fath "Now [name], run this transmitter to the palace for the festival!"
    $ addItem("Transmitter")

    "I nodded solemnly. My family was on the line."
    hide fath2 with Dissolve(0.4)

    ##### Into the street #####
    show street1_bg with Dissolve(0.4)
    hide home_bg with Dissolve(0.5)
    "I ran out of the house, transmitter snug against my chest."
    "Today was the festival, so the streets should be empty, I thought..."
    "I was wrong."
    "I rounded the corner towards the marketplace, and into a large crowd."
    "We bumped and jostled as I made my way through."
    ##### Into the marketplace #####
    show marketplace_bg with Dissolve(0.3)
    hide street1_bg with Dissolve(0.5)
    "Unfortunately, I was not careful enough."
    "Someone bumped into me, and the transmitter flew from my hands as I tried to regain my balance. It hit the ground."
    "Panicking, I ran to it to assess the damage. It was broken, not unfixable."
    $ removeItem("Broken Transmitter") ## for some reason this isn't moving broken transmitter when rolling back
    $ removeItem("Transmitter")
    $ addItem("Broken Transmitter")

    "I could not return home with the broken transmitter, and decided to fix it myself.  I look around the marketplace, formulating a plan."
    "The components I need are: {b}a wire, a piece of wood, a horn, some gears, an antenna."
    "I remember that my Uncle is an Alchemist with a lab nearby. He and Father aren’t on good terms, for good reason, but Uncle would surely help me."
    "There is also a woodworking shop nearby, with a kind shopkeeper. If I ask her for help, no doubt she’d assist me."

    menu:
        "I decide to..."
    
        "Rely on my Uncle.":
            jump uncle
        "Ask the shopkeeper.":
            jump shopOwner

label uncle:
    hide marketplace_bg with Dissolve(0.5)
    jump lab
label shopOwner:
    hide marketplace_bg with Dissolve(0.5)
    jump woodshop

###street1
label street1:
    show street1_bg with Dissolve(0.5)
    ""
    hide street1_bg with Dissolve(0.5)
    jump end


### Uncle's alchemy lab
label lab:
    show uncle_bg with Dissolve(0.5)
    hide marketplace_bg with Dissolve(0.5)
    "I hesitantly pushed open the door to my Uncle’s laboratory, wondering how we could be related as the chemicals hit my nose."
    "My Uncle looked up from his work, smiling at me as I walked towards his desk."
    show uncl1 at left with Dissolve(0.5)
    uncl "[name], child, how are you?"
    you "Not well Uncle. I broke the transmitter we built for the Ruler."
    uncl "And you’ve come to me for help. Does my brother know?"
    "I shake my head, and my Uncle smiled slyly."
    uncl "How nice that you wish to rely on me."
    "I shiver, not completely understanding why."
    show uncl1:
        linear 0.3 xpos 0.3
    "Uncle walks up and pats my head."
    uncl "I’ll give you a wire, and money, if you do a little job for me. You will won’t you."
    "I meekly nod my head."
    uncl "You see, the nearby mechanic has been irritating me. Go to their shop and ‘fix’ their machine for me. Anything you find there you can keep."
    "I nod again. My Uncle went to a shelf, collected a wire, and came back to me. He reached into his coin purse, and pressed both items into my hands."
    $ removeItem("a wire")  
    $ removeItem("a coin")
    $ addItem("a wire")  
    $ addItem("a coin")
    $ display_items_overlay()
    uncl "It’s so great you decided to come to me, [name]."
    "He smiled and pushed me out the door."
    hide uncl1 with Dissolve(0.5)
    hide uncle_bg with Dissolve(0.5)
    jump garage

###Wood shop
label woodshop:
    show woodshop_bg with Dissolve(0.5)
    "I shyly enter the wood shop. It had been ages since I last came in, and I hoped the shopkeeper would remember me."
    "The shopkeeper approached me concerned."
    show shop1 at left with Dissolve(0.8)
    shop "Ah, it’s been a while since I saw you last. Your face is gray, what happened?"
    "The Shopkeepers ability to read the situation made my eyes well up with tears. I chokingly recounted my ordeal as she sympathetically patted my shoulder."
    you "Any help you can give, I would be grateful for!"
    "The shopkeeper sighed and smiled"
    shop "One of my workers decided not come in, so work for me a while, and I’ll give you some wood."
    you "Alright. I'll start right away!"
    hide shop1 with Dissolve(1.2)
    "Finally, the Shopkeeper pulled me aside."
    show shop2 at right with Dissolve(0.5)
    shop "I believe you’ve worked long enough"
    "She gave me the wood I needed, while also placing a coin into my palm."
    $ removeItem("a piece of wood")  
    $ removeItem("a coin")
    $ addItem("a piece of wood")  
    $ addItem("a coin")
    $ display_items_overlay()
    shop "Don't be a stranger!"
    "She winked and sent me on my way."
    hide shop2 with Dissolve(0.5)
    hide woodshop_bg with Dissolve(0.5)
    jump marketplace2
         
###Mechanic's garage
label garage:
    show garage_bg with Dissolve(0.5)
    "I successfully sneak into the empty Mechanic’s shop unsure of what to do. I walk around, poking at several things."
    "I pick up some gears that lay on a table. I might even be able to get a hand crank, I think."
    "I poke around a bit more when I hear the back door opening."

    # SNEAKY SNEAKY
    show thief1 at right with Dissolve(0.25)
    thief "She's back early."
    "A Thief runs past me, knocking me down."
    show thief1:
        linear 0.3 xpos -1.0 ypos 2.0
    hide thief1 with Dissolve(1.0)

    menu:
        "Panicking, I decide to..."
        "Run out the front.":
            jump followTheif
        "Stay where I am.":
            jump stayWhereIAm
    
    label followTheif:
        show marketplace_bg with Dissolve(0.25)
        hide garage_bg with Dissolve(0.25)
        "Following the Thief, I run outside. But a strong arm catches me."
        "I turn around and see the Mechanic."
        show mech1 at left with Dissolve(0.35)
        mech "Trying to steal from me are you?!"
        "She looks me up and down, griping tighter so that tears stung at the edges of my eyes.  A Soldier passes by and she hails him."
        show sold2 at right with Dissolve(0.50)
        mech "This brat tried to steal from me. I doubt they’re the mastermind though. Interrogate them."
        "The Soldier shrugs ascension and looks at me."
        menu:
            sold "Tell me the truth. Were you instructed to harm this business?"
            "Rat our my Uncle.":
                jump ratOut
            "Plead Guilty.":
                jump guilty
        label ratOut:
            "I rat out my Uncle. It was his vendetta that I refused to go down for."
            mech "That cursed man! Using his own relatives for such vile acts."
            "The Mechanic shook me down, taking back the gears I stole. She then went back into her shop, slamming the door."
            show mech1:
                linear 0.3 xpos 0.65
            hide mech1 with Dissolve(0.25)
            sold "It’s great you told the truth."
            show sold2:
                linear 0.2 xpos 0.6
            "Grabbing me, he punched my gut. I fell to the ground heaving."
            sold "For my troubles."
            "The soldier turned on his heel and left."
            hide sold2 with Dissolve(0.2)
            show sold1 with Dissolve(0.2)
            show sold1:
                linear 1.0 xpos 2.0
            hide sold1 with Dissolve(0.1)
            jump marketplace2
        label guilty:
            "I decide to plead guilty. After all I did break in."
            hide mech1 with Dissolve(1.25)
            "The Soldier shrugs, and takes you to the prison."
            hide sold2 with Dissolve(1.5)
            hide marketplace_bg with Dissolve(1.0)
            jump jail

    label stayWhereIAm:
        "I stay where I am, slinking lower behind some crates when I see the Mechanic run out the front towards the Thief."
        "Seeing a clear path, I sneak out through the back. I go straight towards the wood shop."
        hide garage_bg with Dissolve(0.5)
        jump woodshop

label marketplace2:
    show marketplace_bg with Dissolve(0.5)
    "Back at the marketplace, I walk around trying to figure out what to do next."
    you "Getting the horn is what I’m most worried about."
    "As I worry, I trip and fall down. I look up and see it was a beggar."
    show beg2 at left with Dissolve(1.1)
    menu:
        "Alms for the poor?"
        "Give a coin.":
            jump giveCoin
        "Deny the coin.":
            jump denyCoin
    label giveCoin:
        "I give the Beggar a coin."
        beggar "You should be able to get a horn from the Holy Palace."
        you "Thank you so much!"
        "I head to the Palace."
        hide beg2 with Dissolve(0.5)
        hide marketplace_bg with Dissolve(0.5)
        jump church1

    label denyCoin:
        "I deny the Beggar a coin."
        beggar "Humph! Go to the brothel if you want a horn."
        you "Uh... thanks."
        "I warily listen and go to the brothel."
        hide beg2 with Dissolve(0.3)
        hide marketplace_bg with Dissolve(0.5)
        jump brothel

#church1
label church1:
    show church1_bg with Dissolve(0.5)
    "As I walk up to the Holy Palace, there is a commotion."
    show thief2:
        xalign -1.0
        yalign 1.25
    show thief2:
        linear 0.8 xpos 0.45
    "The Thief suddenly runs out the doors, hands full, and pushing me to the ground"
    show thief2:
        linear 0.4 xpos 2.0
    "As I stand I hear metallic clinking. I am surrounded by coins."
    hide thief2 with Dissolve(5.0)
    "People surround me, preventing me from leaving as they get a Soldier."
    show rel2 with Dissolve(0.4)
    rel "The Religious Leader comes up and strikes me across the face."
    show rel2:
        linear 0.5 xpos 0.25
    show sold1 at right with Dissolve(1.0)
    "The Soldier arrests me."
    hide rel2 with Dissolve(0.4)
    hide sold1 with Dissolve(1.25)
    hide church1_bg with Dissolve(0.5)
    jump jail
         
###brothel
label brothel:
    show brothel_bg with Dissolve(0.5)
    show hm1 at left with Dissolve(0.5)
    "I enter the brothel. It is my first time in one and I find it hard to look at the beautiful workers. A worker asks me what I would like, startling me."
    you "A horn. N-not that type! But one that sound can come out of."
    "The worker shrugs and points me to a table with a shiny horn. I reached for the horn, but someone grabbed my wrist."
    "I look up and lock eyes with the Soldier."
    show sold2 at right with Dissolve(0.25)
    sold "What's this? Stealing?"
    you "N-no! I -- !"
    show sold2:
        linear 0.1 xpos 0.6
    "The Soldier pulled my arm taught and raised his sword."
    show sold2:
        linear 0.2 xpos 0.8
    "As the sword swung down, I was suddenly pulled backwards."
    show sold2:
        linear 0.1 xpos 0.6
    show hm1:
        linear 0.1 xpos 0.1
    "I felt arms surround me protectively."
    lover "Not in here!"
    "I look up to see one of the Ruler’s harem member, furiously staring down the Soldier. He shrunk a little."
    sold "Sweetheart, please."
    "The Soldier looked at his Lover pleadingly."
    lover "If you want to fight, go outside. If you want to f-"
    sold "Alright!"
    hide sold2 with Dissolve(0.2)
    show sold1 with Dissolve(0.2):
        xalign 0.6
    show sold1:
        linear 0.2 xpos 1.5
    hide sold1 with Dissolve(1.0)
    "The Soldier went outside, and we followed after."
    show hm1:
        linear 1.5 xpos 1.5
    hide hm1 with Dissolve(2.0)

    show street3_bg with Dissolve(0.5)
    hide brothel_bg with Dissolve(0.5)
    "The three of us stand outside the brothel. Me protectively in the harem members strong arms. The Soldier jealously across from us."
    show sold2 with Dissolve(0.5):
        xalign 0.5
    show hm2 with Dissolve(0.5):
        xalign 0.8
    sold "Why were you taking my horn?"
    hide sold2 with Dissolve(0.2)
    show sold1 with Dissolve(0.2):
        xalign 0.45
    you "My transmitter for the Ruler broke. I have to fix it before the festival!"
    "The Soldier's and Lover's face softened as they looked at each other."
    sold "We can't let the child leave. Stealing aside, they'll talk about my being here to the Ruler. Us or them."
    "The Lover looked at me an caressed my face"
    show hm2:
        linear 0.1 xpos 0.75
    lover "We can't give you the horn. What else do you need?"
    $ have = iHave()
    you "Well... let's see, I have a [have]."
    $ need = iNeed()
    you "And I still need a [need]."
    lover "Oh, well then! I think we can help each other out."

    show sold1: 
        linear 0.3 xpos 1.5
    hide sold1 with Dissolve(0.2)
    "The Lover gestured to the Soldier who went back inside and brought out an antenna."
    show sold2:
        xalign 1.5
    show sold2:
        linear 0.3 xpos 0.6
    sold "I'll give you this on your work that you say nothing of seeing us here."
    "I nod and am given the antenna."
    $ removeItem("an antenna")
    $ addItem("an antenna")
    hide sold2 with Dissolve(0.5)
    hide hm2 with Dissolve(0.5)
    hide street3_bg with Dissolve(0.75)
    jump marketplace3

label marketplace3:
    show marketplace_bg with Dissolve(0.75)
    "I sullenly wandered the stalls, looking for the remaining components."
    show fr2 at left with Dissolve(0.5)
    "I come see my best Friend. He is trustworthy so I run up to him."
    friend "[you], what's up? You're looking down."
    "I tell my story of what has happened to me, but stop when I get to the
brothel."
    menu:
        "I decide to..."
        "Tell what happened at the brothel.":
            jump tellFriend
        "Skip over that part.":
             jump dontTellFriend

label tellFriend:
    "I include the brothel in my story, but am suddenly grabbed."
    show sold2 at right with Dissolve(0.2)
    "I look up and see the Soldier. He grabs my friend as well and drags us into an alleyway."
    show alley_bg with Dissolve(0.3)
    hide marketplace_bg with Dissolve(0.4)
    show sold2:
        linear 0.15 xpos 0.6
    "The Soldier throws us violently against the wall."
    sold "You should have kept your word..."
    show sold2:
        linear 0.1 xpos 0.5
    "Before I can catch my breath I am stabbed."
    hide fr2 with Dissolve(0.1)
    show fr1 at left with Dissolve(0.1)
    show fr1:
        linear 0.2 -2.0
    "My Friend screams and tries to run. He is stabbed as well."
    show sold2:
        linear 0.17 -2.0
    hide alley_bg with Dissolve(1.5)
    "Father..."
    jump end

label dontTellFriend:
    "I skip over the brothel and say that I found the antenna on a side street."
    "A feel a pat on my back and turn to see the Soldier. He had followed me and overheard the entire conversation."
    show sold2 at right with Dissolve(0.5)
    sold "You should see a mystic to avoid any more bad luck."
    friend "My cousin is a Fortune Teller. Tell her I sent you to get a free reading."
    hide sold2 with Dissolve(0.5)
    hide fr2 with Dissolve(0.5)
    hide marketplace_bg with Dissolve(0.5)
    show fortune_bg with Dissolve(0.5)
    "I skeptically enter the Fortune Teller’s shop and look around. The décor is spooky, making me uncomfortable."
    fortune "The unknown is a scary thing, isn't it child?"
    show ft1 at right with Dissolve(0.2)
    "I tell her that my Friend sent me to her."
    fortune "You have avoided many horrible things. But worse is yet to come."
    hide ft1 with Dissolve(1.5)
    menu:
        fortune "You should go to the Holy Palace."
        "Believe her.":
            hide fortune_bg with Dissolve(0.5)
            jump church2
        "Don't believe her.":
            hide fortune_bg with Dissolve(0.5)
            jump street2



###street2
label street2:
    show street1_bg with Dissolve(0.5)
    "I refuse to believe her and leave."
    show thief2:
        xalign -1.0
    show theif2:
        linear 0.5 xpos 0.25
    "As I exit I bump into a Thief. He looks me up and down."
    show theif2:
        linear 0.2 xpos 0.5
    "I am mugged."
    show theif2:
        linear 0.3 xpos 2.0
    "I have lost all the components."
    hide thief2 with Dissolve(0.2)
    "I have failed."
    "Unable to face my Father, I lose myself to the darkest alleyways."
    hide street1_bg with Dissolve(0.5)
    jump end

#church2
label church2:
    show church4_bg with Dissolve(0.5)
    "I believe the Fortune Teller and head straight to the Holy Palace."
    "As I approach, I see the Religious Leader distraught outside."
    show rel2 at left with Dissolve(1.0)
    you "Holy Leader, what is wrong?"
    rel "We have been robbed today. Many of the offerings for the Holy Palace have been lost to this desolate city."
    "He sobbingly put his face into his hands." 
    "I tug on his robe and he lifts his face."
    "I reach into my pocket, pulling out my coin. I place it into his hand."
    "He stares at me, face turning from sorrow to compassion."
    rel "Thank you, young one. Is there anything I could do for you?"
    you "Do you happen to have a horn?"
    "He furrowed his brow in thought before quickly going inside."
    show rel2:
        linear 0.2 xpos 2.0
    hide rel2 with Dissolve(1.0)
    "He came back out with an old, chipped horn."
    show rel1:
        xalign 2.0
    show rel1:
        linear 0.5 xpos 0.8
    rel "I'm sorry, but this old instrument is all we have."
    you "Oh! That'll work fine! Thank you!"
    "I bow and the Religious Leader hands me the horn."
    $ removeItem("a horn")
    $ addItem("a horn")
    hide rel1 with Dissolve(0.5)
    hide church4_bg with Dissolve(0.5)        
    jump marketplace4

label marketplace4:
    show marketplace_bg with Dissolve(0.5)
    "I arrive again at the marketplace when I see something from the corner of my eye."
    show thief1 at left with Dissolve(0.5)
    "The Thief is stealing. The Soldier is nearby, but I don't want to be involved with him again."
    show sold1 at right with Dissolve(0.5)
    menu:
        "The Thief is stealing. The Soldier is nearby, but I don't want to be involved with him again."
        "Call out to the Soldier.":
            jump callSoldier
        "Let the Thief steal.":
            jump letSteal

label callSoldier:
    "Hesitantly, I call out the Soldier."
    "He looks in the direction I’m pointing and see the Thief."
    hide sold1 with Dissolve(0.1)
    show sold2 at right with Dissolve(0.1)
    sold "Oi, you again!"
    "The Thief runs, dropping things, as the Solider gives chase."
    show thief1:
        linear 0.5 xpos -1.0
    show sold2:
        linear 0.3 xpos -1.0
    "I walk up to what the Thief drops and see the Mechanic’s handcrank."
    hide theif1 with Dissolve(0.5)
    hide sold2 with Dissolve(0.5)
    menu:
        "What do you do with the handcrank?"
        "Take it for yourself":
            jump takeHC
        "Give it back to the Mechanic":
            jump returnHC

label takeHC:
    hide marketplace_bg with Dissolve(0.5)
    show home_bg with Dissolve(0.5)
    $ removeItem("a handcrank")
    $ addItem("a handcrank")
    "Once at home I immediately get to work on fixing the transmitter."
    "Father is already at the Palace so I must work on it alone."
    "Before fixing it I double check the parts I have."
    $ have = iHave()
    $ need = iNeed()
    if need == "":
        jump success
    if not(need == ""):
        jump failure
label returnHC:
    "I pick up the hand crank and take it to the Mechanic"
    hide marketplace_bg with Dissolve(0.5)
    show garage_bg with Dissolve(0.5)
    "I enter the empty Mechanic’s shop."
    show mech2 at right with Dissolve(0.5)
    you "Excuse me?"
    "I hear some shuffling and the Mechanic comes from the back. She looks at me with suspicion."
    mech "What is it?"
    "I tell her about the Thief at the marketplace, and that I was returning the hand crank. She rolls her eyes as I pushed it towards her."
    mech "Thanks, but you can have it. I needed a new one anyway."
    "She pushed back towards me."
    mech "There’s some extra gears and a wire lying around, since your fixing
                    something up."
    "I take the gears and wire and go home."
    $ removeItem("some gears")
    $ addItem("some gears")
    $ removeItem("a wire")
    $ addItem("a wire")
    hide mech2 with Dissolve(0.5)
    hide garage_bg with Dissolve(0.5)
    jump takeHC

label letSteal:
    "I let the Thief continue stealing, but follow quietly after when he leaves."
    hide marketplace_bg with Dissolve(0.5)
    hide thief1 with Dissolve(0.5)
    hide sold2 with Dissolve(0.5)
    show hideout_bg with Dissolve(0.5)
    show thief2 at right with Dissolve(0.5)
    show thief2:
        linear 1.0 xpos -2.0
    hide thief2 with Dissolve(1.0)
    "We get to the Thief’s hideout. I watch him go inside and hide by a window."
    "He sets his bag down near the window and inside I see the Mechanic’s hand crank."
    "I quietly reach inside, pull the hand crank out, and go home."
    $ removeItem("a handcrank")
    $ addItem("a handcrank")
    jump takeHC

            
label success:
    "I have all the parts!"
    "I fix the transmitter quickly, giving it a quick shine after it is done."
    "This time I wrap it in several blankets and proudly leave for the Palace."
    hide home_bg with Dissolve(0.5)
    show royal_bg with Dissolve(0.5)
    "As I arrive I see my Father sweating in front of the cold faced Ruler."
    show fath1 at right with Dissolve(0.5)
    show rule2 at left with Dissolve(0.5)
    you "Father - !"
    "I trip and the transmitter falls to the ground."
    "It is quiet."
    "I get up and quickly unravel the blankets to revel an unharmed transmitter. Suddenly there is clapping."
    "I look up and see the source of the noise, the Ruler, walking towards me. He helps me up smiling."
    ruler "Such a smart child to wrap it up. Let the festivities begin!"
    hide fath1 with Dissolve(0.5)
    hide rule2 with Dissolve(0.5)
    "The festival begins."
    "The transmitter plays flawlessly all through the night."
    show rule1 at right with Dissolve(1.0)
    "The Ruler publicly praises your family."
    ruler "All the honors for this family. They are now my Royal Transmitter Technicians!"
    "Thanks to the Ruler’s accolades, my family prospers for generations."
    jump end

label failure:
    "I don’t have all the parts."
    "I do my best to fix the transmitter, but can only hope it holds up during the festival."
    "This time I wrap it in several blankets and fearfully leave for the Palace."
    hide home_bg with Dissolve(0.5)
    show royal_bg with Dissolve(0.5)
    "As I arrive I see my Father sweating in front of the cold faced Ruler."
    show fath1 at left with Dissolve(0.5)
    show rule2 at right with Dissolve(0.5)
    you "Father - !"
    "I trip and the transmitter falls to the ground."
    "It is quiet."
    "I get up and quickly unravel the blankets to revel an unharmed transmitter. Suddenly there is clapping."
    "I look up and see the source of the noise, the Ruler, walking towards me. He helps me up smiling."
    ruler "Such a smart child to wrap it up. Let the festivities begin!"
    hide fath1 with Dissolve(0.5)
    hide rule2 with Dissolve(0.5)
    "The festival begins."
    "The transmitter plays flawlessly, until the party reaches its peak."
    "The transmitter gives out."
    "Under the Ruler’s cold gaze, Father and I try to fix it but fail."
    ruler "I am disgraced thanks to you. Never again shall you work in my realm."
    "We are thrown out of the Palace."
    hide royal_bg with Dissolve(1.0)
    show desert_bg with Dissolve(0.9)
    "Exiled, Father and I wander the desert in search of work."
    fath "I’m sorry [you]. It’s my fault that we’re in this situation. I should have never accepted the task."
    "All I can do is weakly sob. My tears dried up long ago."
    jump end

###fail
label jail:
    show jail_bg with Dissolve(0.75)
    "It is cold and dark. I do not know how many days have gone by. All I know is that I failed the Ruler, and condemned my family to destitution. They are surely exiled, if they are alive. . ."
    jump end

label end:
    $ resetInventory()
    "The end."
    return