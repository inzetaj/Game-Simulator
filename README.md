# Game Simulator

A Python desktop RPG battle simulator built with **Tkinter**. The project lets you create a character, choose a class and gender, inspect character and monster stats, and fight randomly selected monsters using class-specific abilities.

> **Project status:** This is a work in progress. Some features and gameplay systems may be incomplete or contain bugs.

## Features

- Login screen
- Character creation with a nickname, gender, and one of three classes
- Three playable classes:
  - **Warrior** — focused on physical damage and durability
  - **Mage** — focused on high magical damage and MP-based abilities
  - **Healer** — focused on healing, barriers, and longer fights
- Main screen with character information and a randomly selected monster
- Turn-based combat with character and monster turns
- Class-specific spell lists
- Character and monster stat windows
- Four difficulty settings: Easy, Normal, Hard, and Difficult
- Experience and level progression systems
- Image-based backgrounds, character art, and monster art

## Requirements

- Python 3
- Tkinter (usually included with standard Python installations)

The project uses Python's standard-library modules:
- `tkinter` and `tkinter.ttk` for the interface
- `datetime`
- `time`
- `random`

No third-party Python packages are currently imported by the project.

## Setup and Run

1. Make sure Python 3 is installed.
2. Keep `MMO Game Simulator.py` and the required image files together in the same directory.
3. Open a terminal or command prompt in that directory.
4. Run:

   ```bash
   python "MMO Game Simulator.py"
   ```

   On some systems you may need to use `python3` instead of `python`.

The program loads image assets by filename from the current working directory. If an image is missing or the program is started from a different directory, the interface may fail to load correctly.

## Login

The current login details are hard-coded in the Python file:

- **Username:** `username`
- **Password:** `password`

These are only placeholder credentials. The current version does not provide a database-backed account system or persistent account storage. Do not use real or sensitive passwords with this project.

## How to Play

1. Launch the program and log in.
2. Choose a character class.
3. Choose a gender and enter a nickname.
4. On the main screen, select a difficulty.
5. Start a fight against the displayed monster.
6. Use the available combat actions and spells, and end your turn when ready.
7. Check character or monster stats when you want to review their attributes.

## Monsters

The project defines four monster types:

- **Goylca** — stronger in magic and weaker physically
- **Bulmar** — physically strong and magically weak
- **Krosmo Crusher** — boss-style enemy with balanced offensive stats
- **Hierophant** — a defensive, tank-oriented enemy

The monster chosen for the next encounter is selected randomly.

## Spells and Abilities

Each class has its own set of abilities. The spell information includes MP costs, damage descriptions, and explanations of the effects.

Examples include:

- **Warrior:** Basic Attack, Strike, Swordsmanship, Warrior's Sword, Advance Shield
- **Mage:** Staff Attack, MP Drain, HP Drain, Magic Explosion, Damage Debuff
- **Healer:** Wand Attack, HP Drain, Protective Barrier, Sacrificial Lamb, Heal

Some abilities use MP while others provide healing, barriers, or defensive effects. Check the in-game spell window for the descriptions.

## Project Files

The Python script expects image assets with these filenames in the same directory:

```text
main.png
loadingbg2.png
mainscreen.png
mobfightbg.png
bossfightbg.png
m_warrior.png
m_mage.png
m_healer.png
f_warrior.png
f_mage.png
f_healer.png
m_warrioricon.png
m_mageicon.png
m_healericon.png
f_warrioricon.png
f_mageicon.png
f_healericon.png
Goylca.png
Goylca_icon.png
Bulmar.png
Bulmaricon.png
Hierophant.png
Hierophanticon.png
Krosmo Crusher.png
Krosmo Crushericon.png
```

Keep the filenames unchanged unless you also update the corresponding paths in the code.

## Known Limitations

- Account credentials are hard-coded and are not stored securely.
- Character progress is held in program variables and is not saved between launches.
- The code and gameplay are still under development, so some mechanics may not behave as intended.
- The interface depends on external image files being available at runtime.

## Future Improvements

Possible next steps include adding persistent save data, improving login and account handling, refining combat feedback and animations, expanding the tutorial, and polishing the interface.


