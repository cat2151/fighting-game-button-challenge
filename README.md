# fighting-game-button-challenge (Fighting Game Button Challenge)
A fighting game training app for Windows. It allows you to practice button inputs. Developed specifically for Street Fighter 6 Modern controls, but may also be useful for practicing other games.

[English README](README.md)

# App Summary in 3 Lines
- A fighting game button practice app.
- Random challenges are displayed.
- Pressing the correct button for the challenge earns you a score and displays the next challenge.

# More Details
- Features
    - Resident
        - As a resident application, it's ready for use the moment you feel like practicing and input a lever or button; it's available in 1 frame.
        - It comes to the foreground only when there's a lever or button input.
        - It moves to the background 1 second after input stops, so it won't get in your way.
        - It automatically moves to the background while you're playing a fighting game, ensuring it doesn't interfere.
    - Random
        - After each successful mission, the next mission appears randomly.
        - Train your flexibility to react instantly to unexpected situations.
    - Time
        - Compete to see how many frames it took you to input.
        - * 30 frames is considered fast. This is because reading Japanese and the delay from not being able to narrow down from 30 choices could take about 15 frames.
        - * For example, if you focus your attention solely on Drive Impact, you can quickly reduce it to about 24 frames, but your reaction to anything other than Drive Impact will slow down. Give it a try.
    - Score
        - Can be used as a benchmark, e.g., "Practice until you get 10 points."
    - Settings
        - Classic controls, not just Modern, are likely possible if configured.
        - Fighting games other than SF6, or even games other than fighting games, are likely possible if configured.
        - There are no configuration files for anything other than SF6 Modern. Try creating your own.
- Environment Confirmed to Work
    - Windows
    - XInput
    - Arcade Controller
        - Leverless Controller (4 buttons + 10 buttons = 14 buttons)

# Usage
## Installation
- Clone the repository.
- Run `pip install -r requirements.txt`.
## Configuration
- Edit `config/button_names.toml` to match your game's button assignments.
- * There are several other configuration files. You can change display button name aliases and fonts.
## Launch
- Run `button_challenge.bat`.
- To exit, press `CTRL+C` in the terminal.

# What This App Solves
- * This section is intended to explain what this app is, serve as a milestone guideline, and for various other purposes.
- Previous Challenges
    - Startup Time
        - Most fighting games take about a minute from launching to reaching training mode.
        - What's needed is something that takes 0 seconds, where pressing a controller button immediately displays a button prompt.
            - This app achieves that. It's resident, unobtrusive, and returns to the background 1 second after a button press.
    - Getting used to controls for each fighting game.
        - Most fighting game tutorials are:
            - Divided into an explanation part (where you can't move the character) and an operation part (where you can't quickly select which operation to learn). Or sometimes, there's no operation part at all.
            - After clearing, there's a several-second period of inactivity, which wastes time. It takes too long, and the tempo is poor.
                - Insufficient for quickly grasping all moves when starting out.
                - Insufficient for thoroughly mastering individual moves when starting out.
                - Insufficient for quick warm-ups during daily training.
            - There are no quick warm-up routines built into the game, nor are they displayed automatically. It requires manual effort: writing them down, referring to notes, and self-practicing in training mode.
        - What's needed is a way to learn "what happens when I press which button" that:
            - Uses a mission format, with success/failure judgments.
            - Allows quick play of one mission per second.
            - Covers all necessary button combinations for that game.
            - Provides a mode for repetitive practice to master them.
            - Features random missions, aiming to enable quick, responsive operations in any situation.
            - If shared, allows smooth learning from predefined missions by predecessors, without needing to create your own.
            - This app aims to achieve that.
                - However, it focuses on what is feasible, narrows down specifications, and is not a panacea. The fundamental premise is to utilize both actual matches and training mode.

# Approach
- * Relates to the app's policy/direction.
- Musical Instrument
    - Similar to practicing a musical instrument.
    - Through repetitive practice, you'll eventually be able to press buttons unconsciously.
        - Idea: It would be good if users could feel this progress by seeing their app score gradually increase.
            - Idea: Provide a score type better suited for measuring actual skill.
            - Idea: It would also be good to provide a parallel score (like a cookie clicker) that increases simply by continuing, serving as motivation. The current score follows this approach.
- Attention Allocation
    - * The following are based on experience.
    - When you're not yet accustomed to the buttons, pressing them consumes a large portion of your attention, often leading to an inability to grasp the situation or make decisions.
    - For example, grasping "what move did I choose and what was the result?" or "why did I get hit by the opponent's move and what's the countermeasure?" and reacting instantly to such situations is often impossible when your attention is consumed by button inputs.
    - As you become able to press buttons without conscious thought, the attention previously allocated to buttons can be redirected to the match itself, leading to a more favorable match development.

# Example Usage with Actual Matches & Training Mode
- * This is just one example.
- If you're at the stage where you don't immediately know "which button does which move?":
    - Get accustomed to the buttons with this app.
- Once you're familiar with the buttons:
    - Play in Training Mode.
    - Play Actual Matches.
- If you can't launch the main game during a break, but want to at least practice buttons:
    - Practice buttons with this app.

# Out of Scope
- Instructions for Python and module import steps required to run this app: [issue-notes/12.md](https://github.com/cat2151/fighting-game-button-challenge/blob/main/issue-notes/12.md)
- Configuration files for anything other than SF6 Modern.
- Settings GUI
- Sequence input (e.g., `DI` > `A + Heavy`) → This will be handled by a separate project: [command-challenge](https://github.com/cat2151/command-challenge)
- Highly advanced missions
- Elaborate graphics
- Elaborate sounds (e.g., mission success fanfare)
- Broad controller recognition
- Multi-platform support
- Web app conversion
- All features of browser-based typing apps.

# Automatic English Translation
README.md is automatically generated from README.ja.md using Gemini's translation via GitHub Actions.