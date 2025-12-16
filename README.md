# fighting-game-button-challenge (Fighting Game Button Challenge)
A fighting game practice app for Windows. It allows you to practice button inputs. Developed for Street Fighter 6 Modern controls, it might also be useful for practicing other games.

<p align="left">
  <a href="README.ja.md"><img src="https://img.shields.io/badge/🇯🇵-Japanese-red.svg" alt="Japanese"></a>
  <a href="README.md"><img src="https://img.shields.io/badge/🇺🇸-English-blue.svg" alt="English"></a>
</p>

## Quick Links
| Item | Link |
|------|--------|
| 📊 Development Status | [generated-docs/development-status](generated-docs/development-status.md) |

# Status
- Undergoing frequent breaking changes

# App Description in 3 Lines
- A fighting game button practice app.
- Displays random challenges.
- Pressing the correct button for the challenge earns a score and displays the next challenge.

# More Details
- Features
    - Always-on
        - Being an always-on application, it's ready the moment you want to practice and input a lever or button, available in 1 frame.
        - It only brings itself to the foreground when there's a lever or button input.
        - It moves to the background 1 second after input stops, so it won't get in your way.
        - While playing a fighting game, it automatically moves to the background, so it won't interfere.
    - Random
        - After each successful mission, the next mission appears randomly.
        - Train your flexibility to react instantly to unexpected situations.
    - Time
        - Compete to see how many frames it takes to input.
        - *30 frames is considered fast, as reading Japanese and the delay from not being able to narrow down 30 choices would likely take around 15 frames.
        - *For example, if you focus your awareness solely on Drive Impact, you can quickly reduce it to around 24 frames, but this will slow down your reaction to everything else. Give it a try.
    - Score
        - Can be used as a benchmark, e.g., "Let's practice until I get 10 points."
    - Configuration
        - It can likely also be configured for Classic controls, not just Modern.
        - It can likely also be configured for fighting games other than SF6, or even other genres of games.
        - There are no configuration files for anything other than SF6 Modern. Try creating your own.
- Tested Environment
    - Windows
    - XInput
    - Arcade Controller
        - Leverless Controller (4 buttons + 10 buttons = 14 buttons)

# Usage
## Install
- Please clone the repository.
- Run `pip install -r requirements.txt`.
## Configuration
- Please edit `config/button_names.toml` to match your game's button assignments.
- *There are a few other configuration files. You can change the aliases for displayed button names and fonts.
## Launch
- Run `button_challenge.bat`.
- To exit, use `CTRL+C` in the terminal.

# What This App Solves
- *This section is intended to explain what this app is, serve as a guideline for milestones, and for various other purposes.
- Previous Challenges
    - Startup Time
        - Most fighting games take about a minute from startup to reaching training mode.
        - What's needed is something that shows button displays instantly, in 0 seconds, as soon as a controller button is pressed.
            - This app does that. It's always-on, non-intrusive, and moves to the background 1 second after a button press.
    - Getting Used to Each Fighting Game's Controls
        - Most fighting game control tutorials:
            - Are often divided into an explanation part (where you can't move the character) and an operation part (where you can't quickly select which operation to learn). Or sometimes there's no operation part at all.
            - After clearing, there's a few seconds of uncontrollable time, leading to wasted time. It takes too long and the tempo isn't good.
                - Insufficient for quickly grasping all moves when first starting out.
                - Insufficient for thoroughly learning each individual move when first starting out.
                - Insufficient for quickly warming up during daily training.
            - There's no quick warm-up routine for daily training within the game itself, nor is it displayed automatically. It requires manually writing notes and referring to them while self-practicing in training mode.
        - What's needed is a way to understand which button press leads to which action, through:
            - A mission format where success or failure can be judged,
            - The ability to quickly play one mission per second,
            - Covering all necessary button combinations for that game,
            - A mode for repetitive practice to master them,
            - A random mission mode, aiming to enable quick and appropriate actions in any situation,
            - If shared, one can smoothly learn with mission definitions from experienced players, without having to create their own.
            - This app aims to achieve that.
                - However, it will focus on what's feasible, narrow down specifications, and is not a panacea. The fundamental premise is to also utilize actual matches and training mode.

# Philosophy
- *Relates to the app's direction.
- Musical Instrument
    - Similar to practicing a musical instrument.
    - Through repetitive practice, you gradually become able to press buttons unconsciously.
        - Idea: It would be good if users could feel this progress as their app score gradually increases while using the app.
            - Idea: Provide a type of score that is more suitable for measuring actual skill.
            - Idea: It would be good to also provide a parallel score that increases simply by continuing (like a cookie clicker game) to motivate users; the current score follows this approach.
- Mental Allocation
    - *The following are based on anecdotal experience.
    - When not accustomed to buttons, a significant portion of your mental allocation is taken up just by pressing them, leading to frequent failures in grasping the situation or making decisions.
    - For example, understanding what move was chosen and its result, or why an opponent's move landed and what the counter-measure is, along with immediate on-the-spot reactions, are often impossible when your mental allocation is tied up with button presses.
    - By becoming able to press buttons without conscious thought, the mental allocation previously dedicated to buttons can be redirected to the match, leading to more favorable game developments.

# Example Usage with Real Matches & Training Mode
- *This is just one example.
- If you're at the stage where you don't immediately know which button corresponds to which move:
    - Get used to the buttons with this app.
- Once you're comfortable with the buttons:
    - Do training mode.
    - Play real matches.
- If you can't launch the main game in your spare time, but at least want to practice buttons:
    - Practice buttons with this app.

# Out of Scope
- Explanation of Python and module import procedures required to run this app: [issue-notes/12.md](https://github.com/cat2151/fighting-game-button-challenge/blob/main/issue-notes/12.md)
- Configuration files other than SF6 Modern
- Configuration GUI
- Sequence input (e.g., `DI` > `Attack + Heavy`) → This will be handled by a separate project: [command-challenge](https://github.com/cat2151/command-challenge)
- Highly advanced missions
- Lavish graphics
- Elaborate sounds (e.g., mission success fanfare)
- Broad controller recognition
- Multi-platform support
- Web app conversion
- All capabilities of a browser-based typing app

# Automatic Translation
README.md is automatically generated from README.ja.md using Gemini's translation via GitHub Actions.