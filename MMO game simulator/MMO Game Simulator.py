#imports
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import time
import random

"""this i want to fix- will do these later on, not pressing issues
1. loading page-  want to make the labels in here a bit bigger so no1 strains to see
4. tutorial - maybe can use the label i created
5. add music
6 clean up code proccess, move my global code to below, move my configures to the bottoms, make some of my repeatable code functions.
    might try to make classes as they can remove unnecasarry variables
7.    # if want to make gear would have to put 1 which monster drops what gear, how would character equip them, and an array that holds the information of the gears - could make the database work into this too. will use the dropdown to do determine that gear drop rates
    want to somehow encrypt my code so that people cant see it
    later on if decide to save information can just save the information from the variables and also include a portion where it updates the database in loading page - when i login can make an if and will take the stats saved in the database and make the variables = to that
8. add restrictions on names so that can use profanity languages
9. will need to replace class imgs - doesnt match with monsters
10. create a logout button
11.   in fight page  #need to make a message box or something that holds the information of the fight - can be small covering 4 commands
12. make the game be able to save a game instance associated with a login/pass - would probably make an automatic save in loading page or whatever button you click before switching pages and then another save upon logging out
13. make a file to hold all the imges so wont have multiple files all over the place and then redirect everything in the code
14. include the spell bonus descriptions in fightscreen and main screen
15. edit code to include a tutorial

        #Make new button called player stats that will have shield and mp and regular stats from stat window - and delete mp label
        #need to add shield to monster stats window
        #need to make shields update in variable updates - can include the original set in the if at top
        #want to show mp for character and monster            
        #need to edit stats and monster window to include that physical or magical defence /2 is subtracted by dmg
        #need to make monster spells
        #found a bug where if press end turn too fast the game will freeze for a ec then the timer will go up drammatically past 90 and turn will go up by 1 every second
        #also if press end turn when u have 1 hp will cause a bug that will make you keep going from fight screen to main screen back n forth. - to fix this should put an hp check in end turn so monster turn will never start
        

        plan for now, get everything to work calculation and logic wise, then im going to go back in and add animations
            1. finish spell calculations
            2.Animations - 
                when come back to do animations for spells make a variable called mpchange for the label) and add it at the start of spell activationa nd it will change depending on the spell - and maybe have to make another variable for spells that take all mp, perhaps called currentmp or expectedmploss
                will create like same makeshift animation - when click spell a label will be and it shows dmg/heals/barriers then disappears after 3 seconds - would like it to fade out but no clue yet  -would be an if to decide who gets the label then  would be a probably have to make a def that calls ever 1 second for 3 seconds and make a variable that adds 1 each time until reach 3 then when 3 resets
                will have it make a temporary label that shows the spell animations in between the two characters and a time sleep 0.1 and have it move across the label -might use ai for this part as a lot of work - think might just go ahead and use giphs
                #if a spell grants bonuses or debuffs will have the effect go after the animations and put a after or something.
        
            3. Button deactivation - 
                thinking of making it a def  and before countdown def and call it in countdown - and what it will basically do is if go ahead and make a variable (not character turn because that can bug, perhaps will be like a boolean - basically it will be a variable to check if its already called or not, can add more conditions in monster def), and if character turn = true then it will call the def to check to deactivate buttons with a .after, and inside the def will be another .after to check it again - make sure to also make a character turn variable so when its monster turn this stops activating - will make an if with that
                need to include an if for when when fightmp < MP Cost so spell doesnt activate #currently will make it not activate and show an error message but later on when im deactivating buttons will make it deactivate the button - or maybe do both just in case
                going to make a variable to determine if monster turn or character turn, a boolean- think this will be used for deactivating buttons and much more - if cant figure it out can include an if for where if not your turn will get a popup telling you its not your turn and you cant cast spells (might include this as a backup even if it originally works) and nothing else happens
                need to make it where when turn ends it deactivates all buttons, also in the if not turn 1, can also reactivate all buttons - after that can make another if cooldown != 0 deactivates again

            4. cooldowns
                i didnt add cooldowns yet but will do it soon - might need to add new variable called cooldown for spell functions, if cooldown != 0 then will automatically deactivate the button at the start of the def- might make a small label that pops up for buttons with cooldowns, will just display "0/1/2"

            5. Monster 
                #after that going to go ahead and do the monster attack and animations, character stuff will be copying and pasting from ehre and will be much more work
    
17. need to include more tips- also want to edit it abit because i think i have extra codes , could just try appending based on class - 
    - for each spell a monster cast after a certain ammount of attacks they will gain dmg due to radiation
    - you will lose 1 hp every turn due to radiation, so make sure to finish the fight quickly
    - monsters uses their own mp to cast spells, monsters cannot cast spells without mp and if they start their turn without mp they will skip

18. want to make the graphics more better, i might include giphs and maybe a video like wakfu that introduces the game - and for fighting when you click spell fasts the animations dont glitch and instead they are just done way faster. 
19. need to redo spell arrays - might also make a class so can use edit make an object that holds editable data instead of lots of different variables- wanna make another portion called effect so the description isnt holding calculations- it might be better to just exlcude the formula in spell array dmg and just put the actual spell dmg - who wants to do math? - will probably have to make a spell def so the arrays get redefined too - actually rethinking this and might be better just to use variables and since i can update them and only use the array as an initial starting point.
20. use date time and have it in the fight mini screen that tracks whats happening.
"""                     
#--------------------------------------------Global----------------------
password = "password"
username = "username"
logginerrortxt = "Unable to login at this time, Please try again later."
name = ""

#character stats and precalcultions
currentlvl = 1
pastlvl = 1
hp = 0
    #defences decreases dmg received - need to caluclate it in dmg taken - ex: defence = - (physical_defence*0.5) - wil use an if in the fight, if attack type = this the use physical defence
physical_defence = 0
magical_defence = 0
mp = 0
basedmg = 3

#for counting exp after battler
currentexp = 0
past_expneeded = 50
expneeded = past_expneeded*1.5
lvlupnotification = ""

lvldmg = (currentlvl * 1.5)

#monsters
monstername = "" # will be the display of what monster is chosen - can use this for calculations, chosen_monster changes a lot
chosen_monster = "" #is chosen during loading page - will be used to pull out monster stats
difficulty = "" # saves the difficulty the user chose

timer = 60 #used in fight calculations
pressedEndFight = False #used when ending the fight in fight screen so i know the button was pressed
fightHpandMpset = False #used when determining if hp and mp was already set to the new variable

monsters = [
    {#strong magic but phyically weak
        "name": "Goylca",
        "lvl": currentlvl, 
        "hp": 70 + currentlvl*1.5, 
        "mp": 40, 
        "physical_defence": 1 + currentlvl*1.5, 
        "magical_defence": 10 + currentlvl*1.5, 
        "physical_dmg": 0 + currentlvl*1.5, 
        "magical_dmg": 20 + currentlvl*1.5, 
    },
    {#physical strong but magically weak
        "name": "Bulmar", 
        "lvl": currentlvl, 
        "hp": 100 + currentlvl*1.5, 
        "mp": 20, 
        "physical_defence": 10 + currentlvl*1.5, 
        "magical_defence": 1, 
        "physical_dmg": 20 + currentlvl*1.5, 
        "magical_dmg": 0 + currentlvl*1.5, 
    },
    {#boss
        "name": "Krosmo Crusher", 
        "lvl": currentlvl, 
        "hp": 130 + currentlvl*1.5, 
        "mp": 50 + currentlvl*1.5, 
        "physical_defence": 15 + currentlvl*1.5, 
        "magical_defence": 15 + currentlvl*1.5, 
        "physical_dmg": 15 + currentlvl*1.5,
        "magical_dmg": 15 + currentlvl*1.5, 
    },
    {#all round tank but weak dmg -
        "name": "Hierophant",
        "lvl": currentlvl, 
        "hp": 110 + currentlvl*1.5, 
        "mp": 20, 
        "physical_defence": 10 + currentlvl*1.5, 
        "magical_defence": 10 + currentlvl*1.5, 
        "physical_dmg": 5 + currentlvl*1.5, 
        "magical_dmg": 5 + currentlvl*1.5, 
    }
]

    #will create an array for spells below too spells so they can be global

#USED for stat pages and info pages, actual spell dmg and stuff will be inside spell activation def on fight screen
warriorspells = [
    {
        "Name": "Basic Attack",
        "MP Cost": 0,
        "Damage": "(Base damage * 1.5)",
        "Description": "Hits the target without any MP to lightly damage the target. Gains 3 MP."
    },
    {
        "Name": "Strike",
        "MP Cost": 1,
        "Damage": "(Base Damage * 1.5) + (MP Used * 3) + (lvl * 1.5)",
        "Description": "Strikes the target quickly with your sword. Gains 3 MP."
    },
    {
        "Name": "Swordsmanship",
        "MP Cost": 2,
        "Damage": "(Base Damage * 1.5) + (MP Used * 3) + (lvl * 1.5)",
        "Description": "Uses MP to deal massive damage in a short time. Gains 3 MP."
    },
    {
        "Name": "Warrior's Sword",
        "MP Cost": "100%",
        "Damage": "(Base Damage * 1.5) + (MP Used * 3) + (lvl * 1.5)",
        "Description": "Uses all your MP to deal a very heavy attack. Gains 3 MP."
    },
    {
        "Name": "Advance Shield",
        "MP Cost": 3,
        "Damage": "(Base Damage * 1.5) + (MP Used * 3) + (lvl * 1.5)",
        "Description": "Hits the target to deal damage and steals some HP with MP and generates a shield with it to advance next turn with. Gains 3 MP. The shield is generated at random but will never be less than half of your outputed damage."
    }
]

magespells = [
    {
        "Name": "Staff Attack",
        "MP Cost": 0,
        "Damage": "Base Damage",
        "Description": "Hits the target without any MP to lightly damage the target. Gains 3 MP."
    },
    {
        "Name": "MP Drain",
        "MP Cost": 3,
        "Damage": "(lvl * 1.5)",
        "Description": "Drains the target of MP equal to tripple the MP used. Causes slight damage as the target is being drained. Disables the target for 1 turn due to magic poisoning."
    },
    {
        "Name": "HP Drain",
        "MP Cost": 5,
        "Damage": "15 + (lvl * 1.5)",
        "Description": "Uses magic to drain the target's HP."
    },
    {
        "Name": "Magic Explosion",
        "MP Cost": 10,
        "Damage": "30 + (lvl * 1.5)",
        "Description": "Explodes MP onto the target to deal massive damage."
    },
    {
        "Name": "Damage Debuff",
        "MP Cost": 4, 
        "Damage": "0", 
        "Description": "Reduces  Enemy Damage by 40% for two turns"
    }
]

healerspells = [
    {
        "Name": "Wand Attack",
        "MP Cost": 0,
        "Damage": "Base Damage",
        "Description": "Hits the target without any MP to lightly damage the target."
    },
    {
        "Name": "HP Drain",
        "MP Cost": 5,
        "Damage": "(MP Used * 3) + (lvl * 1.5)",
        "Description": "Drains the target's HP to heal itself."
    },
    {
        "Name": "Protective Barrier",
        "MP Cost": 3,
        "Damage": "0",
        "Description": "Casts a strong shield to block enemy attacks. The shield equals (MP Used * 3) * (lvl * 1.5)."
    },
    {
        "Name": "Sacrificial Lamb",
        "MP Cost": "100%",
        "Damage": "Current HP / 2 + (MP Used * 3) + (lvl * 1.5) + shield / 2",
        "Description": "Sacrifices half of your current HP, shield, and all of your MP to deal one high-damage attack. If you have a barrier, it also consumes half of the barrier. Has a 3-turn cooldown starting from the beginning of the fight."
    },
    {
        "Name": "Heal",
        "MP Cost": 1,
        "Damage": "0",
        "Description": "Heals (MP Used * 3) + (lvl * 1.5) HP at the cost of dealing no damage."
    }
]

fightstatus = None #will be updated to empty(no fight is happening), fight started, or fight ended - this is to tell if a fight is happening or not
fightWon = False #this is to tell if fight was won or not, seperate from fight status
numOfFights = 0 #just a personal status later on for people who will want to know how many fights they did.

#-----------------------------------main window----------------------------------
#Create Window
window = tk.Tk()
window.title("Game Simulator")
window.geometry ("1408x768")
window.configure(bg="black")
window.resizable(False, False)

 #change window background
bg_image = tk.PhotoImage(file="main.png")
bg_label = tk.Label(window, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1) # relwidth/height=1 stretches it 100%

#title
title = tk.Label(
    window,
    text="Game Simulator",
    fg="white",
    bg="#1A1A1A",
    font=("Courier", 30, "bold"))
title.place(relx=0.475, rely=0.4, anchor="center")

#Username label and text input
username_lab = tk.Label(window, text="Username: ", font = ("Ariel", 14), fg="black", bg="white") #window i what adding the label to
username_lab.place(relx=0.4, rely=0.7, anchor="center")

username_entry = tk.Entry(window, font = ("Ariel", 14), bd=2)
username_entry.place(relx=0.52, rely=0.7, anchor="center")

#Password label and text input
password_lab = tk.Label(window, text="Password: ", font = ("Ariel", 14), fg="black", bg="white") #window i what adding the label to
password_lab.place(relx=0.4, rely=0.75, anchor="center")

password_entry = tk.Entry(window, font = ("Ariel", 14), bd=2)
password_entry.place(relx=0.52, rely=0.75, anchor="center")

#login Button Function
def login():
    global password
    global username
    global logginerrortxt
    global entered_user
    global entered_pass


        #is to see if password entered is right
    entered_user = username_entry.get()
    entered_pass = password_entry.get()


    if entered_user == username and entered_pass == password:
        #login procedure - do a try for loading page incase connecting fails then do another try for loading the main game, the loading page is because it might take time to load everything
        loadingpage()

    else: 
        username_entry.delete(0, tk.END) #clears entry box
        password_entry.delete(0, tk.END) #clears entry box

        wronginfo_lab = tk.Label(window, text="Wrong password or username.", font = ("Ariel", 13, "bold"), fg="red", bg="grey") 
        wronginfo_lab.place(relx=0.52, rely=0.63, anchor="center")

#Login Button
login_but = tk.Button(window, text="Login", bg="#00A8FF", font=("Ariel", 16, "bold"), bd=2, width=10, height=2)
login_but.place(relx=0.5, rely=0.86, anchor="center")

#Connect login button
login_but.config(command=login)

#handle loading new pages and in the future will handle after battle calculations
def loadingpage():
    global character_selected
    global fightstatus
    global currentlvl
    global pastlvl
    global hp
    global magical_defence
    global physical_defence
    global basedmg
    global monstername
    global monsters
    #for counting exp after battler
    global expneeded
    global currentexp
    global past_expneeded
    global chosen_monster
    global lvlupnotification
    global pressedEndFight

    print(f"{fightstatus}") #for testing that the fight status  is being updated incase screens aren't witching properly
    
    # 1. Triggered when the Login button is clicked
    try:
        # Destroy the interactive widgets so they disappear - its in a try because if run this again may cause an error because already deleted it
        try:
            username_entry.destroy()
            password_entry.destroy()
            login_but.destroy()
            password_lab.destroy()
            username_lab.destroy()
            title.destroy()
            bg_label.destroy()
        except ValueError:
                print("Code already deleted")

                    #replace background img 
        loadingbg = tk.PhotoImage(file="loadingbg2.png")
        loadingbg_lab = tk.Label(window, image=loadingbg)
        loadingbg_lab.place(x=0, y=0, relwidth=1, relheight=1) # relwidth/height=1 stretches it 100%
        #without this it wouldnt load for some reason - directly saving the whole bg 
        loadingbg_lab.image = loadingbg 
      
        #-------------------------------------------loading... percentage-----------------------------
        # --- VARIABLES ---
        percent = 0  # Holds the actual numerical percentage - need to edit it to where % is displayed afterwards
        dots = ""  # Holds the string of dots ("." or ".." or "...")

        #load text, dots, and percentage
        loadingtxt = tk.Label(window, text=f"Loading{dots} {percent}%", fg="black", bg="purple", width=20, height=2)
        loadingtxt.place(relx=0.5, rely=0.5, anchor="center")

        percent += random.randint(1, 20)

        while percent < 100:
                            #random info on loading screen
            randominfo = ""

            if character_selected == "":
                randominfoarray = [
                    "Pick your character look carefully—it's permanent!", 
                    "Every character starts fresh at Level 1!",
                    "Whatever name you pick is final!"
                    ]
                randominfo = random.choice(randominfoarray)

            elif character_selected == "Mage":
                randominfoarray = [
                    "High MP lets you cast your biggest spells.", 
                    "Watch your HP—if it hits 0, it's game over!", 
                    "Defeat enemies to level up your stats.", 
                    "Always keep an eye on the enemy's health bar!", 
                    "Save your MP for the toughest boss fights.", 
                    "Mages have low resistance to physical attacks!"
                ]    
                randominfo = random.choice(randominfoarray)

            elif character_selected == "Healer":
                randominfoarray = [
                    "High MP lets you cast your biggest spells.", 
                    "Watch your HP—if it hits 0, it's game over!", 
                    "Defeat enemies to level up your stats.", 
                    "Always keep an eye on the enemy's health bar!", 
                    "Use your Heal spell when your HP drops low.", 
                    "Your holy magic deals extra damage to undead monsters."
                ]
                randominfo = random.choice(randominfoarray)

            elif character_selected == "Warrior":
                randominfoarray = [
                    "High MP lets you cast your biggest spells.", 
                    "Watch your HP—if it hits 0, it's game over!", 
                    "Defeat enemies to level up your stats.", 
                    "Always keep an eye on the enemy's health bar!", 
                    "Heavy Armor makes you slow but protects your HP."
                ]
                randominfo = random.choice(randominfoarray)

            randominfo_lab = tk.Label(window, text= f"{randominfo}", fg="black", bg="purple", width=60, height=2)
            randominfo_lab.place(relx=0.5, rely=0.9, anchor="center")

            #Randomly increase percentage (by 5% to 20% each step)
            if percent < 100:
                percent += random.randint(1, 20)

                if percent > 100:
                     percent = 100
                
                # dots that goes up by 1 then resets until variable reaches 100%
                if dots == "...":
                                dots = ""
                                
                else:
                     dots += "."

                loadingtxt.config(text=f"Loading{dots} {percent}%")
                window.update() #without this the timer below will pause the config and the loop will keep running making it seem like the number is jump from 0 to 100

                # random timer for when the percentage goes up (shouldnt be fast tho) 
                wait_time = random.uniform(0.5, 5)
                time.sleep(wait_time)

        #this is so the percent updates correctly - without this may not show correct percent, like might stop at 93
        percent = 100
        loadingtxt.config(text=f"Loading{dots} {percent}%")
        window.update() #without this the timer below will pause the config and the loop will keep running making it seem like the number is jump from 0 to 100

        # random timer for when the percentage goes up (shouldnt be fast tho) 
        wait_time = random.uniform(0.1, 1)
        time.sleep(wait_time)
        #------------------------------caluclate fight stats and status-------------------

        if fightstatus == "Fight Ended":
            fightstatus = ""

            if currentexp == expneeded or currentexp > expneeded:
                if currentexp == expneeded:

                    #resets past exp to cureent exp needed then update expneeded again to have a new value
                    past_expneeded = expneeded + 5
                    expneeded = past_expneeded*1.5
                    currentexp = 0
                    lvlupnotification = "You Have Leveled Up!"
                    currentlvl + 1

                elif currentexp > expneeded:
                    #resets past exp to cureent exp needed then update expneeded again to have a new value
                    past_expneeded = expneeded + 5
                    expneeded = past_expneeded*1.5

                    #reset exp to the overflow exp then lvl up
                    surplusexp = currentexp - expneeded
                    currentexp = surplusexp
                    currentlvl + 1

            if currentlvl > pastlvl:
                hp*1.5
                magical_defence*1.5
                physical_defence*1.5
                basedmg*1.5
                pastlvl = currentlvl

        # make it destroy everything again when its done
        loadingtxt.destroy()
        loadingbg_lab.destroy()
        randominfo_lab.destroy()
        loadingtxt.destroy()
        window.update_idletasks() 

        
        # for choosing which screen to go to
        if character_selected == "":
            characterscreen()

        #sends to fighting screen 
        elif fightstatus == "Fight Started": 
            lvlupnotification = ""
            pressedEndFight = False
            fightscreen()  

        else:
            #Chooses next monster
            chosen_monster = random.choice(monsters)
            monstername = chosen_monster["name"]

            #sends to main screen page'
            mainscreen()

    except ValueError:
       messagebox.showerror("Error", logginerrortxt)

character_selected = "" #for when a character gets selected below
info_labtxt = None
gender = "" #for whenever they select a gender

#character screen, can make it inide an if later once im able to save information can have it where if dont have a character go to this page but if not automatically logins in
def characterscreen():
        #--------------character screen besides button-------------

     #replace background img 
    characterscreenbg = tk.PhotoImage(file="loadingbg2.png")
    characterscreenbg_lab = tk.Label(window, image=characterscreenbg)
    characterscreenbg_lab.place(x=0, y=0, relwidth=1, relheight=1) # relwidth/height=1 stretches it 100%
        #without this it wouldnt load for some reason - directly saving the whole bg 
    characterscreenbg_lab.image = characterscreenbg 

    #label and entry field for name
    entername_lab = tk.Label(window, text="Make a nickname: ", font = ("Ariel", 14), fg="black", bg="purple") #window i what adding the label to
    entername_lab.place(relx=0.383, rely=0.8, anchor="center")

    name_entry = tk.Entry(window, font = ("Ariel", 14), bd=2)
    name_entry.place(relx=0.52, rely=0.8, anchor="center")

        #--------------------------configures gender buttons--------------------------
        #connect switch gender button and caluclations to make it happen - need to do this next
    def malegender():
         global gender
         global character_selected
         global info_labtxt
         gender = "Male"
         #update all pictures and icons to = male version
  
        #had to do multiple ifs because if they didnt select a class had to make it only change preview then on top if that if they chose gender first it would only change the first preview so had to change all of them then add the one for that class i actually wanted to change third so that would be the last img changed and would how that img on the label instead of other classes
         if character_selected == "Warrior":

            #switches the preview img for mage
            m_mageimg = tk.PhotoImage(file="m_mage.png")
            classimgs_lab.config(image=m_mageimg)
            classimgs_lab.image = m_mageimg

            #switches the preview img for healer
            m_healerimg = tk.PhotoImage(file="m_healer.png")
            classimgs_lab.config(image=m_healerimg)
            classimgs_lab.image = m_healerimg

            #switches the preview img for warrior
            m_warriorimg = tk.PhotoImage(file="m_warrior.png")
            classimgs_lab.config(image=m_warriorimg)
            classimgs_lab.image = m_warriorimg

            #switches button icons to female warrior
            m_warrior_icon = tk.PhotoImage(file="m_warrioricon.png")
            warrior_btn.config(image=m_warrior_icon)
            warrior_btn.image = m_warrior_icon

            #switches button icon to female mage
            m_mage_icon = tk.PhotoImage(file="m_mageicon.png")
            mage_btn.config(image=m_mage_icon)
            mage_btn.image = m_mage_icon

             ##switch button icon to female healer
            m_healer_icon = tk.PhotoImage(file="m_healericon.png")
            healer_btn.config(image=m_healer_icon)
            healer_btn.image = m_healer_icon 

            #set txts because without img shows up with no label if dont click class first
            info_labtxt.set("The Warrior is a class focused on delivering high physical damage. Unlike the mage class, it doesn't rely all on mp to cast spells. While highly durable, they have no built-in healing abilities. As they do not rely on mp they have little protecting against magical attacks.\n\n Bonuses: Base damage is multiplied by 1.5 and all spells will use base damage and generate MP but the mp is generated at 2 per spell instead of 3 per spell \n\n\n\n Difficulty: Low\n\n *Make sure to click a class and type a name before you hit the create character button or you will get an error.")

         elif character_selected == "Mage":

            #switches the preview img for warrior
            m_warriorimg = tk.PhotoImage(file="m_warrior.png")
            classimgs_lab.config(image=m_warriorimg)
            classimgs_lab.image = m_warriorimg

            #switches the preview img for healer
            m_healerimg = tk.PhotoImage(file="m_healer.png")
            classimgs_lab.config(image=m_healerimg)
            classimgs_lab.image = m_healerimg

            #switches the preview img for mage
            m_mageimg = tk.PhotoImage(file="m_mage.png")
            classimgs_lab.config(image=m_mageimg)
            classimgs_lab.image = m_mageimg

            #switches button icons to female warrior
            m_warrior_icon = tk.PhotoImage(file="m_warrioricon.png")
            warrior_btn.config(image=m_warrior_icon)
            warrior_btn.image = m_warrior_icon

            #switches button icon to female mage
            m_mage_icon = tk.PhotoImage(file="m_mageicon.png")
            mage_btn.config(image=m_mage_icon)
            mage_btn.image = m_mage_icon

             ##switch button icon to female healer
            m_healer_icon = tk.PhotoImage(file="m_healericon.png")
            healer_btn.config(image=m_healer_icon)
            healer_btn.image = m_mage_icon 

            #set txts because without img shows up with no label if dont click class first
            info_labtxt.set("The Mage is a class focused on delivering explosive magical damage from a distance. Unlike physical classes, it relies heavily on a large mp pool to cast its powerful destructive spells. While they possess incredible offensive capabilities, they have a very low health pool and weak physical defenses.\n\n Bonuses: Magic damage is increased by half of the magic used.\n\n\n Difficulty: Medium\n\n *Make sure to click a class and type a name before you hit the create character button or you will get an error.")

         elif character_selected == "Healer":

            #switches the preview img for warrior
            m_warriorimg = tk.PhotoImage(file="m_warrior.png")
            classimgs_lab.config(image=m_warriorimg)
            classimgs_lab.image = m_warriorimg

            #switches the preview img for mage
            m_mageimg = tk.PhotoImage(file="m_mage.png")
            classimgs_lab.config(image=m_mageimg)
            classimgs_lab.image = m_mageimg

            #switches the preview img for healer
            m_healerimg = tk.PhotoImage(file="m_healer.png")
            classimgs_lab.config(image=m_healerimg)
            classimgs_lab.image = m_healerimg

            #switches button icons to female warrior
            m_warrior_icon = tk.PhotoImage(file="m_warrioricon.png")
            warrior_btn.config(image=m_warrior_icon)
            warrior_btn.image = m_warrior_icon

            #switches button icon to female mage
            m_mage_icon = tk.PhotoImage(file="m_mageicon.png")
            mage_btn.config(image=m_mage_icon)
            mage_btn.image = m_mage_icon

             ##switch button icon to female healer
            m_healer_icon = tk.PhotoImage(file="m_healericon.png")
            healer_btn.config(image=m_healer_icon)
            healer_btn.image = m_healer_icon 

            #set txts because without img shows up with no label if dont click class first
            info_labtxt.set("The Healer is a class focused on self heals and deals low damage for long term fights. It relies on a steady use of mp to cast restorative spells and protective barriers during combat. While they can constantly recover from damage, they possess very low physical and magical damage output but can do a 1 time burst damage with the cost of half their life and all their mp.\n\n Bonuses: Each spell has a healing bonus which is the MP used multiplied by your current lvl * 1.5 and is applied to every spell. \n\n\n Difficulty:  high\n\n *Make sure to click a class and type a name before you hit the create character button or you will get an error.")

         else: # updates all button icons but not preview, there are ifs inside of chose a class that will check what the gender is

            #switches button icons to female warrior
            m_warrior_icon = tk.PhotoImage(file="m_warrioricon.png")
            warrior_btn.config(image=m_warrior_icon)
            warrior_btn.image = m_warrior_icon

            #switches button icon to female mage
            m_mage_icon = tk.PhotoImage(file="m_mageicon.png")
            mage_btn.config(image=m_mage_icon)
            mage_btn.image = m_mage_icon

             ##switch button icon to female healer
            m_healer_icon = tk.PhotoImage(file="m_healericon.png")
            healer_btn.config(image=m_healer_icon)
            healer_btn.image = m_healer_icon 

    def femalegender():
        global gender
        global character_selected
        global info_labtxt
        gender = "Female"
        #update all pictures and icons to = female version

         #had to do multiple ifs because if they didnt select a class had to make it only change preview then on top if that if they chose gender first it would only change the first preview so had to change all of them then add the one for that class i actually wanted to change third so that would be the last img changed and would how that img on the label instead of other classes
        if character_selected == "Warrior":

            #switches the preview img for mage
            f_mageimg = tk.PhotoImage(file="f_mage.png")
            classimgs_lab.config(image=f_mageimg)
            classimgs_lab.image = f_mageimg

            #switches the preview img for healer
            f_healerimg = tk.PhotoImage(file="f_healer.png")
            classimgs_lab.config(image=f_healerimg)
            classimgs_lab.image = f_healerimg

            #switches the preview img for warrior
            f_warriorimg = tk.PhotoImage(file="f_warrior.png")
            classimgs_lab.config(image=f_warriorimg)
            classimgs_lab.image = f_warriorimg

            #switches button icons to female warrior
            f_warrior_icon = tk.PhotoImage(file="f_warrioricon.png")
            warrior_btn.config(image=f_warrior_icon)
            warrior_btn.image = f_warrior_icon

            #switches button icon to female mage
            f_mage_icon = tk.PhotoImage(file="f_mageicon.png")
            mage_btn.config(image=f_mage_icon)
            mage_btn.image = f_mage_icon

             ##switch button icon to female healer
            f_healer_icon = tk.PhotoImage(file="f_healericon.png")
            healer_btn.config(image=f_healer_icon)
            healer_btn.image = f_healer_icon 

            #set txts because without img shows up with no label if dont click class first
            info_labtxt.set("The Warrior is a class focused on delivering high physical damage. Unlike the mage class, it doesn't rely all on mp to cast spells. While highly durable, they have no built-in healing abilities. As they do not rely on mp they have little protecting against magical attacks.\n\n Bonuses: Base damage is multiplied by 1.5 \n\n\n\n Difficulty: Low\n\n *Make sure to click a class and type a name before you hit the create character button or you will get an error.")

        elif character_selected == "Mage":

            #switches the preview img for warrior
            f_warriorimg = tk.PhotoImage(file="f_warrior.png")
            classimgs_lab.config(image=f_warriorimg)
            classimgs_lab.image = f_warriorimg

            #switches the preview img for healer
            f_healerimg = tk.PhotoImage(file="f_healer.png")
            classimgs_lab.config(image=f_healerimg)
            classimgs_lab.image = f_healerimg

            #switches the preview img for mage
            f_mageimg = tk.PhotoImage(file="f_mage.png")
            classimgs_lab.config(image=f_mageimg)
            classimgs_lab.image = f_mageimg

            #switches button icons to female warrior
            f_warrior_icon = tk.PhotoImage(file="f_warrioricon.png")
            warrior_btn.config(image=f_warrior_icon)
            warrior_btn.image = f_warrior_icon

            #switches button icon to female mage
            f_mage_icon = tk.PhotoImage(file="f_mageicon.png")
            mage_btn.config(image=f_mage_icon)
            mage_btn.image = f_mage_icon

             ##switch button icon to female healer
            f_healer_icon = tk.PhotoImage(file="f_healericon.png")
            healer_btn.config(image=f_healer_icon)
            healer_btn.image = f_healer_icon 

            #set txts because without img shows up with no label if dont click class first
            info_labtxt.set("The Mage is a class focused on delivering explosive magical damage from a distance. Unlike physical classes, it relies heavily on a large mp pool to cast its powerful destructive spells. While they possess incredible offensive capabilities, they have a very low health pool and weak physical defenses.\n\n Bonuses: Magic damage is increased by half of the magic used.\n\n\n Difficulty: Medium\n\n *Make sure to click a class and type a name before you hit the create character button or you will get an error.")

        elif character_selected == "Healer":

            #switches the preview img for warrior
            f_warriorimg = tk.PhotoImage(file="f_warrior.png")
            classimgs_lab.config(image=f_warriorimg)
            classimgs_lab.image = f_warriorimg

            #switches the preview img for mage
            f_mageimg = tk.PhotoImage(file="f_mage.png")
            classimgs_lab.config(image=f_mageimg)
            classimgs_lab.image = f_mageimg

            #switches the preview img for healer
            f_healerimg = tk.PhotoImage(file="f_healer.png")
            classimgs_lab.config(image=f_healerimg)
            classimgs_lab.image = f_healerimg

            #switches button icons to female warrior
            f_warrior_icon = tk.PhotoImage(file="f_warrioricon.png")
            warrior_btn.config(image=f_warrior_icon)
            warrior_btn.image = f_warrior_icon

            #switches button icon to female mage
            f_mage_icon = tk.PhotoImage(file="f_mageicon.png")
            mage_btn.config(image=f_mage_icon)
            mage_btn.image = f_mage_icon

             ##switch button icon to female healer
            f_healer_icon = tk.PhotoImage(file="f_healericon.png")
            healer_btn.config(image=f_healer_icon)
            healer_btn.image = f_healer_icon 

            #set txts because without img shows up with no label if dont click class first
            info_labtxt.set("The Healer is a class focused on self heals and deals low damage for long term fights. It relies on a steady use of mp to cast restorative spells and protective barriers during combat. While they can constantly recover from damage, they possess very low physical and magical damage output but can do a 1 time burst damage with the cost of half their life and all their mp.\n\n Bonuses: Each spell has better  individual bonuses than other classes.\n\n\n Difficulty:  high\n\n *Make sure to click a class and type a name before you hit the create character button or you will get an error.")

        else: # updates all button icons but not preview, there are ifs inside of chose a class that will check what the gender is

            #switches button icons to female warrior
            f_warrior_icon = tk.PhotoImage(file="f_warrioricon.png")
            warrior_btn.config(image=f_warrior_icon)
            warrior_btn.image = f_warrior_icon

            #switches button icon to female mage
            f_mage_icon = tk.PhotoImage(file="f_mageicon.png")
            mage_btn.config(image=f_mage_icon)
            mage_btn.image = f_mage_icon

             ##switch button icon to female healer
            f_healer_icon = tk.PhotoImage(file="f_healericon.png")
            healer_btn.config(image=f_healer_icon)
            healer_btn.image = f_healer_icon 

    #--------------------------configure for create character button----------------
    def activateCharacterCreation():
        global gender
        global character_selected
        global hp
        global physical_defence
        global magical_defence
        global mp
        global name

        name = name_entry.get() # save the name so doesnt get lost

        try:
         if character_selected != "" and name != "" and name != " " and name != None:
            

            #assign gender if the gender button wasn't clicked, since male pops up first in the preview
            if gender == "":
                gender = "Male"

            #creating character stats
            if character_selected == "Warrior":
                hp = 90
                physical_defence = 4
                magical_defence = 1
                mp = 0

            elif character_selected == "Mage":
                hp = 70
                physical_defence = 1
                magical_defence = 4
                mp = 4

            elif character_selected == "Healer":
                hp = 80
                physical_defence = 2
                magical_defence = 2
                mp = 3
                
            #destroy everything
            healer_btn.destroy()
            mage_btn.destroy()
            warrior_btn.destroy()
            classimgs_lab.destroy()
            previewheader_lab.destroy()
            info_lab.destroy()
            classinfotxt_lab.destroy()
            left_panel.destroy()
            choseyourclass_lab.destroy()
            createcharacter_btn.destroy()
            Mgender_btn.destroy()
            fgender_btn.destroy()
            chosegender_lab.destroy()
            name_entry.destroy()
            entername_lab.destroy()
            characterscreenbg_lab.destroy()
            window.update_idletasks() 

            #activate loading screen - theres an if in there that will send it to the main screen
            loadingpage()

         else: 
            raise ValueError # this is for when they havent typed in any info from the if

        except ValueError:
            messagebox.showerror("Error", "Please make sure a class or name has been chosen.")

    #----------------------------building buttons-------------------------------

    #buttons for switching gender & label
    chosegender_lab = tk.Label(window, text="Chose Your Gender", font = ("Ariel", 16, "bold"), fg="black", bg="purple") #window i what adding the label to
    chosegender_lab.place(relx=0.76, rely=0.78, anchor="w")

    fgender_btn = tk.Button(window, text="Female", bg="#00A8FF", font=("Ariel", 14, "bold"), command=femalegender, bd=2, width=10, height=2)
    fgender_btn.place(relx=0.73, rely=0.86, anchor="w")

    Mgender_btn = tk.Button(window, text="Male", bg="#00A8FF", font=("Ariel", 14, "bold"), command=malegender, bd=2, width=10, height=2)
    Mgender_btn.place(relx=0.85, rely=0.86, anchor="w")

    #create char button
    createcharacter_btn = tk.Button(window, text="Create Character", bg="#00A8FF", font=("Ariel", 16, "bold"), command= activateCharacterCreation, bd=2, width=15, height=2)
    createcharacter_btn.place(relx=0.47, rely=0.9, anchor="center")

    #-----choose character buttons & label-----------------------
    #label for chosing class
    choseyourclass_lab = tk.Label(window, text="Chose Your Class", font = ("Ariel", 16, "bold"), fg="black", bg="purple")
    choseyourclass_lab.place(relx=0.11, rely=0.4, anchor="center")

    #Create a frame specifically for the left-side grid
    left_panel = tk.Frame(window, bg="purple")
    left_panel.place(relx=0.073, rely=0.55, anchor="w") # "w" anchors it to the West/Left side

    #-----info label that will show information about the class when clicked-----
    global info_labtxt #named outside def so can change the info in the label below
        #setting the txt lbl to stringvar
    info_labtxt = tk.StringVar() #making it a stringvar otherwise cant update the information of whats shown in the labe;
    info_labtxt.set("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n") #this is updating the information - was here for testing, can remove it

    #class info txt thats atop of the information in the info lab - had to make 2 labels do to issues with imges
    classinfotxt_lab = tk.Label(window, text=f"Class Info\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", font = ("Ariel", 18, "bold"), fg="black", bg="purple", height=18, width=23)
    classinfotxt_lab.place(relx=0.815, rely=0.4, anchor="center")

    #label that holds the class info
    info_lab = tk.Label(window, textvariable=f"{info_labtxt}", font = ("Ariel", 12, "bold"), wraplength=300, fg="black", bg="purple", height=22, width=30) #textvariable links it , wrap length keeps the text inside the label
    info_lab.place(relx=0.815, rely=0.41, anchor="center")

    #Load character icons for class buttons
    warrior_icon = tk.PhotoImage(file="m_warrioricon.png")
    mage_icon = tk.PhotoImage(file="m_mageicon.png")
    healer_icon = tk.PhotoImage(file="m_healericon.png")

    #labels to hold class imgs & header
    previewheader_lab= tk.Label(window, text="Class Preview\n\n\n\n\n\n\n\n\n\n\n\n\n\n", image=None, compound="top", font = ("Ariel", 18, "bold"), fg="black", bg="purple", height=17, width=30) #compount top basically makes everything stack on top of each other and whatever goes first is at top
    previewheader_lab.place(relx=0.46, rely=0.41, anchor="center") # "w" anchors it to the West/Left side

    classimgs_lab= tk.Label(window, image=None, bg="purple")
    classimgs_lab.place(relx=0.46, rely=0.41, anchor="center") # "w" anchors it to the West/Left side

    #configfor when the warrior button is selected

    def selected_warrior():
        global character_selected
        global info_labtxt
        global gender
        character_selected = "Warrior"

        #switches the label text
        info_labtxt.set("The Warrior is a class focused on delivering high physical damage. Unlike the mage class, it doesn't rely all on mp to cast spells. While highly durable, they have no built-in healing abilities. As they do not rely on mp they have little protecting against magical attacks.\n\n Bonuses: Base damage is multiplied by 1.5 \n\n\n\n Difficulty: Low\n\n *Make sure to click a class and type a name before you hit the create character button or you will get an error.")

        if gender == "Female":
            #switches the preview img for warrior
            f_warriorimg = tk.PhotoImage(file="f_warrior.png")
            classimgs_lab.config(image=f_warriorimg)
            classimgs_lab.image = f_warriorimg

        else:
            #switches the preview img
            m_warriorimg = tk.PhotoImage(file="m_warrior.png")
            classimgs_lab.config(
                image=m_warriorimg
            )
            classimgs_lab.image = m_warriorimg

        window.update()

    def selected_mage():
        global character_selected
        global gender
        global info_labtxt

        #switches the label text
        character_selected = "Mage"

        info_labtxt.set("The Mage is a class focused on delivering explosive magical damage from a distance. Unlike physical classes, it relies heavily on a large mp pool to cast its powerful destructive spells. While they possess incredible offensive capabilities, they have a very low health pool and weak physical defenses.\n\n Bonuses: Magic damage is increased by half of the magic used.\n\n\n Difficulty: Medium\n\n *Make sure to click a class and type a name before you hit the create character button or you will get an error.")

        if gender == "Female":
            #switches the preview img for mage
            f_mageimg = tk.PhotoImage(file="f_mage.png")
            classimgs_lab.config(image=f_mageimg)
            classimgs_lab.image = f_mageimg
        
        else:
            #switches the preview img
            m_mageimg = tk.PhotoImage(file="m_mage.png")
            classimgs_lab.config(
                image=m_mageimg
            )
            classimgs_lab.image = m_mageimg

        window.update()

    def selected_healer():
        global character_selected
        global gender
        global info_labtxt
        character_selected = "Healer"

        #switches the label text
        info_labtxt.set("The Healer is a class focused on self heals and deals low damage for long term fights. It relies on a steady use of mp to cast restorative spells and protective barriers during combat. While they can constantly recover from damage, they possess very low physical and magical damage output but can do a 1 time burst damage with the cost of half their life and all their mp.\n\n Bonuses: Each spell has better  individual bonuses than other classes.\n\n\n Difficulty:  high\n\n *Make sure to click a class and type a name before you hit the create character button or you will get an error.")

        if gender == "Female":
            #switches the preview img for healer
            f_healerimg = tk.PhotoImage(file="f_healer.png")
            classimgs_lab.config(image=f_healerimg)
            classimgs_lab.image = f_healerimg

        else:
            #switches the preview img
            m_healerimg = tk.PhotoImage(file="m_healer.png")
            classimgs_lab.config(
                text="Class Preview", 
                image=m_healerimg
            )
            classimgs_lab.image = m_healerimg

        window.update()
     
    # Choose Class Buttons 
    # --- WARRIOR BUTTON ---
    warrior_btn = tk.Button(
        left_panel, image=warrior_icon, # Replace with your actual warrior image variable
        text="Warrior", compound="top", width=37, height=50, command=selected_warrior  
    )
    warrior_btn.grid(row=0, column=0, padx=5, pady=5)
    warrior_btn.image = warrior_icon # Keeps image from turning white

    # --- MAGE BUTTON ---
    mage_btn = tk.Button(
        left_panel, image=mage_icon,        # Replace with your actual mage image variable
        text="Mage", compound="top", width=37, height=50, command=selected_mage   
    )
    mage_btn.grid(row=0, column=1, padx=5, pady=5)
    mage_btn.image = mage_icon

    # --- HEALER BUTTON ---
    healer_btn = tk.Button(
        left_panel, 
        image=healer_icon,      # Replace with your actual healer image variable
        text="Healer", 
        compound="top", 
        width=37, 
        height=50,
        command=selected_healer  
    )
    healer_btn.grid(row=1, column=0, padx=5, pady=5)
    healer_btn.image = healer_icon

def mainscreen():
    global monstername # for the label that shows monster name
    global name # for name label
    global character_selected
    global gender
    global difficulty
    global numOfFights

          #replace background img 
    mainscreenimg = tk.PhotoImage(file="mainscreen.png")
    mainscreenimg_lab = tk.Label(window, image=mainscreenimg)
    mainscreenimg_lab.place(x=0, y=0, relwidth=1, relheight=1) # relwidth/height=1 stretches it 100%
        #without this it wouldnt load for some reason - directly saving the whole bg 
    mainscreenimg_lab.image = mainscreenimg 

    #---------------character------------------

    #label for character name
    namelabel_text = tk.StringVar()
    namelabel_text.set(f"{name} Lv. {currentlvl}")

    name_lab= tk.Label(window, textvariable=namelabel_text, font = ("Ariel", 18, "bold"), fg="black", bg="purple") #compount top basically makes everything stack on top of each other and whatever goes first is at top
    name_lab.place(relx=0.25, rely=0.31, anchor="center") # "w" anchors it to the West/Left side

    #picturetheir char - will need to use if to determine which char is shown

    classimgs_lab= tk.Label(window, image=None, bg="purple")
    classimgs_lab.place(relx=0.25, rely=0.55, anchor="center") # "w" anchors it to the West/Left side    

    #switches classimg label to f/m  warrior
    if character_selected == "Warrior":

        if gender == "Female":
            #switches the preview img for warrior
            f_warriorimg = tk.PhotoImage(file="f_warrior.png")
            classimgs_lab.config(image=f_warriorimg)
            classimgs_lab.image = f_warriorimg

        else:
            #switches the preview img
            m_warriorimg = tk.PhotoImage(file="m_warrior.png")
            classimgs_lab.config(
                image=m_warriorimg
            )
            classimgs_lab.image = m_warriorimg

        window.update()

    elif character_selected == "Mage":

        if gender == "Female":
            #switches the preview img for mage
            f_mageimg = tk.PhotoImage(file="f_mage.png")
            classimgs_lab.config(image=f_mageimg)
            classimgs_lab.image = f_mageimg
        
        else:
            #switches the preview img
            m_mageimg = tk.PhotoImage(file="m_mage.png")
            classimgs_lab.config(
                image=m_mageimg
            )
            classimgs_lab.image = m_mageimg

        window.update()

    elif character_selected == "Healer":

        if gender == "Female":
            #switches the preview img for healer
            f_healerimg = tk.PhotoImage(file="f_healer.png")
            classimgs_lab.config(image=f_healerimg)
            classimgs_lab.image = f_healerimg

        else: #switches the preview img
            m_healerimg = tk.PhotoImage(file="m_healer.png")
            classimgs_lab.config(image=m_healerimg)
            classimgs_lab.image = m_healerimg
        window.update()
    
    #for the stats button - 
    def statsWindow():
        global character_selected
        global currentlvl
        global hp
        global physical_defence
        global magical_defence
        global mp
        global name
        global basedmg

                #Create Stats window Window
        statswindow = tk.Tk()
        statswindow.title("Stats Window")
        statswindow.geometry ("600x700")
        statswindow.configure(bg="black")
        statswindow.resizable(False, False)

        #title
        title = tk.Label(statswindow, text="Stats Window", fg="white", bg="black", font=("Courier", 30, "bold"))
        title.place(relx=0.5, rely=0.15, anchor="center")

        #---------------------------------stats to show - going to be in a grid---------------------------------
        #holds lvl, name, and exp needed
        lvl_label = tk.Label(statswindow, text=f"Name: {name} Lv. {currentlvl} EXP: {currentexp} / {expneeded}", fg="white", bg="black", font=("Courier", 16, "bold"))
        lvl_label.place(relx=0.5, rely=0.3, anchor="center")

        #divider
        divider = tk.Frame(statswindow, height=2, bg="white", bd=0)
        divider.place(relx=0.0, relwidth=1.0, rely=0.325)

        #panel stats will go on
        stats_panel = tk.Frame(statswindow, bg="black")
        stats_panel.place(relx=0.5, rely=0.72, anchor="center")
 
        #hp label
        hp_label = tk.Label(stats_panel, text=f"HP: {hp}", fg="white", bg="black", font=("Courier", 14, "bold"))
        hp_label.grid(row=0, column=0, padx=5, pady=5)

        #mp label
        mp_label = tk.Label(stats_panel, text=f"MP: {mp}", fg="white", bg="black", font=("Courier", 14, "bold"))
        mp_label.grid(row=1, column=0, padx=5, pady=5)

        #basedmg label
        basedmg_label = tk.Label(stats_panel, text=f"Base Damage: {basedmg}", fg="white", bg="black", font=("Courier", 14, "bold"))
        basedmg_label.grid(row=2, column=0, padx=5, pady=5)

        # physical defence label
        physical_defence_label = tk.Label(stats_panel, text=f"Physical Defence: {physical_defence}", fg="white", bg="black", font=("Courier", 14, "bold"))
        physical_defence_label.grid(row=3, column=0, padx=5, pady=5)

        #magical defence label
        magical_defence_label = tk.Label(stats_panel, text=f"Magical Defence: {magical_defence}", fg="white", bg="black", font=("Courier", 14, "bold"))
        magical_defence_label.grid(row=4, column=0, padx=5, pady=5)

        #Run window
        window.mainloop()

    #for the spells button - not done with this- need to add spells
    def spellsWindow():
        global healerspells
        global magespells
        global warriorspells
        global character_selected

                        #Create Stats window Window
        spellswindow = tk.Tk()
        spellswindow.title("Spells Window")
        spellswindow.geometry ("1300x750")
        spellswindow.configure(bg="black")
        spellswindow.resizable(False, False)

        #title
        title = tk.Label(spellswindow, text="Spells Window", fg="white", bg="black", font=("Courier", 30, "bold"))
        title.place(relx=0.5, rely=0.13, anchor="center")

        #divider
        divider = tk.Frame(spellswindow, height=2, bg="white", bd=0)
        divider.place(relx=0.0, relwidth=1.0, rely=0.2)

        #panel for spells
        spells_panel = tk.Frame(spellswindow, bg="white")
        spells_panel.place(relx=0.5, rely=0.55, anchor="center")

            #---------create spell labels-------    - need to change variable names

        if character_selected == "Warrior":

                #spell 0
            bassicattack_label = tk.Label(spells_panel, text=f"\t\t{warriorspells[0]['Name']}\n" 
                                    f"MP Cost: {warriorspells[0]['MP Cost']}\n\n"
                                    f"Damage: {warriorspells[0]['Damage']}\n\n"
                                    f"Description: {warriorspells[0]['Description']}", fg="white", bg="black", font=("Courier", 12, "bold"), wraplength=500, justify="left", anchor="w")
            bassicattack_label.grid(row=0, column=0, padx=5, pady=5)

            #spell 1
            strike_label = tk.Label(spells_panel, text=f"\t\t{warriorspells[1]['Name']}\n" 
                                    f"MP Cost: {warriorspells[1]['MP Cost']}\n\n"
                                    f"Damage: {warriorspells[1]['Damage']}\n\n"
                                    f"Description: {warriorspells[1]['Description']}", fg="white", bg="black", font=("Courier", 12, "bold"), wraplength=500, justify="left", anchor="w")
            strike_label.grid(row=1, column=0, padx=5, pady=5)

            #spell 2
            swordsmanship_label = tk.Label(spells_panel, text=f"\t\t{warriorspells[2]['Name']}\n" 
                                    f"MP Cost: {warriorspells[2]['MP Cost']}\n\n"
                                    f"Damage: {warriorspells[2]['Damage']}\n\n"
                                    f"Description: {warriorspells[2]['Description']}", fg="white", bg="black", font=("Courier", 12, "bold"), wraplength=500, justify="left", anchor="w")
            swordsmanship_label.grid(row=2, column=0, padx=5, pady=5)

            #spell 3
            warriorssword_label = tk.Label(spells_panel, text=f"\t\t{warriorspells[3]['Name']}\n" 
                                    f"MP Cost: {warriorspells[3]['MP Cost']}\n\n"
                                    f"Damage: {warriorspells[3]['Damage']}\n\n"
                                    f"Description: {warriorspells[3]['Description']}", fg="white", bg="black", font=("Courier", 12, "bold"), wraplength=500, justify="left", anchor="w")
            warriorssword_label.grid(row=0, column=1, padx=5, pady=5)

            #spell 4
            advanceshield_label = tk.Label(spells_panel, text=f"\t\t{warriorspells[4]['Name']}\n" 
                                    f"MP Cost: {warriorspells[4]['MP Cost']}\n\n"
                                    f"Damage: {warriorspells[4]['Damage']}\n\n"
                                    f"Description: {warriorspells[4]['Description']}", fg="white", bg="black", font=("Courier", 12, "bold"), wraplength=500, justify="left", anchor="w")
            advanceshield_label.grid(row=1, column=1, padx=5, pady=5)
            
        elif character_selected == "Mage":

                #spell 0
            staffattack_label = tk.Label(spells_panel, text=f"\t\t{magespells[0]['Name']}\n" 
                                    f"MP Cost: {magespells[0]['MP Cost']}\n\n"
                                    f"Damage: {magespells[0]['Damage']}\n\n"
                                    f"Description: {magespells[0]['Description']}", fg="white", bg="black", font=("Courier", 12, "bold"), wraplength=500, justify="left", anchor="w")
            staffattack_label.grid(row=0, column=0, padx=5, pady=5)

            #spell 1
            strike_label = tk.Label(spells_panel, text=f"\t\t{magespells[1]['Name']}\n" 
                                    f"MP Cost: {magespells[1]['MP Cost']}\n\n"
                                    f"Damage: {magespells[1]['Damage']}\n\n"
                                    f"Description: {magespells[1]['Description']}", fg="white", bg="black", font=("Courier", 12, "bold"), wraplength=500, justify="left", anchor="w")
            strike_label.grid(row=1, column=0, padx=5, pady=5)

            #spell 2
            swordsmanship_label = tk.Label(spells_panel, text=f"\t\t{magespells[2]['Name']}\n" 
                                    f"MP Cost: {magespells[2]['MP Cost']}\n\n"
                                    f"Damage: {magespells[2]['Damage']}\n\n"
                                    f"Description: {magespells[2]['Description']}", fg="white", bg="black", font=("Courier", 12, "bold"), wraplength=500, justify="left", anchor="w")
            swordsmanship_label.grid(row=2, column=0, padx=5, pady=5)

            #spell 3
            warriorssword_label = tk.Label(spells_panel, text=f"\t\t{magespells[3]['Name']}\n" 
                                    f"MP Cost: {magespells[3]['MP Cost']}\n\n"
                                    f"Damage: {magespells[3]['Damage']}\n\n"
                                    f"Description: {magespells[3]['Description']}", fg="white", bg="black", font=("Courier", 12, "bold"), wraplength=500, justify="left", anchor="w")
            warriorssword_label.grid(row=0, column=1, padx=5, pady=5)

            #spell 4
            advanceshield_label = tk.Label(spells_panel, text=f"\t\t{magespells[4]['Name']}\n" 
                                    f"MP Cost: {magespells[4]['MP Cost']}\n\n"
                                    f"Damage: {magespells[4]['Damage']}\n\n"
                                    f"Description: {magespells[4]['Description']}", fg="white", bg="black", font=("Courier", 12, "bold"), wraplength=500, justify="left", anchor="w")
            advanceshield_label.grid(row=1, column=1, padx=5, pady=5)
            
        elif character_selected == "Healer":

                #spell 0
            bassicattack_label = tk.Label(spells_panel, text=f"\t\t{healerspells[0]['Name']}\n" 
                                    f"MP Cost: {healerspells[0]['MP Cost']}\n\n"
                                    f"Damage: {healerspells[0]['Damage']}\n\n"
                                    f"Description: {healerspells[0]['Description']}", fg="white", bg="black", font=("Courier", 12, "bold"), wraplength=500, justify="left", anchor="w")
            bassicattack_label.grid(row=0, column=0, padx=5, pady=5)

            #spell 1
            strike_label = tk.Label(spells_panel, text=f"\t\t{healerspells[1]['Name']}\n" 
                                    f"MP Cost: {healerspells[1]['MP Cost']}\n\n"
                                    f"Damage: {healerspells[1]['Damage']}\n\n"
                                    f"Description: {healerspells[1]['Description']}", fg="white", bg="black", font=("Courier", 12, "bold"), wraplength=500, justify="left", anchor="w")
            strike_label.grid(row=1, column=0, padx=5, pady=5)

            #spell 2
            swordsmanship_label = tk.Label(spells_panel, text=f"\t\t{healerspells[2]['Name']}\n" 
                                    f"MP Cost: {healerspells[2]['MP Cost']}\n\n"
                                    f"Damage: {healerspells[2]['Damage']}\n\n"
                                    f"Description: {healerspells[2]['Description']}", fg="white", bg="black", font=("Courier", 12, "bold"), wraplength=500, justify="left", anchor="w")
            swordsmanship_label.grid(row=2, column=0, padx=5, pady=5)

            #spell 3
            warriorssword_label = tk.Label(spells_panel, text=f"\t\t{healerspells[3]['Name']}\n" 
                                    f"MP Cost: {healerspells[3]['MP Cost']}\n\n"
                                    f"Damage: {healerspells[3]['Damage']}\n\n"
                                    f"Description: {healerspells[3]['Description']}", fg="white", bg="black", font=("Courier", 12, "bold"), wraplength=500, justify="left", anchor="w")
            warriorssword_label.grid(row=0, column=1, padx=5, pady=5)

            #spell 4
            advanceshield_label = tk.Label(spells_panel, text=f"\t\t{healerspells[4]['Name']}\n" 
                                    f"MP Cost: {healerspells[4]['MP Cost']}\n\n"
                                    f"Damage: {healerspells[4]['Damage']}\n\n"
                                    f"Description: {healerspells[4]['Description']}", fg="white", bg="black", font=("Courier", 12, "bold"), wraplength=500, justify="left", anchor="w")
            advanceshield_label.grid(row=1, column=1, padx=5, pady=5)

    #def spellWindow(): #spells window pops up to show spells
    spells_but = tk.Button(window, text="Spells", bg="#00A8FF", font=("Ariel", 16, "bold"), command=spellsWindow, bd=2)
    spells_but.place(relx=0.21, rely=0.86, anchor="center")

    #button that pops up for  for stats and lvl 
    stats_but = tk.Button(window, text="Stats", bg="#00A8FF", font=("Ariel", 16, "bold"), command=statsWindow, bd=2)
    stats_but.place(relx=0.28, rely=0.86, anchor="center")

    #----------------------monster----------------

        #label for monster name 
    namelabel_text = tk.StringVar()
    namelabel_text.set(f"{monstername} Lv. {currentlvl}")

    name_lab = tk.Label(window, textvariable=namelabel_text, font = ("Ariel", 18, "bold"), fg="black", bg="purple") #compount top basically makes everything stack on top of each other and whatever goes first is at top
    name_lab.place(relx=0.75, rely=0.2, anchor="center") # "w" anchors it to the West/Left side

    #picture of monster - will need to use if to determine which char is shown
    monsterimgs_lab= tk.Label(window, image=None, bg="purple")
    monsterimgs_lab.place(relx=0.75, rely=0.5, anchor="center") # "w" anchors it to the West/Left side 

            #for chosing monster img
    if monstername == "Hierophant":

        monsterimg = tk.PhotoImage(file="Hierophant.png")
        monsterimgs_lab.config(image=monsterimg)
        monsterimgs_lab.image = monsterimg

    elif monstername == "Goylca":

        monsterimg = tk.PhotoImage(file="Goylca.png")
        monsterimgs_lab.config(image=monsterimg)
        monsterimgs_lab.image = monsterimg
        
    elif monstername == "Krosmo Crusher":

        monsterimg = tk.PhotoImage(file="Krosmo Crusher.png")
        monsterimgs_lab.config(image=monsterimg)
        monsterimgs_lab.image = monsterimg

    elif monstername == "Bulmar":

        monsterimg = tk.PhotoImage(file="Bulmar.png")
        monsterimgs_lab.config(image=monsterimg)
        monsterimgs_lab.image = monsterimg

    #difficulty dropdown
    difficulty = tk.StringVar() #call difficulty to figure out what was chosen
    difficulty.set("Normal") #this is what will always appear first
    difficulty_options = ["Easy", "Normal", "Hard", "Difficult"] #dropdown options

    #dropdown widget
    # Syntax: OptionMenu(parent, stringvar, *list_of_options)
    dropdown = ttk.Combobox(window, textvariable=difficulty, values=difficulty_options, font=("Courier", 14, "bold"))
    dropdown.place(relx=0.75, rely=0.8, anchor="center")

    #announce level ups after battle with an if/else
    if lvlupnotification == "You Have Leveled Up!":
            # The Pop-up box code
        messagebox.showinfo(f"{lvlupnotification}\n Your current level is LV.{currentlvl}!")
    elif fightWon == False and numOfFights > 0:
        messagebox.showinfo(f"You have lost\n Your current level is LV.{currentlvl}!")

    def startfight():
        global fightstatus

        try:
            if difficulty != "":
                dropdown.destroy()
                name_lab.destroy()
                monsterimgs_lab.destroy()
                stats_but.destroy()
                spells_but.destroy()
                classimgs_lab.destroy()
                mainscreenimg_lab.destroy()
                startfight_but.destroy()

                fightstatus = "Fight Started"

                window.update_idletasks() 

                loadingpage()
            else: 
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Please make sure a difficulty was chosen.")
    
    #button that pops up for  for stats and lvl 
    startfight_but = tk.Button(window, text="Start Fight", bg="#00A8FF", font=("Ariel", 16, "bold"), command=startfight, bd=2)
    startfight_but.place(relx=0.5, rely=0.47, anchor="center")

def fightscreen():
    global difficulty
    global monstername
    global magespells, healerspells, warriorspells
    global character_selected
    global currentlvl
    global name
    global monsters
    global hp
    global mp
    global basedmg
    global currentexp
    global pastlvl
    global expneeded
    global fightstatus
    global timer
    global physical_defence, magical_defence #used when monster is attacking player
    global pressedEndFight
    global fightHpandMpset

    #this because of end fight button sends back to fight screen
    if pressedEndFight == False:

        difficulty_choice = difficulty.get()
        timer = 60 #reassigning because without on 2nd fight will be messed up
        timerExists = False #used to check if the timer exists or not - if it does then it will be destroyed and a new one will be created
        oneSecondCountdown = None #used for the timer variable in countdown
        pressedEndTurn = False # this is to properly destroy countdown timer if player presses end turn button instead of waiting for the timer to run out - if this is true then the timer will be destroyed and a new one will be created

        # anything added to these debuffs/buffs must follow a form of - EX: "State":" "Player Debuff", "Name": "Damage Debuff", "Turns(how long it lasts- dont include this paraenthesis)": 2, "Effect": "blah blah blah", "Value": 0.40 - the value is only thing used for calculation - anything that only adds values without any turn cooldown should not be added
        #states are the array name without the s on the end
        #states are for the for loop because im putting multiple lists in the loop so need an if statement to differenciate between them.
        #for -% its always totaldmg * (1 - debuff) #debuff should always be a decimal, ex .40 , thi is effectively 100% - 40%- or you can do totaldmg *= 0.60
        player_buffs = []   
        player_debuffs = []   
        monster_buffs = []  
        monster_debuffs = [] 

        #used for calculations in fight to exit loop and also display variables - used so they dont change the innitial variables - will cause a bug and game may crash because if remove the if makes a infinite loop
        if fightHpandMpset == False:
            fighthp = hp
            #mhp is made inside  - monster hp
            fightmp = mp
            #mmp is made inside - monster mp

            #shield is used the same as hp but it doesnt kill u if it reaces 0, its used in place of hp.
            playershield = 0
            monstershield = 0

    #------------set background-----------
    #mob fight background
    if monstername == "Bulmar" or "Goylca" or "Hierophant":

        fightscreenimg = tk.PhotoImage(file="mobfightbg.png")
        fightscreenimg_lab = tk.Label(window, image=fightscreenimg)
        fightscreenimg_lab.place(x=0, y=0, relwidth=1, relheight=1) # relwidth/height=1 stretches it 100%
            #without this it wouldnt load for some reason - directly saving the whole bg 
        fightscreenimg_lab.image = fightscreenimg 

    #boss fight background
    elif monstername == "Krosmo Crusher":

        fightscreenimg = tk.PhotoImage(file="bossfightbg.png")
        fightscreenimg_lab = tk.Label(window, image=fightscreenimg)
        fightscreenimg_lab.place(x=0, y=0, relwidth=1, relheight=1) # relwidth/height=1 stretches it 100%
        #without this it wouldnt load for some reason - directly saving the whole bg 
        fightscreenimg_lab.image = fightscreenimg 

    try: 
        #-----------create character img & label/hp/mp label-------------
        #label for character name
        namelabel_text = tk.StringVar()
        namelabel_text.set(f"{name} Lv. {currentlvl}")

        name_lab= tk.Label(window, textvariable=namelabel_text, font = ("Ariel", 18, "bold"), fg="black", bg="purple") #compount top basically makes everything stack on top of each other and whatever goes first is at top
        name_lab.place(relx=0.21, rely=0.31, anchor="center") # "w" anchors it to the West/Left side

        characterimgs_lab= tk.Label(window, image=None, bg="purple")
        characterimgs_lab.place(relx=0.21, rely=0.55, anchor="center") # "w" anchors it to the West/Left side  

        #label for mp
        fightmp_text = tk.StringVar()
        fightmp_text.set(f"MP: {fightmp}")

        fightmp_lab= tk.Label(window, textvariable=fightmp_text, font = ("Ariel", 18, "bold"), fg="black", bg="purple") #compount top basically makes everything stack on top of each other and whatever goes first is at top
        fightmp_lab.place(relx=0.21, rely=0.75, anchor="center") # "w" anchors it to the West/Left side
        #character image
        if character_selected == "Warrior":

            if gender == "Female":
                #switches the preview img for warrior
                f_warriorimg = tk.PhotoImage(file="f_warrior.png")
                characterimgs_lab.config(image=f_warriorimg)
                characterimgs_lab.image = f_warriorimg

            else:
                #switches the preview img
                m_warriorimg = tk.PhotoImage(file="m_warrior.png")
                characterimgs_lab.config(
                    image=m_warriorimg
                )
                characterimgs_lab.image = m_warriorimg

            window.update()

        elif character_selected == "Mage":

            if gender == "Female":
                #switches the preview img for mage
                f_mageimg = tk.PhotoImage(file="f_mage.png")
                characterimgs_lab.config(image=f_mageimg)
                characterimgs_lab.image = f_mageimg
            
            else:
                #switches the preview img
                m_mageimg = tk.PhotoImage(file="m_mage.png")
                characterimgs_lab.config(
                    image=m_mageimg
                )
                characterimgs_lab.image = m_mageimg

            window.update()

        elif character_selected == "Healer":

            if gender == "Female":
                #switches the preview img for healer
                f_healerimg = tk.PhotoImage(file="f_healer.png")
                characterimgs_lab.config(image=f_healerimg)
                characterimgs_lab.image = f_healerimg

            else: #switches the preview img
                m_healerimg = tk.PhotoImage(file="m_healer.png")
                characterimgs_lab.config(image=m_healerimg)
                characterimgs_lab.image = m_healerimg

                window.update()
        
        #----------------------set monster img/stats/experience gained from that monster/ hp label----------------
        
        #difficulty stat diffrentiator(just have to multiple this with the chosen stat) + the experience ammount will get after fight + the lvl that will be displayed

        baseexpgained = 30 * (1.20 ** (currentlvl - 1)) #grows by 20% each level

        if difficulty_choice == "Easy":
            difficulty_multiplier = 0.50
            monsterlvl = currentlvl/2

        elif difficulty_choice == "Normal":
            difficulty_multiplier = 1 #doesn't increase stats or decrease
            monsterlvl = currentlvl

        elif difficulty_choice == "Hard":
            difficulty_multiplier = 1.25
            monsterlvl = currentlvl*1.25

        elif difficulty_choice == "Difficult":
            difficulty_multiplier = 1.50
            monsterlvl = currentlvl/2 + currentlvl

        #label for monster name 
        mnamelabel_text = tk.StringVar()
        mnamelabel_text.set(f"{monstername} Lv. {monsterlvl}")

        mname_lab = tk.Label(window, textvariable=mnamelabel_text, font = ("Ariel", 18, "bold"), fg="black", bg="purple") #compount top basically makes everything stack on top of each other and whatever goes first is at top
        mname_lab.place(relx=0.8, rely=0.2, anchor="center")

        #label for the monster img
        monster_imgs_lab= tk.Label(window, image=None, bg="purple")
        monster_imgs_lab.place(relx=0.8, rely=0.5, anchor="center")  
    
        #monster imgs and stats, assigned new temporary variables so that the main value doesnt change and only the values inside the fight will change

        if fightHpandMpset == False: # here so when this screen is called again it doesnt reset monster hp

            if monstername == "Hierophant":

                monster_img = tk.PhotoImage(file="Hierophant.png")
                monster_imgs_lab.config(image=monster_img)
                monster_imgs_lab.image = monster_img

                #stats
                mhp = monsters[3]["hp"]*difficulty_multiplier
                mmp = monsters[3]["mp"]*difficulty_multiplier
                mphysical_defence = monsters[3]["physical_defence"] *difficulty_multiplier
                mmagical_defence = monsters[3]["magical_defence"] *difficulty_multiplier
                mphysical_dmg = monsters[3]["physical_dmg"] *difficulty_multiplier
                mmagical_dmg = monsters[3]["magical_dmg"] *difficulty_multiplier

            elif monstername == "Goylca":

                monster_img = tk.PhotoImage(file="Goylca.png")
                monster_imgs_lab.config(image=monster_img)
                monster_imgs_lab.image = monster_img

                mhp = monsters[0]["hp"]*difficulty_multiplier
                mmp = monsters[0]["mp"]*difficulty_multiplier
                mphysical_defence = monsters[0]["physical_defence"] *difficulty_multiplier
                mmagical_defence = monsters[0]["magical_defence"] *difficulty_multiplier
                mphysical_dmg = monsters[0]["physical_dmg"] *difficulty_multiplier
                mmagical_dmg = monsters[0]["magical_dmg"] *difficulty_multiplier
                
            elif monstername == "Krosmo Crusher":

                monster_img = tk.PhotoImage(file="Krosmo Crusher.png")
                monster_imgs_lab.config(image=monster_img)
                monster_imgs_lab.image = monster_img

                mhp = monsters[2]["hp"] *difficulty_multiplier
                mmp = monsters[2]["mp"]*difficulty_multiplier
                mphysical_defence = monsters[2]["physical_defence"] *difficulty_multiplier
                mmagical_defence = monsters[2]["magical_defence"] *difficulty_multiplier
                mphysical_dmg = monsters[2]["physical_dmg"] *difficulty_multiplier
                mmagical_dmg = monsters[2]["magical_dmg"] *difficulty_multiplier

            elif monstername == "Bulmar":

                monster_img = tk.PhotoImage(file="Bulmar.png")
                monster_imgs_lab.config(image=monster_img)
                monster_imgs_lab.image = monster_img

                mhp = monsters[1]["hp"] *difficulty_multiplier
                mmp = monsters[1]["mp"]*difficulty_multiplier
                mphysical_defence = monsters[1]["physical_defence"] *difficulty_multiplier
                mmagical_defence = monsters[1]["magical_defence"] *difficulty_multiplier
                mphysical_dmg = monsters[1]["physical_dmg"] *difficulty_multiplier
                mmagical_dmg = monsters[1]["magical_dmg"] *difficulty_multiplier

            #this is used for stats window so when i spell is cast that that affects monster mp it changes
            mmp_text = tk.StringVar()
            mmp_text.set(f"{mmp}")

    #----------------------------basic display labels-----------------------------
    
        #label for the character hp
        hplab_text = tk.StringVar()
        hplab_text.set(f"{fighthp}")

        hp_lab= tk.Label(window, textvariable=f"{hplab_text}", font = ("Ariel", 16, "bold"), fg="black", bg="purple")
        hp_lab.place(relx=0.4, rely=0.95, anchor="center")  

        #vs label
        vs_lab= tk.Label(window, text="vs", font = ("Ariel", 16, "bold"), fg="black", bg="purple")
        vs_lab.place(relx=0.5, rely=0.95, anchor="center")  
        
        #label for the monster hp
        mhplab_text = tk.StringVar()
        mhplab_text.set(f"{mhp}")

        mhp_lab= tk.Label(window, textvariable=f"{mhplab_text}", font = ("Ariel", 16, "bold"), fg="black", bg="purple")
        mhp_lab.place(relx=0.6, rely=0.95, anchor="center")  

    except:
        print("Already made")

    try:
        #----------------------------Turn label & img -----------------------------------------------
        #label for turns - should say turn then will make a counter that will update it text=f"Turn", textvariable=
        turn = 1
        turnlab_text = tk.StringVar()
        turnlab_text.set(f"Turn: {turn}")        
        turn_lab= tk.Label(window, textvariable=f"{turnlab_text}", font = ("Ariel", 20, "bold"), fg="black", bg="purple")
        turn_lab.place(relx=0.93, rely=0.85, anchor="center")

        #label for turn icon imgs, - will be for the turn and when its your turn it will config to show img and will keep switching
        yourturnimg_lab = tk.Label(window, img =None, fg="black", bg="purple")
        yourturnimg_lab.place(relx=0.93, rely=0.9, anchor="center")

        #character turn image icon
        if character_selected == "Warrior":

            if gender == "Female":
                #switches the preview img for warrior
                turniconimg = tk.PhotoImage(file="f_warrioricon.png")
                yourturnimg_lab.config(image=turniconimg)
                yourturnimg_lab.image = turniconimg

            else:
                #switches the preview img
                turniconimg = tk.PhotoImage(file="m_warrioricon.png")
                yourturnimg_lab.config(image=turniconimg)
                yourturnimg_lab.image = turniconimg

            window.update()

        elif character_selected == "Mage":

            if gender == "Female":
                #switches the preview img for mage
                turniconimg = tk.PhotoImage(file="f_mageicon.png")
                yourturnimg_lab.config(image=turniconimg)
                yourturnimg_lab.image = turniconimg
            
            else:
                #switches the preview img
                turniconimg = tk.PhotoImage(file="m_mageicon.png")
                yourturnimg_lab.config(image=turniconimg)
                yourturnimg_lab.image = turniconimg

            window.update()

        elif character_selected == "Healer":

            if gender == "Female":
                #switches the preview img for healer
                turniconimg = tk.PhotoImage(file="f_healericon.png")
                yourturnimg_lab.config(image=turniconimg)
                yourturnimg_lab.image = turniconimg

            else: #switches the preview img
                turniconimg = tk.PhotoImage(file="m_healericon.png")
                yourturnimg_lab.config(image=turniconimg)
                yourturnimg_lab.image = turniconimg

            window.update()

    except Exception as e:
        print("Already made turn label and turn img icon or ", e)

    def variablesUpdate(): #used whenever something affects a player's or monsters hp/mp and will also do an hp check to see if anyone died
        #could also incorporate the check if a player dies in here too
        nonlocal fighthp
        nonlocal mhp
        global fightHpandMpset
        nonlocal mmp

        hplab_text.set(f"{fighthp}")
        mhplab_text.set(f"{mhp}")
        fightmp_text.set(f"MP: {fightmp}")
        mmp_text.set(f"{mmp}")

        if fighthp <= 0 or mhp <= 0:
            fightHpandMpset == True # this is set because need this so that the current hp of the monster and fighter dont change when i send it back to fight screen
            fightscreen()

    def end_fight():    #triggers fight experience and then sends to loading page once the fight has ended, lvl calculations will be completed in the loading page, this does decide if won the fight or not and debuffs/exp from the fight
        global fightstatus
        global difficulty_choice
        global timer
        global currentexp
        global currentlvl
        global currentexp
        nonlocal fighthp
        nonlocal mhp
        global fightWon
        global numOfFights
        global pressedEndFight
        global fightHpandMpset

        #-------------exp calculations ------------- 
        def lvl_exp_decrease():
            #lvl and exp decrease
            currentlvl - 1
            pastlvl - 1
            currentexp - baseexpgained*difficulty_multiplier
            currentexp =  expneeded + currentexp

            #stats dec
            hp/1.5
            magical_defence/1.5
            physical_defence/1.5
            basedmg/1.5     

        if fighthp > 0 and mhp <= 0:
            fightWon = True
            currentexp = currentexp + (baseexpgained*difficulty_multiplier)

        elif mhp > 0 and fighthp <= 0:
            fightWon = False
            lvl_exp_decrease

        elif fighthp <= 0 and mhp <=0:
            fightWon = False #technically a draw  but its not a win so false - later on could rework mechanics so that they could get like half of what they would have gained
            lvl_exp_decrease

        pressedEndFight = True

        numOfFights += 1
        fightstatus = "Fight Ended"
        difficulty_choice = None

        #in fight screen when press end fight it should send to fight screen, then fight screen will send it back here and set fightblah to false which will then send us to the loading page properly
        if fightHpandMpset == False: 
            loadingpage() 
        else:
            fightscreen()

    def monsterStatsWindow():    #for the monster stats button - 
        global monstername
        nonlocal mhp
        nonlocal mmp
        nonlocal mphysical_defence
        nonlocal mmagical_defence
        nonlocal mphysical_dmg
        nonlocal mmagical_dmg
        nonlocal monsterlvl

                #Create Stats window Window
        statswindow = tk.Tk()
        statswindow.title("Stats Window")
        statswindow.geometry ("800x700")
        statswindow.configure(bg="black")
        statswindow.resizable(False, False)

        #title
        title = tk.Label(statswindow, text="Stats Window", fg="white", bg="black", font=("Courier", 30, "bold"))
        title.place(relx=0.5, rely=0.15, anchor="center")
        
        #---------------------------------stats to show - going to be in a grid---------------------------------
        #holds lvl, name, and exp needed
        lvl_label = tk.Label(statswindow, text=f"Name: {monstername} Lv. {monsterlvl}", fg="white", bg="black", font=("Courier", 16, "bold"))
        lvl_label.place(relx=0.5, rely=0.3, anchor="center")

        #divider
        divider = tk.Frame(statswindow, height=2, bg="white", bd=0)
        divider.place(relx=0.0, relwidth=1.0, rely=0.325)

        #panel stats will go on
        stats_panel = tk.Frame(statswindow, bg="black")
        stats_panel.place(relx=0.5, rely=0.72, anchor="center")
 
        #mhp label

        mhp_label = tk.Label(stats_panel, text=f"HP: {mhp}", fg="white", bg="black", font=("Courier", 14, "bold"))
        mhp_label.grid(row=0, column=0, padx=5, pady=5)

        #mmp label
        mmp_label = tk.Label(stats_panel, text=f"MP: {mmp_text}", fg="white", bg="black", font=("Courier", 14, "bold"))
        mmp_label.grid(row=1, column=0, padx=5, pady=5)

        #mphysical dmg label
        mmphysical_dmg_label = tk.Label(stats_panel, text=f"Physical Damage: {mphysical_dmg}", fg="white", bg="black", font=("Courier", 14, "bold"))
        mmphysical_dmg_label.grid(row=2, column=0, padx=5, pady=5)

        #mmagical dmg label
        mmagical_dmg_label = tk.Label(stats_panel, text=f"Physical Damage: {mmagical_dmg}", fg="white", bg="black", font=("Courier", 14, "bold"))
        mmagical_dmg_label.grid(row=3, column=0, padx=5, pady=5)

        # mphysical defence label
        mphysical_defence_label = tk.Label(stats_panel, text=f"Physical Defence: {mphysical_defence}", fg="white", bg="black", font=("Courier", 14, "bold"))
        mphysical_defence_label.grid(row=4, column=0, padx=5, pady=5)

        #mmagical defence label
        mmagical_defence_label = tk.Label(stats_panel, text=f"Magical Defence: {mmagical_defence}", fg="white", bg="black", font=("Courier", 14, "bold"))
        mmagical_defence_label.grid(row=5, column=0, padx=5, pady=5)

                #mmagical defence label
        monster_dmg_infolabel = tk.Label(stats_panel, text="*Total damage is calculated using Magical and Physical Damage instead of Base Damage", fg="white", bg="black", font=("Courier", 14, "bold"),  wraplength=400)
        monster_dmg_infolabel.grid(row=6, column=0, padx=10, pady=10)
        #Run window
        window.mainloop()

    #counts down timer and creates/destroys timer label
    def countdown():
        global timer
        nonlocal timerExists
        nonlocal pressedEndTurn
        nonlocal oneSecondCountdown

        #timer label - fight will have a timer of 60 seconds, can increase if they play fast, timer will start automatically - the number will be changed in the loop
            #the if is for checking if the label already exists so it doesnt create duplicates
        if timerExists == False:
            timerlab_text = tk.StringVar()
            timerlab_text.set(f"{timer}")
            timer_lab= tk.Label(window, textvariable=f"{timerlab_text}", font = ("Ariel", 24, "bold"), fg="black", bg="purple")
            timer_lab.place(relx=0.5, rely=0.1, relwidth=0.1, relheight=0.1, anchor="center")

        if pressedEndTurn == True: #this is to properly destroy countdown timer if player presses end turn button instead of waiting for the timer to run out - if this is true then the timer will be destroyed and a new one will be created
            timer_lab.destroy() #destroys the timer label when it reaches 0
            timerExists = False
            pressedEndTurn = False # this resets the end turn codition for the next turn

        #this is here for end fight procedures - need to destroy timer label
        if fighthp <= 0 or mhp <= 0:
            if timerExists == True:
                timer_lab.destroy() #destroys the timer label when it reaches 0
                timerExists = False
            end_fight() #makes it complete end fight procedures.

        #this is here because if press end turn too fast it can cause the .after to repeat making countdown trigger multiple times   + also found making coutndown restart to lower timer count     
        if timer >= 0:
            timer -= 1
            oneSecondCountdown = window.after(1000, countdown) #this repeats the countdown function every 1 second so can make it count down

        else: 
            timer_lab.destroy() #destroys the timer label when it reaches 0
            timerExists = False
            monster_turn() #makes it switch to monster turn when timer reaches 0
        
        window.update()

    #-----------create spell methods and spell buttons & label/panel----------------
    #create button pannel - should be made above the def above
    try: 
        spells_panel = tk.Frame(window, bg="purple", bd=2, width=20, height=2)
        spells_panel.place(relx=0.425, rely=0.8, anchor="center")  

        spellinfo_lab = tk.Label(window, text="", font=("Ariel", 12), fg="black", bg="purple")
        spellinfo_lab.place(relx=0.5, rely=0.78, anchor="center")
    except Exception as e:
        print("already made spell info label and panel or ", e)

    def spellactivation(spell):
        global warriorspells, magespells, healerspells
        global character_selected
        global difficulty
        global character_selected
        global currentlvl
        global name
        global monsters, monstername
        global basedmg
        global currentexp
        global pastlvl
        global expneeded
        global fightstatus
        global timer
        nonlocal mhp, fighthp, fightmp, mmp, mphysical_defence, mmagical_defence
        nonlocal player_buffs, player_debuffs, monster_buffs, monster_debuffs
        nonlocal playershield, monstershield
        nonlocal player_buffs, monster_debuffs, monster_buffs, player_debuffs

        #up here sp the array has the value of mpused
        mpused = spell["Mp Cost"]
        mpdmg = mpused*3 #whenever need to do math with magical dmg only need to assign the valueto   mpused and add mpdmg 
        spelldmg = 0 #its the base spell dmg for every spell
        totaldmg = 0 #the actual dmg that will be dealt

        #this is to decide the monster index so we can call monster's physical/magical defence for any monster 
        if monstername == "Bulmar":
            monster_index = 1
    
        elif monstername == "Goylca":
            monster_index = 0
   
        elif monstername == "Hierophant":
            monster_index = 3
    
        elif monstername == "Krosmo Crusher":
            monster_index = 2

        #---------------this decides the base total dmg in the fight, additional adds on to this dmg will change depending on the spell, mostly here so that this part doesnt repeat in all if's---------------
        #made this a def because in the spells, certain spells/classess can cause additional effects and may need to redo the math below
        def totaldmgcalculations():
            nonlocal totaldmg, spelldmg
            nonlocal mpdmg
            global monsters
            nonlocal fightmp, fighthp
            global currentlvl, basedmg, hp
            nonlocal player_buffs, player_debuffs, monster_buffs, monster_debuffs
            global character_selected

            #this is because each spell have either two types of spell damage depending on if they used mp or not

            if spell["Name"] == "Basic Attack" or spell["Name"] == "Staff Attack" or spell["Name"] == "Wand Attack":
                spelldmg = basedmg*1.5

            elif character_selected == "Warrior": #this is because all of warrior spells uses base dmg while others doesn't + 1.5 bonus multiplier
                spelldmg = (basedmg*1.5)*1.5 + (currentlvl * 1.5)

            else:
                spelldmg = (currentlvl * 1.5)

            if mpused > 0: #checks if the mpused is above 0 for mp dmg
                #for calculating the dmg loss from monster defence
                if monsters[monster_index]["magical_defence"] > 0 and monsters[monster_index]["physical_defence"] > 0:
                    totaldmg = spelldmg + mpdmg - (monsters[monster_index]["magical_defence"] 
                                                    + monsters[monster_index]["physical_defence"])/2

                elif monsters[monster_index]["magical_defence"] > 0:
                    totaldmg = spelldmg + mpdmg - monsters[monster_index]["magical_defence"]/2

                elif monsters[monster_index]["physical_defence"] > 0:
                    totaldmg = spelldmg + mpdmg - monsters[monster_index]["physical_defence"]/2

                else: 
                    totaldmg = spelldmg + mpdmg

            elif mpused == 0: #checks if the mpused is = 0 for no mp dmg
            
                #for calculating the dmg loss from monster defence
                if monsters[monster_index]["magical_defence"] > 0 and monsters[monster_index]["physical_defence"] > 0:
                    totaldmg = spelldmg + -(monsters[monster_index]["magical_defence"] 
                                            + monsters[monster_index]["physical_defence"])/2

                elif monsters[monster_index]["magical_defence"] > 0:
                    totaldmg = spelldmg + -monsters[monster_index]["magical_defence"]/2

                elif monsters[monster_index]["physical_defence"] > 0:
                    totaldmg =  spelldmg + -monsters[monster_index]["physical_defence"]/2

                else: 
                    totaldmg = spelldmg + 0

            elif mpused == "100%": #this is for the spells that use all mp
                mpused = fightmp
                if monsters[monster_index]["magical_defence"] > 0 and monsters[monster_index]["physical_defence"] > 0:
                    totaldmg = spelldmg + mpdmg +  - (monsters[monster_index]["magical_defence"] 
                                                    + monsters[monster_index]["physical_defence"])/2

                elif monsters[monster_index]["magical_defence"] > 0:
                    totaldmg = spelldmg + mpdmg +  - monsters[monster_index]["magical_defence"]/2

                elif monsters[monster_index]["physical_defence"] > 0:
                    totaldmg = spelldmg + mpdmg +  - monsters[monster_index]["physical_defence"]/2

                else: 
                    totaldmg = spelldmg + mpdmg

            for spellEffects in player_debuffs + player_buffs + monster_buffs:
                if spellEffects["State"] == "Player Debuff":
                    if spellEffects["Name"] == "Damage Debuff":
                        totaldmg * (1 - spellEffects["Value"])
                elif spellEffects["State"] == "Player Buff":
                    pass #i dont know what buffs i will have yet
                elif spellEffects["State"] == "Monster Buff":
                    pass #i dont know what buffs i will have yet
                else:
                    break

        #this is just to check to see if have enough mp to even use the spell
        if fightmp < spell["MP Cost"]:
            messagebox.showerror("Error", "You Do Not Have Enough Mp")

        else: 

            #--------------------this calculates actual total dmg and will also do animations in the future
            if spell["MP Cost"] != "100%":
                fightmp -= spell["MP Cost"]

            if character_selected == "Warrior":
                #warrior spell bonus was calculated in totaldmgcalculations()
                totaldmgcalculations()
                
                #holds the spell dmg calculations
                if spell["Name"] == "Basic Attack":
                    
                    if monstershield > 0 and totaldmg > monstershield:
                        totaldmg - monstershield
                        shieldloss = monstershield #shield lost will be used for animations
                        monstershield = 0
                        monsterHpLoss = mhp - totaldmg
                        mhp - totaldmg

                    elif monstershield > 0 and monstershield > totaldmg:
                        shieldloss = totaldmg 
                        monstershield = monstershield - totaldmg
                        
                    elif monstershield == 0:                    
                        monsterHpLoss = mhp - totaldmg
                        mhp - totaldmg

                    fightmp += 2 

                elif spell["Name"] == "Strike":
                    if monstershield > 0 and totaldmg > monstershield:
                        totaldmg - monstershield
                        shieldloss = monstershield #shield lost will be used for animations
                        monstershield = 0
                        monsterHpLoss = mhp - totaldmg
                        mhp - totaldmg

                    elif monstershield > 0 and monstershield > totaldmg:
                        shieldloss = totaldmg 
                        monstershield = monstershield - totaldmg

                    elif monstershield == 0:                    
                        monsterHpLoss = mhp - totaldmg
                        mhp - totaldmg

                    fightmp += 2 
                    
                elif spell["Name"] == "Swordsmanship":
                    if monstershield > 0 and totaldmg > monstershield:
                        totaldmg - monstershield
                        shieldloss = monstershield #shield lost will be used for animations
                        monstershield = 0
                        monsterHpLoss = mhp - totaldmg

                    elif monstershield > 0 and monstershield > totaldmg:
                        shieldloss = totaldmg 
                        monstershield = monstershield - totaldmg

                    elif monstershield == 0:                    
                        monsterHpLoss = mhp - totaldmg

                    fightmp += 2 

                elif spell["Name"] == "Warrior’s Sword":
                    fightmp = 0

                    if monstershield > 0 and totaldmg > monstershield:
                        totaldmg - monstershield
                        shieldloss = monstershield #shield lost will be used for animations
                        monstershield = 0
                        monsterHpLoss = mhp - totaldmg
                        mhp - totaldmg
                        
                    elif monstershield > 0 and monstershield > totaldmg:
                        shieldloss = totaldmg 
                        monstershield = monstershield - totaldmg
                        
                    elif monstershield == 0:                    
                        monsterHpLoss = mhp - totaldmg
                        mhp - totaldmg
    
                    fightmp += 2 

                elif spell["Name"] == "Advance Shield":                
                    if monstershield > 0 and totaldmg > monstershield:
                        totaldmg - monstershield
                        shieldloss = monstershield #shield lost will be used for animations
                        monstershield = 0
                        monsterHpLoss = mhp - totaldmg
                        mhp - totaldmg

                    elif monstershield > 0 and monstershield > totaldmg:
                        shieldloss = totaldmg 
                        monstershield = monstershield - totaldmg
                        
                    elif monstershield == 0:                    
                        monsterHpLoss = mhp - totaldmg
                        mhp - totaldmg
                    
                    fightmp += 2 

                    #this gives shield at random from half of damage dealt to full damage dealt
                    playershield += random.randint(totaldmg/2,totaldmg)
        
            elif character_selected == "Mage":
                mpdmg = (mpused + (spell["MP Cost"]/2))*3
                #holds the spell dmg calculations

                totaldmgcalculations()
                if spell["Name"] == "Staff Attack":
                    if monstershield > 0 and totaldmg > monstershield:
                        totaldmg - monstershield
                        shieldloss = monstershield #shield lost will be used for animations
                        monstershield = 0
                        monsterHpLoss = mhp - totaldmg
                        mhp - totaldmg

                        fightmp += 3 

                    elif monstershield > 0 and monstershield > totaldmg:
                        shieldloss = totaldmg 
                        monstershield = monstershield - totaldmg
                        
                        fightmp += 3 

                    elif monstershield == 0:                    
                        monsterHpLoss = mhp - totaldmg
                        mhp - totaldmg
                        fightmp += 3 
    
                    variablesUpdate()

                elif spell["Name"] == "MP Drain":

                    totaldmg -= (mpused + (spell["MP Cost"]/2))*3#this here because the dmg calculations added more dmg, this spell only supossed to do slight damage
                    if monstershield > 0 and totaldmg > monstershield:
                        totaldmg - monstershield
                        shieldloss = monstershield #will be used for animations
                        monstershield = 0
                        monsterHpLoss = mhp - totaldmg
                        mhp - totaldmg

                        mploss = random.randint(3, 9)
                        mmp - mploss
                        fightmp += mploss 

                    elif monstershield > 0 and monstershield > totaldmg:
                        shieldloss = totaldmg 
                        monstershield = monstershield - totaldmg
                        
                        mploss = random.randint(3, 9)
                        mmp - mploss
                        fightmp += mploss 

                    elif monstershield == 0:                    
                        monsterHpLoss = mhp - totaldmg
                        mhp - totaldmg

                        mploss = random.randint(3, 9)
                        mmp - mploss
                        fightmp += mploss 
    
                elif spell["Name"] == "HP Drain":
                    if monstershield > 0 and totaldmg > monstershield:
                        totaldmg - monstershield
                        shieldloss = monstershield #shield lost will be used for animations
                        monstershield = 0
                        monsterHpLoss = mhp - totaldmg
                        mhp - totaldmg

                        fighthp += monsterHpLoss

                    elif monstershield > 0 and monstershield > totaldmg:
                        shieldloss = totaldmg 
                        monstershield = monstershield - totaldmg
                        fighthp += monsterHpLoss

                    elif monstershield == 0:                    
                        monsterHpLoss = mhp - totaldmg
                        mhp - totaldmg
                        fighthp += monsterHpLoss
    
                elif spell["Name"] == "Magic Explosion":
                    if monstershield > 0 and totaldmg > monstershield:
                        totaldmg - monstershield
                        shieldloss = monstershield #shield lost will be used for animations
                        monstershield = 0
                        monsterHpLoss = mhp - totaldmg
                        mhp - totaldmg

                    elif monstershield > 0 and monstershield > totaldmg:
                        shieldloss = totaldmg 
                        monstershield = monstershield - totaldmg

                    elif monstershield == 0:                    
                        monsterHpLoss = mhp - totaldmg
                        mhp - totaldmg
    
                elif spell["Name"] == "Damage Debuff":
                    monster_debuffs.append({"State": "Monster Debuff", "Name":  "Damage Debuff", "Turns": 2, "Effect": "Reduces Enemy Damage by 40% for two turns", "Value": 0.40})

            elif character_selected == "Healer":
                healingbonus = mpused * (currentlvl*1.5)
                healingspell = False #this is for the def because some spells actually heal while others will have just the healing bonus
                def healingCalculations(): #this def was made because in future spells dont want to always have to do the calculations just for the healing bonus
                                    
                    if healingspell == True:
                        if spell["Name"] == "HP Drain" or spell["Name"] == "Heal":
                            if fighthp < hp:
                                fighthp += healingbonus + totaldmg
                                if fighthp > hp:
                                        fighthp = hp

                            elif fighthp == hp or fighthp > hp: 
                                    healingbonus = 0
                                    
                    #makes it so that they dont go over their original hp cap
                    elif fighthp < hp:
                        fighthp += healingbonus
                        if fighthp > hp:
                                fighthp = hp

                    elif fighthp == hp or fighthp > hp: 
                            healingbonus = 0

                totaldmgcalculations()
                #holds the spell dmg calculations

                if spell["Name"] == "Wand Attack":
                    if monstershield > 0 and totaldmg > monstershield:
                        totaldmg - monstershield
                        shieldloss = monstershield #shield lost will be used for animations
                        monstershield = 0
                        monsterHpLoss = mhp - totaldmg
                        mhp - totaldmg

                    elif monstershield > 0 and monstershield > totaldmg:
                        shieldloss = totaldmg 
                        monstershield = monstershield - totaldmg
                        
                    elif monstershield == 0:                    
                        monsterHpLoss = mhp - totaldmg
                        mhp - totaldmg
                        
                    fightmp += 3 

                    healingCalculations()
    
                elif spell["Name"] == "HP Drain":
                    if monstershield > 0 and totaldmg > monstershield:
                        totaldmg - monstershield
                        shieldloss = monstershield #shield lost will be used for animations
                        monstershield = 0
                        monsterHpLoss = mhp - totaldmg
                        mhp - totaldmg

                    elif monstershield > 0 and monstershield > totaldmg:
                        shieldloss = totaldmg 
                        monstershield = monstershield - totaldmg

                    elif monstershield == 0:                    
                        monsterHpLoss = mhp - totaldmg
                        mhp - totaldmg

                    healingspell = True
                    healingCalculations()

                elif spell["Name"] == "Protective Barrier":
                        playershield += mpdmg*(currentlvl*1.5)
                        healingCalculations()
            
                elif spell["Name"] == "Sacrificial Lamb":
                    #this adds spell effect dmg and halves hp
                    if playershield > 0:
                        totaldmg += fighthp/2 + playershield/2

                    else:
                        totaldmg += fighthp/2
                    fighthp /= 2

                    if monstershield > 0 and totaldmg > monstershield:
                        totaldmg - monstershield
                        shieldloss = monstershield #shield lost will be used for animations
                        monstershield = 0
                        monsterHpLoss = mhp - totaldmg
                        mhp - totaldmg

                    elif monstershield > 0 and monstershield > totaldmg:
                        shieldloss = totaldmg 
                        monstershield = monstershield - totaldmg
                        
                    elif monstershield == 0:                    
                        monsterHpLoss = mhp - totaldmg
                        mhp - totaldmg

                    fightmp = 0 

                    healingCalculations()
        
                elif spell["Name"] == "Heal":
                    healingspell = True
                    healingCalculations()

            variablesUpdate()
            window.update()
    
    def show_spell_info(spell): #shows spell info in label when hovered over.
        spellinfo_lab.config(text=f"\t\t{spell["Name"]} \n MP Cost: {spell["Mp Cost"]} \nDamage: {spell["Damage"]} \nDescription: {spell["Description"]}", font=("Courier", 12, "bold"), wraplength=500, justify="left", anchor="w")
         
    def hide_spell_info(event=None): #hides spell info in label.
        spellinfo_lab.config(text="")

    spell_buttons = []
    #need to go back to the array above and include spell pictures and call it spell["Spell Icon"]
    try:
        if character_selected == "Warrior":       
            for i, spell in enumerate(warriorspells):
                btn = tk.Button(spells_panel, image =spell["Spell Icon"], width=14, height=2,
                                command=lambda s=spell: spellactivation(s))        # click - s=spell is basically saving data in the index of each button - when the button is created each button will have its own lambda so s wont be overwritten - lambda is a function without any code under it, whatever u write next to it ='s its function - the : in s=spell: is basically assigning that variable to whatever comes after: because how in def they cant know information outside of defs, its the same thing. this calls the variable so can also do for ex: spell: spell *2
                btn.bind("<Enter>", lambda e, s=spell: show_spell_info(s))          # mouse over
                btn.bind("<Leave>", hide_spell_info)                                # mouse away
                btn.grid(row=0, column=0 + i, padx=5, pady=5)
                spell_buttons.append(btn)

        elif character_selected == "Mage":
            for i, spell in enumerate(magespells):
                btn = tk.Button(spells_panel, image =spell["Spell Icon"], text=spell["name"], width=14, height=2,
                                command=lambda s=spell: spellactivation(s))        # click - s=spell is basically saving data in the index of each button - when the button is created each button will have its own lambda so s wont be overwritten - lambda is a function without any code under it, whatever u write next to it ='s its function - the : in s=spell: is basically assigning that variable to whatever comes after: because how in def they cant know information outside of defs, its the same thing. this calls the variable so can also do for ex: spell: spell *2
                btn.bind("<Enter>", lambda e, s=spell: show_spell_info(s))          # mouse over
                btn.bind("<Leave>", hide_spell_info)                                # mouse away
                btn.grid(row=0, column=0 + i, padx=5, pady=5)
                spell_buttons.append(btn)

        elif character_selected == "Healer":
            for i, spell in enumerate(healerspells):
                btn = tk.Button(spells_panel, image =spell["Spell Icon"], text=spell["name"], width=14, height=2,
                                command=lambda s=spell: spellactivation(s))        # click - s=spell is basically saving data in the index of each button - when the button is created each button will have its own lambda so s wont be overwritten - lambda is a function without any code under it, whatever u write next to it ='s its function - the : in s=spell: is basically assigning that variable to whatever comes after: because how in def they cant know information outside of defs, its the same thing. this calls the variable so can also do for ex: spell: spell *2
                btn.bind("<Enter>", lambda e, s=spell: show_spell_info(s))          # mouse over
                btn.bind("<Leave>", hide_spell_info)                                # mouse away
                btn.grid(row=0, column=0 + i, padx=5, pady=5)
                spell_buttons.append(btn)

    except Exception as e:
        print("Spell buttons already exist", e)
        #---------------------------------------------turn defs---------------------------------------------------------------------------
    
    def end_turn():
        nonlocal pressedEndTurn
        pressedEndTurn = True #this is to properly destroy countdown timer if player presses end turn
        monster_turn()

    def monster_turn():        #need to add attack parts

            #will have to edit end turn where it activates countdown as well
        nonlocal fightmp 
        nonlocal mmp
        nonlocal turn 
        global timer
        nonlocal fighthp
        nonlocal mhp
        nonlocal pressedEndTurn
        global fightHpandMpset # this is set because when anyone dies dont want the hp to reset
        nonlocal oneSecondCountdown

        time.sleep(1.5) #makes it wait a second before switching turns

        if pressedEndTurn == True: #this is to properly destroy countdown timer if player calls end turn command
            if timer > 0:
                leftovertimer = timer
                timer = leftovertimer + 30
                if timer > 90:
                    timer = 90 #this caps the timer at 90 seconds

            countdown() #

        if oneSecondCountdown is not None and oneSecondCountdown in window.tk.call('after', 'info'):
            try:
               for after_id in window.tk.call('after', 'info'):
                window.after_cancel(after_id)
            except Exception as e:
                print ("There are no countdowns, or", e)


        #thi changes the turn icon from character img to monster img so you know its tthe monsters turn.
        if monstername == "Hierophant":

            monster_imgicon = tk.PhotoImage(file="Hierophanticon.png")
            yourturnimg_lab.config(image=monster_img)
            yourturnimg_lab.image = monster_imgicon

        elif monstername == "Goylca":

            monster_imgicon = tk.PhotoImage(file="Goylca_icon.png")
            yourturnimg_lab.config(image=monster_imgicon)
            yourturnimg_lab.image = monster_imgicon
            
        elif monstername == "Krosmo Crusher":

            monster_imgicon = tk.PhotoImage(file="Krosmo Crushericon.png")
            yourturnimg_lab.config(image=monster_imgicon)
            yourturnimg_lab.image = monster_imgicon

        elif monstername == "Bulmar":

            monster_imgicon = tk.PhotoImage(file="Bulmaricon.png")
            yourturnimg_lab.config(image=monster_imgicon)
            yourturnimg_lab.image = monster_imgicon

            # for when the player makes the mp go into negative it buffs monster and monster skips turn
        
        if mmp < 0: #for if the player makes the mp go into negative it buffs monster
            mmp = 0
            mmp +=20
            mmagical_dmg*2
            mphysical_dmg*2

        else:                  #attacks - will also include function where if monster kills player it will end fight/ - going to make monster spells in a loop - will make it do 3 attacks per turn or until it runs out of mp - was going to do a turn thing where thain gain dmg on dif turns but think will switch it to they gain damage depending on how many attacks they do so for example if the dmg count is 9 they gain dmg/spell dmg

                #when doing dmg calculation take its basically copy and paste from spellactivatgion
                #could also include the monster def actions, such as him hitting the player
                """
                will do an if for attacks by turn
                    if turn/5 = 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 - for the fifth turns
                    elif turn 4 = 
                    elif turn /3 = 
                    elif turn /2= 
                    else

                will do an array for type of attacks - will never use all mp - all monsters will have a 
            
                while loop for monster attack animation 
                        to make it pop up the spell animation label will make an empty label img and when a spell is triggered it configures the img and at the end it clears the img
                        updates spell position - (basically make a variable and make it = to the x of the starting position then put that variable in its place -  in the loop each time increase the value of the variable - can end the loop once the x is = to this for example)-
                        after it reaches x position a label with the total dmg will pop up
                        will do a .after to destroy the label for the pop up total dmg
                        
                """
            
        #-----------------end of turn stuff--------------------

            #basically sends it to after fight calculations or next turn - checks to see if someone died
        variablesUpdate
        try:
            time.sleep(1.5) #makes wait before switch turns

            if timer <= 0: #this will reset timer if the player didnt end turn
                timer = 30

            #end of turn mp recovery
            fightmp += 1
            mmp +=1
                
            turn += 1 # updates turn label by 1
            turnlab_text.set(f"Turn: {turn}")        
            
            character_turn()
        except Exception as e:
            print(e)

    def character_turn():
        nonlocal turn 
        nonlocal timerExists
        nonlocal fighthp
        global fightHpandMpset # this is set because when anyone dies dont want the hp to reset
        nonlocal oneSecondCountdown
        nonlocal fightmp

        timerExists = False #used to check if the timer exists or not - if it does then it will be destroyed and a new one will be created
        fighthp -= 1 #this is here for radiation, at start of turn player loses 1 hp - will add a check if it kills user  
        fightmp += 1 #every turn they get 1 mp
        variablesUpdate()#updates hp - check if radiation would end the fight           
        window.update()
        
        variablesUpdate()#updates hp and checks if anything died

        countdown() #starts the countdown timer for the turn

            #updates the character turn icon but not for turn 1
        if turn > 1:
            
            if character_selected == "Warrior":

                if gender == "Female":
                    #switches the preview img for warrior
                    turniconimg = tk.PhotoImage(file="f_warrioricon.png")
                    yourturnimg_lab.config(image=turniconimg)
                    yourturnimg_lab.image = turniconimg

                else:
                    #switches the preview img
                    turniconimg = tk.PhotoImage(file="m_warrioricon.png")
                    yourturnimg_lab.config(image=turniconimg)
                    yourturnimg_lab.image = turniconimg

                window.update()

            elif character_selected == "Mage":

                if gender == "Female":
                    #switches the preview img for mage
                    turniconimg = tk.PhotoImage(file="f_mageicon.png")
                    yourturnimg_lab.config(image=turniconimg)
                    yourturnimg_lab.image = turniconimg
                    
                else:
                    #switches the preview img
                    turniconimg = tk.PhotoImage(file="m_mageicon.png")
                    yourturnimg_lab.config(image=turniconimg)
                    yourturnimg_lab.image = turniconimg

                window.update()

            elif character_selected == "Healer":

                if gender == "Female":
                    #switches the preview img for healer
                    turniconimg = tk.PhotoImage(file="f_healericon.png")
                    yourturnimg_lab.config(image=turniconimg)
                    yourturnimg_lab.image = turniconimg

                else: #switches the preview img
                    turniconimg = tk.PhotoImage(file="m_healericon.png")
                    yourturnimg_lab.config(image=turniconimg)
                    yourturnimg_lab.image = turniconimg

                window.update()
                


                #basically sends it to after fight calculations - checks to see if someone died
                if fighthp == 0:
                    return

                elif mhp == 0:
                    return      

        variablesUpdate #hp checj

   #--------------------------------general buttons----------------------------
    #in a try so buttons wont be duplicated
    try:
        endturn_but = tk.Button(window, text="End Turn", bg="#00A8FF", font=("Ariel", 16, "bold"), command=end_turn, bd=2, width=10, height=2)
        endturn_but.place(relx=0.73, rely=0.95, relheight=0.07, relwidth=0.08, anchor="center")

        #end fight 
        endfight_but = tk.Button(window, text="End Fight", bg="#00A8FF", font=("Ariel", 16, "bold"), command=end_fight, bd=2, width=10, height=2)
        endfight_but.place(relx=0.32, rely=0.95, relheight=0.07, relwidth=0.08, anchor="center")

        #check monter stats 
        monsterstats_but = tk.Button(window, text="Monster Stats", bg="#00A8FF", font=("Ariel", 16, "bold"), command=monsterStatsWindow, bd=2, width=11, height=2)
        monsterstats_but.place(relx=0.22, rely=0.95, relheight=0.07, relwidth=0.11, anchor="center")

    except Exception as e:
        print("Already made general buttons or ", e)

    #THIS is the main key for ending the fight - if either the monster or player hp is 0 then it will destroy everything and go to end fight def
    if fighthp <= 0 or mhp <= 0:
        print("Fight has ended")
        #destroy everything
        try:
            endfight_but.destroy()
            endturn_but.destroy()
            monsterstats_but.destroy()
            yourturnimg_lab.destroy()
            mname_lab.destroy()
            mhp_lab.destroy()
            characterimgs_lab.destroy()
            name_lab.destroy() 
            hp_lab.destroy()
            turn_lab.destroy()
            spellinfo_lab.destroy()
            spells_panel.destroy()
            for b in spell_buttons:
                b.destroy()
                spell_buttons.clear()                  # empties the list so it doesn't hold dead buttons

            fightHpandMpset == False # this is set because need this so that the current hp of the monster and fighter dont change when i send it back to fight screen
            end_fight()

        except Exception as e:
            print(e)
            pass

        countdown() #this is here so that if the fight ends it will destroy the timer label and reset the timer to 0 for next fight and then it will go to end fght def in there.
    else:
        character_turn() #this is what actually starts the fight - its here because when the fight needs to end gonna send it back to fighting screen so i can properly destroy everything.
                      
#Run window
window.mainloop()
