#imports
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import time
import random

"""this i want to fix- will do these later on, not pressing issues
1. loading page-  want to make the labels in here a bit bigger so no1 strains to see
2. perhaps make a label in the beginning telling the password and user - will edit it so they can make a new password first and it will be saved inside the variable - will make a button for it - later on if get a databse can take the value from the variable
3. notices that when you load it up it doesnt sit in the center so would need to move it abit
4. add more tips to help play the game
5. add music
6 clean up code proccess, move my global code to below, move my configures to the bottoms
7.    # if want to make gear would have to put 1 which monster drops what gear, how would character equip them, and an array that holds the information of the gears - could make the database work into this too. will use the dropdown to do determine that gear drop rates
    want to somehow encrypt my code so that people cant see it
    later on if decide to save information can just save the information from the variables and also include a portion where it updates the database in loading page - when i login can make an if and will take the stats saved in the database and make the variables = to that
8. add restrictions on names so that can use profanity languages
9. will need to replace class imgs
10. create a logout button
11.   in fight page  #need to make a message box or something that holds the information of the fight - can be small covering 4 commands
12.   will create like same makeshift animations, when click spell like a panel being made and it shows dmg/heals/barriers then disappears after 3 seconds - would like it to fade out but no clue yet - for now will get things working then will edit this is
13. make a file to hold all the imges so wont have multiple files all over the place and then redirect everything in the code
14. explain dmg calculations in stat page
15. edit code to include a tutorial

    #was working on general buttons - need to edit position 
    #after that going to go ahead and do the monster attack and animations, character stuff will be copying and pasting from ehre and will be much more work
    #  next making spell array
    #need to check loading page make sure leaving fightingpage works properly
    need to make it where when turn ends it deactivates all buttons, also in the if not turn 1, can also reactivate all buttons - after that can make another if cooldown != 0 deactivates again

    make command for spell button - dont need to add too much in here, could just check spell name and what character
    
    #spells button
    for spells gonna make an array 
    gonna make a panel to hold the buttons
        gonna make an if "class" then generates these type of buttons spells, will have elif for onther two classes, and add to panel
            gonna make the button loop for the amount of spells inside the if -
                inide the button loop gonna make a command - spell button - row always 0, columns increase by 1 each loop
                    spell button is gonna be a def and inside thats is more ifs that checks the name of the button, if button name = this it does this
                        will have it make a temporary label that shows the spell animations in between the two characters
                        will make it show an animation on the label with pictures and a time sleep 0.1 and have it move across the label -might ue ai for this part as a lot of work
                        then will calculate the spell dmg 

    

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
mpused = 0
mpdmg = mpused*2 #whenever need to do math with magical dmg only need to assign the value  mpused and add mpdmg 
basedmg = 3
totaldmg = mpdmg + basedmg

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

timer = None #used in fight calculations

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
        "mp": 50 +  + currentlvl*1.5, 
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

warriorspells = [
    {
        "Name": "Basic Attack",
        "MP Cost": 0,
        "Damage": "Base damage",
        "Description": "Hits the target without any MP to lightly damage the target. Gains 3 MP."
    },
    {
        "Name": "Strike",
        "MP Cost": 1,
        "Damage": "Base Damage + 2 + (lvl * 1.5)",
        "Description": "Strikes the target quickly with your sword. Gains 3 MP."
    },
    {
        "Name": "Swordsmanship",
        "MP Cost": 3,
        "Damage": "Base Damage + 6 + (lvl * 1.5)",
        "Description": "Uses MP to deal massive damage in a short time. Gains 3 MP."
    },
    {
        "Name": "Warrior's Sword",
        "MP Cost": "all",
        "Damage": "(MP used * 2 * 1.5) + Base Damage + (lvl * 1.5)",
        "Description": "Uses all your MP to deal a very heavy attack. Gains 3 MP."
    },
    {
        "Name": "Advance Shield",
        "MP Cost": 2,
        "Damage": "Base Damage + 4 + (lvl * 1.5)",
        "Description": "Hits the target and steals some HP with MP and generates a shield with it to advance next turn with. Gains 3 MP. The shield equals 4 + (lvl * 1.5) + 10."
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
        "Damage": "9 + (lvl * 1.5)",
        "Description": "Drains the target of MP equal to double the MP used. Causes slight damage as the target is being drained. Disables the target for 1 turn due to magic poisoning."
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
        "Description": "Reduces incoming damage by 40% for two turns."
    }
]

healerspells = [
    {
        "Name": "Wand Attack",
        "MP Cost": 0,
        "Damage": "Base Damage",
        "Description": "Hits the target without any MP to lightly damage the target. Heals 5 + (lvl * 1.5) HP."
    },
    {
        "Name": "HP Drain",
        "MP Cost": 5,
        "Damage": "15 + (lvl * 1.5)",
        "Description": "Drains the target's HP to heal itself. Heals 10 HP."
    },
    {
        "Name": "Protective Barrier",
        "MP Cost": 3,
        "Damage": "0",
        "Description": "Casts a strong shield to block enemy attacks. The barrier equals (6 * 2) * (lvl / 2 + 1)."
    },
    {
        "Name": "Sacrificial Lamb",
        "MP Cost": "100%",
        "Damage": "Current HP / 2 + 20 + (lvl * 1.5) + Barrier / 2",
        "Description": "Sacrifices half of your current HP and all of your MP to deal one high-damage attack. If you have a barrier, it also consumes half of the barrier. Has a 3-turn cooldown starting from the beginning of the fight."
    },
    {
        "Name": "Heal",
        "MP Cost": 1,
        "Damage": "0",
        "Description": "Heals 8 + (lvl * 1.5) HP at the cost of dealing no damage. The heal is boosted to help save yourself in times of need and low MP."
    }
]

fightstatus = None #will be updated to empty(no fight is happening), fight started, or fight ended

#-----------------------------------main window----------------------------------
#Create Window
window = tk.Tk()
window.title("MMO Game Simulator")
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
    text="MMO Game Simulator",
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
            info_labtxt.set("The Warrior is a class focused on delivering high physical damage. Unlike the mage class, it doesn't rely all on mp to cast spells. While highly durable, they have no built-in healing abilities. As they do not rely on mp they have little protecting against magical attacks.\n\n Bonuses: Base damage is multiplied by 1.5 \n\n\n\n Difficulty: Low\n\n *Make sure to click a class and type a name before you hit the create character button or you will get an error.")

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
            info_labtxt.set("The Healer is a class focused on self heals and deals low damage for long term fights. It relies on a steady use of mp to cast restorative spells and protective barriers during combat. While they can constantly recover from damage, they possess very low physical and magical damage output but can do a 1 time burst damage with the cost of half their life and all their mp.\n\n Bonuses: Each spell has better  individual bonuses than other classes.\n\n\n Difficulty:  high\n\n *Make sure to click a class and type a name before you hit the create character button or you will get an error.")

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
        text="Warrior", compound="top", width=37, height=50, command=selected_warrior  # Links instantly on click!
    )
    warrior_btn.grid(row=0, column=0, padx=5, pady=5)
    warrior_btn.image = warrior_icon # Keeps image from turning white

    # --- MAGE BUTTON ---
    mage_btn = tk.Button(
        left_panel, image=mage_icon,        # Replace with your actual mage image variable
        text="Mage", compound="top", width=37, height=50, command=selected_mage    # Links instantly on click!
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
        command=selected_healer  # Links instantly on click!
    )
    healer_btn.grid(row=1, column=0, padx=5, pady=5)
    healer_btn.image = healer_icon

def mainscreen():
    global monstername # for the label that shows monster name
    global name # for name label
    global character_selected
    global gender
    global difficulty

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

            #---------create spell labels-------

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
    global magespells
    global healerspells
    global warriorspells
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

    timerafter = None #this is used when switching from character turn to monster turn after timer ends
    difficulty_choice = difficulty.get()

    #used for calculations in fight to exit loop and also display variables - used so they dont change the innitial variables
    fighthp = hp
    #mhp is made inside  - monster hp
    fightmp = mp
    #mmp is made inside - monster mp

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

    #-----------create character img & label/hp label & spell buttons and methods-------------
  #label for character name
    namelabel_text = tk.StringVar()
    namelabel_text.set(f"{name} Lv. {currentlvl}")

    name_lab= tk.Label(window, textvariable=namelabel_text, font = ("Ariel", 18, "bold"), fg="black", bg="purple") #compount top basically makes everything stack on top of each other and whatever goes first is at top
    name_lab.place(relx=0.21, rely=0.31, anchor="center") # "w" anchors it to the West/Left side

    #picturetheir char - will need to use if to determine which char is shown

    characterimgs_lab= tk.Label(window, image=None, bg="purple")
    characterimgs_lab.place(relx=0.21, rely=0.55, anchor="center") # "w" anchors it to the West/Left side    

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
    
    #-------------------------------------timer label------------------------------------
    #timer label - fight will have a timer of 60 seconds, can increase if they play fast, timer will start automatically - the number will be changed in the loop
    timer = 60
    timerlab_text = tk.StringVar()
    timerlab_text.set(f"{timer}")

    timer_lab= tk.Label(window, textvariable=f"{timerlab_text}", font = ("Ariel", 24, "bold"), fg="black", bg="purple")
    timer_lab.place(relx=0.5, rely=0.1, anchor="center")

    #--------------------------------------------------after fight calculations fight mechs---------------------------------------------------------------------------
    #triggers fight experience and debuff calculations then sends to loading page if someone dies - still need to put the destroy parts - will connect it with the spell functions later on to determine if fight ends
    def end_fight():
        global fightstatus
        global difficulty_choice
        global timer
        global physical_defence
        global magical_defence
        global basedmg
        global hp
        global currentexp
        global currentlvl
        global pastlvl
        global currentexp

        
        if fighthp != 0:
            fighthp = 0

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
        elif mhp == 0:
            currentexp = currentexp + (baseexpgained*difficulty_multiplier)

        fightstatus = "Fight Ended"
        difficulty_choice = None
        timer = None #resets the timer to 0 for next fight - its just in case

        #destroy everything - will add these at the end as everything isnt set in stone
        
        loadingpage() 

    #-----------------------------------monster stats def-----------------------------------------------
    #for the stats button - 
    def monsterStatsWindow():
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
        mmp_label = tk.Label(stats_panel, text=f"MP: {mmp}", fg="white", bg="black", font=("Courier", 14, "bold"))
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
        monster_dmg_infolabel = tk.Label(stats_panel, text="*Total damage is calculated using Magical and Physical Damage instead of Base Damage", fg="white", bg="black", font=("Courier", 14, "bold"))
        monster_dmg_infolabel.grid(row=6, column=0, padx=10, pady=10)

        #Run window
        window.mainloop()

    #--------------------------------------------------turn defs---------------------------------------------------------------------------
    #need to add attack parts
    def monster_turn():
        nonlocal fightmp 
        nonlocal mmp
        nonlocal turn 
        global timer
        nonlocal fighthp
        nonlocal mhp
        nonlocal timerafter

        time.sleep(1.5) #makes it wait a second before switching turns

        # Check if the timer is currently active, then cancel it - this so monster_turn doesn't activate twice from timer
        if timerafter is not None:
            window.after_cancel(timerafter) #cancels
            timerafter = None   #Clear the ID since it is canceled just in case

        #add function that configures turn img to monster preview img - didnt configure this yet
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
        if mmp < 0:
            mmp = 0
            mmp +=20
            mmagical_dmg*2
            mphysical_dmg*2

            time.sleep(1.5) #makes wait before switch turns

            #----end of turn stuff-------

            #function that calculates new timer - timer wont start counting down till its your turn
            if timer != 0:
                leftovertimer = timer
                timer = leftovertimer + 30

            elif timer == 0:
                timer = 30

            if timer > 60:
                timer = 60

            turn + 1 # updates turn label by 1

            #end of turn mp recovery
            fightmp += 1
            mmp +=1

            #basically sends it to after fight calculations or next turn - checks to see if someone died
            #if is here because i dont want it to check if need to end the fight then if it does need to end the fight will still run character turn
            if fighthp == 0:
                end_fight()

            elif mhp == 0:
                end_fight()

            else:
                character_turn()

        #attacks and end turn
        else:

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
            time.sleep(1.5) #makes wait before switch turns

            #----end of turn stuff-------

            #function that calculates new timer - timer wont start counting down till its your turn
            if timer != 0:
                leftovertimer = timer
                timer = leftovertimer + 30

            elif timer == 0:
                timer = 30

            if timer > 60:
                timer = 60

            turn + 1 # updates turn label by 1

            #end of turn mp recovery
            fightmp += 1
            mmp +=1

            #basically sends it to after fight calculations or next turn - checks to see if someone died
            #if is here because i dont want it to check if need to end the fight then if it does need to end the fight will still run character turn
            if fighthp == 0:
                end_fight()

            elif mhp == 0:
                end_fight()

            else:
                character_turn()

    def character_turn():
        nonlocal turn
        global timer
        nonlocal timerafter

        timerafter = window.after(timer, monster_turn) # so monster turn starts after timer = 0

        #counts down timer
        def countdown():
            global timer
            if timer > 0:
                timer -= 1
                window.after(1000, countdown)
        countdown()

        #updates character turn icon but not for turn 1
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

        #if is here because i dont want it to check if need to end the fight then if it does need to end the fight will still run monster turn
        if fighthp == 0:
            end_fight()

        elif mhp == 0:
            end_fight()
        else: 
            monster_turn()

    character_turn()
        #-----------create spell methods and spell buttons----------------
    """DO THIS AFTER YOU MADE BUTTONS SO CAN USE BUTTON NAMES
    if character_selected == "Warrior":
        def spellactivation():
            global warriorspells
            if spellname = #start checking which was clicked button name was clicked 
        #do spell functions written below

            if 

    elif character_selected == "Mage":

    elif character_selected == "Healer":"""

    """
        if click spell do spell function - inside spell will be a while loop for animations so dont need to worry about time
        
        #might need to add new variable called cooldown for spell functions, if cooldown != 0 then will automatically deactivate the button at the start of the def- might make a small label that pops up for buttons with cooldowns, will just display "0/1/2"
        #need to include the end fight fucntion here
    """

    #--------------------------------general buttons----------------------------
    #end turn button
    endturn_but = tk.Button(window, text="End Turn", bg="#00A8FF", font=("Ariel", 16, "bold"), command=monster_turn, bd=2, width=10, height=2)
    endturn_but.place(relx=0.7, rely=0.86, anchor="center")

    #end fight 
    endfight_but = tk.Button(window, text="End Fight", bg="#00A8FF", font=("Ariel", 16, "bold"), command=end_fight, bd=2, width=10, height=2)
    endfight_but.place(relx=0.2, rely=0.86, anchor="center")

    #check monter stats 
    monsterstats_but = tk.Button(window, text="Monster Stats", bg="#00A8FF", font=("Ariel", 16, "bold"), command=monsterStatsWindow, bd=2, width=10, height=2)
    monsterstats_but.place(relx=0.23, rely=0.86, anchor="center")

#Run window
window.mainloop()