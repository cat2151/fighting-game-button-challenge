# fighting-game-button-challenge (Fighting Game Button Challenge)
A practice app for fighting games on Windows. You can practice button inputs. Made for Street Fighter 6 Modern controls. Might also be useful for practicing other games.

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
- Undergoing frequent breaking changes

# What This App Is In 3 Lines
- A button practice app for fighting games
- Random challenges are displayed
- Pressing the correct button for the challenge earns a score and displays the next challenge

# A Bit More Detail
- Features
    - Always-on
        - Being an always-on application, it's ready to use the moment you feel like practicing and input a lever or button, available in 1 frame.
        - It only comes to the foreground when there's a lever or button input.
        - It moves to the background 1 second after input ceases, so it won't get in your way.
        - It automatically moves to the background while you're playing a fighting game, so it won't interfere.
    - Random
        - After each successful mission, the next mission appears randomly.
        - Train your flexibility to respond instantly to unexpected situations.
    - Time
        - You can compete to see how many frames it took to input.
        - * 30 frames is considered fast. This is because reading Japanese and the delay from not being able to narrow down 30 choices would likely take about 15 frames.
        - * For example, if you focus your mental allocation solely on Drive Impact, you can quickly reduce your reaction time to around 24 frames, but in turn, your reaction to everything else will slow down. Give it a try.
    - Score
        - Can be used as a benchmark, e.g., "Let's practice until I get 10 points."
    - Settings
        - It's likely possible to configure it for Classic controls, not just Modern.
        - It's likely possible to configure it for fighting games other than SF6, or even non-fighting games.
        - There are no configuration files for anything other than SF6 Modern. Try creating your own.
    - Hot Reload
        - When you edit the TOML configuration file, settings are automatically applied without restarting the app.
        - Convenient for toggling debug display on/off and for maintaining techniques.
        - After a reload, the app automatically restarts from the beginning of Phase 1.
        - Refer to [docs/hot_reload.md](docs/hot_reload.md) for details.
- Tested Environment
    - Windows
    - XInput
    - Arcade Controller
        - Leverless Controller (4 buttons + 10 buttons = 14 buttons)

# Usage
## Install
- Clone the repository.
- Run `pip install -r requirements.txt`.
## Settings
- Edit `config/button_names.toml` to match your game's button assignments.
- * There are several other configuration files. You can change display button name aliases and fonts.
## Launch
- Execute `button_challenge.bat`.
- To exit, press `CTRL+C` in the terminal.

# What This App Solves
- * This section is intended to explain what this app is, serve as a milestone guide, and for various other purposes.
- Previous Challenges
    - Startup Time
        - Most fighting games take about 1 minute from launch until you can enter training mode.
        - What's desired is an app that starts in 0 seconds and instantly displays button prompts when you press a controller button.
            - This app can do that. It's always-on. It won't get in your way. It moves to the background 1 second after a button press.
    - Getting Used to Each Fighting Game's Controls
        - Most fighting game control tutorials:
            - Are divided into explanation parts (where you can't move the character) and practice parts (where you can't quickly choose which action to learn). Or sometimes there's no practice part at all.
            - After clearing a segment, there's a few seconds of inaction, leading to wasted time. It takes too long, and the tempo is poor.
                - Insufficient for quickly grasping all basic moves when starting out.
                - Insufficient for thoroughly mastering each individual move when starting out.
                - Insufficient for quick warm-ups during daily training.
            - No quick warm-up routines exist within the game itself; they're not automatically displayed, requiring manual effort to write them down, refer to them, and practice in training mode.
        - What's desired is a mode that helps you understand what happens when you press which button by:
            - Using a mission format with success/failure judgments,
            - Allowing you to quickly complete one mission per second,
            - Covering all necessary button combinations for that game,
            - Allowing you to master them through repetitive practice,
            - A random mission mode aiming for quick, responsive actions in any situation,
            - If shared, you can learn smoothly from pre-defined missions without creating your own,
            - This app aims to achieve that.
                - However, it focuses on what's achievable. It narrows down specifications. It's not a panacea. The fundamental premise is to also utilize actual matches and training mode.

# Philosophy
- * Relates to the app's policy.
- Musical Instruments
    - Similar to practicing a musical instrument.
    - Through repetitive practice, you gradually become able to press buttons subconsciously.
        - Suggestion: It would be good if users could feel this progress as their app score gradually increases.
            - Suggestion: Provide a score type better suited for measuring actual skill.
            - Suggestion: It would also be good to provide a parallel score type that increases simply by continuing (like a cookie clicker) to boost motivation. The current score follows this approach.
- Mental Allocation
    - * The following are based on experience.
    - When you're not yet accustomed to the buttons, pressing them consumes a large portion of your mental allocation, frequently leading to an inability to grasp the situation or make decisions.
    - For example, understanding what move to choose and its outcome, or why you got hit by an opponent's move and what the countermeasure is, and reacting instantly in such situations, often becomes impossible when your mental resources are tied up with button inputs.
    - By becoming able to press buttons without conscious thought, the mental allocation previously consumed by buttons can be shifted to the match itself, leading to a more advantageous game flow.

# Example Usage with Actual Matches & Training Mode
- * This is just one example.
- If you're at the stage where you don't immediately know which button corresponds to which move:
    - Get familiar with buttons using this app.
- Once you're accustomed to the buttons:
    - Do training mode.
    - Play actual matches.
- If you can't launch the game itself in your free time, but still want to at least practice buttons:
    - Practice buttons with this app.

# Out of Scope
- Explanation of Python and module import procedures required to run this app: [issue-notes/12.md](https://github.com/cat2151/fighting-game-button-challenge/blob/main/issue-notes/12.md)
- Configuration files for anything other than SF6 Modern
- Configuration GUI
- Sequence inputs (e.g., `DI` > `A + Heavy`) → Handled by a separate project: [コマンドチャレンジ](https://github.com/cat2151/command-challenge)
- Highly advanced missions
- Lavish graphics
- Lavish sounds (e.g., mission success fanfare)
- Broad controller recognition
- Multi-platform support
- Web app conversion
- Everything a browser-based typing app can do

# Automatic English Translation
README.md is automatically generated from README.ja.md using Gemini's translation via GitHub Actions.