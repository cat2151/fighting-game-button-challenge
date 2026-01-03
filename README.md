# fighting-game-button-challenge
A fighting game practice app for Windows. You can practice button inputs. Developed for Street Fighter 6 Modern controls. It might also be useful for practicing other games.

<p align="left">
  <a href="README.ja.md"><img src="https://img.shields.io/badge/🇯🇵-Japanese-red.svg" alt="Japanese"></a>
  <a href="README.md"><img src="https://img.shields.io/badge/🇺🇸-English-blue.svg" alt="English"></a>
  <a href="https://deepwiki.com/cat2151/fighting-game-button-challenge"><img src="https://deepwiki.com/badge.svg" alt="Ask DeepWiki"></a>
</p>

## Quick Links
| Item | Link |
|------|--------|
| 📊 Development Status | [generated-docs/development-status](generated-docs/development-status.md) |

# Status
- Subject to frequent breaking changes.

# App Description (in 3 lines)
- A fighting game button practice app.
- Random challenges are displayed.
- Pressing the correct button for the challenge earns you a score and displays the next challenge.

# More Details
- Features
    - Resident
        - Being a resident application, it's ready for use the moment you feel like practicing and input a lever or button, available in 1 frame.
        - It only comes to the foreground when there's a lever or button input.
        - It moves to the background 1 second after input stops, so it doesn't get in the way.
        - It automatically moves to the background while playing a fighting game, so it doesn't interfere.
    - Random
        - After each successful mission, the next mission appears randomly.
        - Train your adaptability to react quickly to unexpected situations.
    - Time
        - Compete to see how many frames it takes to input.
        - ※I think 30 frames is fast. This is because reading Japanese and the delay from not being able to narrow down 30 choices would likely take about 15 frames.
        - ※For example, if you focus your mental allocation solely on Drive Impact, you can quickly reduce the time to around 24 frames, but in turn, your reaction to anything other than Drive Impact will slow down. Give it a try.
    - Score
        - Can be used as a guideline, e.g., "Practice until you get 10 points."
    - Configuration
        - You can probably use it with Classic controls, not just Modern, by configuring it.
        - It can probably also be configured for fighting games other than SF6, or even games other than fighting games.
        - There are no configuration files for anything other than SF6 Modern. Try creating your own.
- Verified Environment
    - Windows
    - XInput
    - Arcade Controller
        - Leverless controller (4 buttons + 10 buttons = 14 buttons)

# How to Use
## Installation
- Please clone the repository.
- Run `pip install -r requirements.txt`.
## Configuration
- Edit `config/button_names.toml` to match your game's button assignments.
- ※There are a few other configuration files. You can change aliases for displayed button names and fonts.
## Launch
- Execute `button_challenge.bat`.
- To exit, press `CTRL+C` in the terminal.

# What This App Solves
- ※This section is intended to explain what this app is, serve as a milestone guideline, and for various other purposes.
- Existing Problems
    - Startup Time
        - Most fighting games take about a minute from launching to reaching training mode.
        - What's desired is something that shows button displays instantly (in 0 seconds) when a controller button is pressed.
            - This app achieves that. It's resident, doesn't interfere, and returns to the background 1 second after a button press.
    - Getting Used to Controls for Each Fighting Game
        - Most fighting game tutorials are structured such that:
            - They are often divided into an explanation part (where you can't move the character) and an operation part (where you can't quickly choose which operation to learn). Or, there might be no operation part at all.
            - Clearing a tutorial results in several seconds of inability to input, leading to wasted time. It takes too long, and the tempo is poor.
                - Insufficient for quickly grasping all moves when starting out.
                - Insufficient for thoroughly learning each individual move when starting out.
                - Insufficient for a quick warm-up during daily training.
            - There are no quick warm-up routines for daily training within the game itself; they aren't displayed automatically, requiring manual work like writing them down in a notebook and practicing them in training mode by sight.
        - What's desired is a mode where you can learn "what happens when you press which button" by:
            - Using a mission format with success/failure judgment,
            - Quickly playing one mission per second,
            - Covering all necessary button combinations for that game,
            - A mode that allows for repetitive practice to master them.
            - A random mission mode aiming to enable quick and appropriate actions in any situation.
            - By sharing, you can learn smoothly using pre-made mission definitions without having to create your own.
            - This app aims to achieve that.
                - However, it is limited to a feasible scope. Specifications are narrowed. It's not a panacea. The fundamental premise is to utilize both actual matches and training mode.

# Philosophy
- ※Related to the app's policy/direction.
- Musical Instrument
    - Similar to practicing a musical instrument.
    - Through repetitive practice, you'll gradually be able to press buttons subconsciously.
        - Idea: It would be good to feel the progress as the app's score increases while using it.
            - Idea: Provide a type of score that is more suitable for measuring actual skill.
            - Idea: It would also be good to provide a parallel "cookie-clicker-like" score that increases just by continuous play, serving as motivation. The current score follows this approach.
- Mental Allocation
    - ※The following are based on experience.
    - When you're not used to the buttons, merely pressing them consumes a large portion of your mental allocation, leading to frequent instances of being unable to grasp the situation or make decisions.
    - For example, understanding what move to choose and its outcome, or why you got hit by an opponent's move and what the counter-measure is, along with immediate responses, are often impossible when your mental resources are tied up with button inputs.
    - By becoming able to press buttons without conscious thought, the mental allocation previously consumed by buttons can be redirected to the match, leading to more favorable game developments.

# Example Usage with Actual Matches & Training Mode
- ※This is just one example.
- If you're at the stage where you don't immediately know "which button does which move?":
    - Get used to the buttons with this app.
- Once you're familiar with the buttons:
    - Play in training mode.
    - Play actual matches.
- If you can't launch the game itself during a spare moment but still want to practice buttons:
    - Practice buttons with this app.

# Out of Scope
- Explanation of Python and module import procedures required to run this app: [issue-notes/12.md](https://github.com/cat2151/fighting-game-button-challenge/blob/main/issue-notes/12.md)
- Configuration files for anything other than SF6 Modern
- Configuration GUI
- Sequence inputs (e.g., `DI` > `ア + 強`) → Handled by a separate project: [コマンドチャレンジ](https://github.com/cat2151/command-challenge)
- Highly advanced missions
- Elaborate graphics
- Elaborate sounds (e.g., mission success fanfare)
- Broad controller recognition
- Multi-platform support
- Web application conversion
- Everything a web-based typing app can do

# Automatic English Translation
README.md is automatically generated from README.ja.md using Gemini translation via GitHub Actions.