# fighting-game-button-challenge
A tool to practice button inputs for fighting games on Windows. Ideal for leverless controllers in games like Street Fighter 6.

# 関連
[日本語版README](README.ja.md)

# TL;DR
- A button practice app for fighting games
- Random challenges are displayed
- Press the buttons matching the challenge to score points and move to the next challenge

# Implementation Status
- What you can do
    - You can challenge tasks like "Press Assist Button + Special Move Button!"
        - You can write any combination of lever and buttons in the config file
            - Button assignments and names are arbitrary, but writing them takes some effort

# More Details
- Button Challenge
    - Features
        - Resident
            - Since it's always running, you can use it the moment you want to practice, as soon as you input the lever or buttons—usable in 1 frame
            - The app comes to the front only when there is lever or button input
            - It automatically moves to the back 1 second after input stops, so it doesn't get in the way
            - While playing a fighting game, it automatically stays in the background, so it doesn't interfere
        - Random
            - After each mission success, the next mission is randomly selected
            - Train your flexibility to respond instantly to unexpected situations
        - Score
            - You can use it as a goal, like "Practice until you get 10 points"
    - Confirmed working environment
        - Windows
        - XInput
        - Arcade controller
            - Leverless controller (4 lever buttons + 10 buttons = 14 buttons)

# How to Use
- Clone the repository
- Run `button_challenge.bat`
    - To exit, press `CTRL+C` in the console
    - The config file is `button_challenge.toml`

# Problems This App Aims to Solve
- *This section is for explaining what this app is, for milestone reference, and for various other uses*
- Previous issues
    - Startup time
        - Most fighting games take about a minute from launch to training mode
        - What I want is something that instantly displays button prompts as soon as I press a controller button—zero wait
            - This app does that. It's always running, doesn't get in the way, and returns to the background 1 second after pressing a button.
    - Getting used to the controls of each fighting game
        - Most fighting games' control tutorials are often divided into:
            - Explanation part (can't move the character) and operation part (can't quickly select which operation to learn). Or there might not be an operation part at all.
            - After clearing, there is a few seconds of inactivity, causing a loss of time. It takes too long and doesn't have good tempo.
                - Insufficient for quickly grasping a full set of moves during initial learning.
                - Insufficient for firmly mastering each move one by one during initial learning.
                - Insufficient for quickly warming up during daily training.
            - There are no in-game quick warm-up recipes for daily training, requiring manual note-taking and visual practice in training mode.
        - What I want is for basic, intermediate (basic moves), and advanced (links, combos) operations to have:
            - Repetitive missions for practicing the same operation quickly and repetitively
            - Sequential missions that move to the next operation within 1 second of clearing the previous one
            - Random missions for learning to respond quickly to any situation
            - Once a mission config file is created, it should be automatically displayed in the app at any time
                - Eliminating the need for manual note-taking and visual practice in training mode
                    - Of course, more practical training should still be done in training mode, etc.
                - By sharing, you can smoothly learn from pre-defined missions without creating your own
            - This app aims to achieve that.
                - However, it will be limited to what's feasible. The specifications will be narrowed down. It won't be万能 (all-purpose). Using training mode, etc., is still a prerequisite.

# Examples of Using This App vs. Training Mode & Actual Combat
- *This is just an example*
- If you can't immediately tell which button corresponds to which move:
    - Get accustomed to the buttons using this app
- Once you're familiar with the buttons:
    - Do some training mode
    - Try actual combat
- If you currently can't start the game due to time constraints but still want to practice button inputs:
    - Practice button inputs using this app

# Out of Scope
- Input time limits, such as 6 frames from lever to button
- Very advanced missions
- Fancy graphics
- Fancy sounds (e.g., mission success fanfare)
- Extensive controller recognition
- Multi-platform support
- Browser app conversion
- Everything that a browser typing app can do
