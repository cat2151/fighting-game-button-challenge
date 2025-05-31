# fighting-game-button-challenge
A tool to practice button inputs for fighting games on Windows. Ideal for leverless controllers in games like Street Fighter 6.

[日本語 README](README.ja.md)

# TL;DR
- A button practice app for fighting games
- Random challenges are displayed
- Press the buttons matching the challenge to score points and move to the next challenge

# Details
- Features
    - Resident
        - The app runs in the background, so you can use it instantly as soon as you input a lever or button—usable in 1 frame
        - The app comes to the front only when there is lever or button input
        - It automatically moves to the back 1 second after input stops, so it doesn't get in the way
        - While playing a fighting game, it automatically stays in the background, so it doesn't interfere
    - Random
        - After each successful mission, the next mission is randomly selected
        - Train your flexibility to respond instantly to unexpected situations
    - Score
        - Use the score as a goal, e.g., practice until you reach 10 points
- Tested Environment
    - Windows
    - XInput
    - Arcade controller
        - Leverless controller (4 buttons + 10 buttons = 14 buttons)

# How to Use
- Clone the repository
- Run `button_challenge.bat`
    - To exit, press `CTRL+C` in the console
    - Configuration files: `button_challenge.toml`, `button_names.toml`, `lever_names.toml`

# Under Consideration
- Random left/right, simplifying toml
    - For entries in `button_challenge.toml` with "left" or "right", for now only "right" is used and "left" is removed
    - In `button_challenge.toml`, `left_right = ['Left', 'Right']`
    - During play, use `left_right` to randomly flip left/right with 50% probability
    - (After alias implementation) Instead of left/right, you can specify front/back or 123456789
- Alias, display both `SA2` and `Right + Strong + Special`

# Future Plans
- Will decide next steps after some dogfooding
- There are many issues and plans, but they are omitted here
    - Will do what I want to do

# Issues
- The input descriptions and feedback are not intuitive
    - Ideally:
        - The input description would be an image like "The opponent jumps in while you have SA3 charged, so press the one-button SA3"
        - The feedback would be an image of SA3 hitting
    - Realistically:
        - For now, will observe with the current descriptions
    - Notes:
        - Making it juicier with sound effects or visual effects will be considered in the future

# What This App Solves
- *This section is for explaining what this app is, as a milestone reference, and for various other uses*
- Previous Issues
    - Startup time
        - Most fighting games take about a minute from launch to training mode
        - What I want is something that shows button prompts instantly when I press a controller button—zero seconds
            - This app does that. Resident type. Doesn't get in the way. Returns to the background 1 second after pressing a button.
    - Getting used to each game's controls
        - Most fighting game tutorials are split into explanation parts (where you can't move the character) and operation parts (where you can't quickly choose which move to learn). Or there is no operation part at all.
        - After clearing, there is a period where you can't operate for a few seconds, which wastes time and breaks the tempo.
            - Not enough for quickly learning all moves as a beginner.
            - Not enough for thoroughly mastering each move as a beginner.
            - Not enough for quick warm-up during daily training.
        - There is no quick warm-up recipe for daily training in the game, so you have to write it in a notebook and practice manually in training mode.
    - What I want is:
        - To know what button does what, in a mission format, with success/failure judgment
        - To play one mission per second for quick practice
        - To cover all necessary button combinations for the game
        - To have a mode for repetitive practice to master them
        - To have a random mission mode to practice responding quickly in any situation
        - To be able to share and learn smoothly from missions defined by others without making your own
        - This app aims for that
            - But will focus on what is realistically possible. Will narrow the scope. Not all-purpose. Actual matches and training mode are still essential.

# Example Usage with Matches & Training Mode
- *Just an example*
- If you don't know which button does which move:
    - Get used to the buttons with this app
- Once you get used to the buttons:
    - Use training mode
    - Play actual matches
- If you can't launch the game right now but want to practice buttons:
    - Practice with this app

# Out of Scope
- Sequence inputs (e.g., `DI` > `Arc + Strong`) → Handled in a separate project: [Command Challenge](https://github.com/cat2151/command-challenge)
- Very advanced missions
- Fancy graphics
- Fancy sounds (e.g., mission success fanfare)
- Wide controller support
- Multi-platform
- Browser app
- Everything that browser-based typing apps can do
