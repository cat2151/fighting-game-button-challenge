# fighting-game-button-challenge
A fighting game training app for Windows. It allows you to practice button inputs. Developed for Street Fighter 6 Modern controls, it might also be usable for practicing other games.

<p align="left">
  <a href="README.ja.md"><img src="https://img.shields.io/badge/🇯🇵-Japanese-red.svg" alt="Japanese"></a>
  <a href="README.md"><img src="https://img.shields.io/badge/🇺🇸-English-blue.svg" alt="English"></a>
</p>

## Quick Links
| Item | Link |
|------|--------|
| 📊 Development Status | [generated-docs/development-status](generated-docs/development-status.md) |

# What kind of app is it, explained in 3 lines
- A fighting game button practice app.
- Challenges are displayed randomly.
- Pressing the correct button for the challenge earns you a score and displays the next challenge.

# A bit more detailed
- Features
    - Persistent
        - Since it's a persistent application, you can start using it the moment you feel like practicing and input a lever or button, available in 1 frame.
        - It only comes to the foreground when there's a lever or button input.
        - It moves to the background 1 second after input stops, so it won't get in your way.
        - It automatically moves to the background while playing fighting games, so it won't interfere.
    - Random
        - After each successful mission, the next mission appears randomly.
        - Train your flexibility to react instantly to unexpected situations.
    - Time
        - You can compete to see how many frames it took to input.
        - ※ 30 frames is probably fast. This is because reading the Japanese text and the delay from not being able to narrow down 30 choices would likely take about 15 frames.
        - ※ For example, if you concentrate your mental resources solely on Drive Impact, you can quickly reduce your reaction time to around 24 frames, but in return, your reaction to other moves will slow down. Give it a try.
    - Score
        - You can use it as a guideline, e.g., "Let's practice until I get 10 points."
    - Settings
        - It can probably be configured for Classic controls too, not just Modern.
        - It can probably be configured for fighting games other than SF6, or even games outside the fighting game genre.
        - Configuration files for anything other than SF6 Modern are not provided. Try creating your own.
- Confirmed Operating Environment
    - Windows
    - XInput
    - Arcade Controller
        - Leverless controller (4 buttons + 10 buttons = 14 buttons)

# How to use
## Install
- Please clone the repository.
- Run `pip install -r requirements.txt`.
## Configuration
- Edit `config/button_names.toml` to match your game's button assignments.
- ※ There are several other configuration files. You can change the alias for displayed button names and the font.
## Launch
- Run `button_challenge.bat`.
- To exit, press `CTRL+C` in the terminal.

# What this app solves
- ※ This section is intended to explain what this app is, serve as a milestone reference, and for various other purposes.
- Previous Challenges
    - Startup Time
        - Most fighting games take about a minute from launching to reaching training mode.
        - What's desired is something that shows button prompts instantly when a controller button is pressed, with zero delay.
            - This app achieves that. It's persistent. It doesn't interfere. It moves to the background 1 second after a button press.
    - Getting used to operations for each fighting game
        - Most fighting game tutorials usually:
            - Are divided into an explanation part (where you can't move the character) and an operation part (where you can't quickly select which operation to learn). Or sometimes, there's no operation part at all.
            - After clearing a segment, there's a period of a few seconds where you can't control, leading to wasted time. It takes too long, and the tempo isn't good.
                - Insufficient for quickly grasping all basic moves when starting out.
                - Insufficient for thoroughly learning each individual move when starting out.
                - Insufficient for quick warm-ups during daily training.
            - There are no quick warm-up routines for daily training within the game, they aren't displayed automatically, and you have to manually write them down, refer to them, and self-practice in training mode.
        - What's desired is a mode that helps you understand what happens when you press which button, by:
            - Using a mission format where success or failure can be judged,
            - Allowing quick play of one mission per second,
            - Covering all necessary button combinations for that game,
            - Providing a mode for repetitive practice to master them.
            - A random mission mode aiming to enable quick and appropriate actions in any situation.
            - If missions can be shared, you can learn smoothly using mission definitions created by others, without having to create your own.
            - This app aims to achieve that.
                - However, it will be limited to what's feasible. The specifications will be focused. It's not a panacea. The fundamental premise is to also utilize actual matches and training mode.

# Philosophy
- ※ Relates to the app's policy/direction.
- Musical Instrument
    - It's similar to practicing a musical instrument.
    - Through repetitive practice, you'll gradually be able to press buttons subconsciously.
        - Idea: It would be good if users could feel this progress as their app score gradually increases while using the app.
            - Idea: Provide a type of score that is more suitable for measuring actual skill.
            - Idea: It would also be good to parallelly provide a score that increases just by continuing to play, acting as motivation (like a 'cookie clicker' game). The current score is designed with this approach.
- Mental Allocation
    - ※ The following are based on experience.
    - When you're not yet used to the buttons, pressing them alone consumes a large portion of your mental allocation, frequently leading to an inability to grasp the situation or make decisions.
    - For example, understanding what move was chosen and its result, or why an opponent's move connected and what the countermeasure is, and reacting instantly in such situations, is often not possible when your mental allocation is tied up with button inputs.
    - By becoming able to press buttons without conscious thought, the mental allocation previously consumed by buttons can be directed towards the match, leading to a more advantageous game progression.

# Example usage with actual matches & training mode
- ※ This is just one example.
- If you're at the stage where you don't immediately know "Which button performs which move?"
    - Get accustomed to the buttons with this app.
- Once you're familiar with the buttons,
    - Go to training mode.
    - Play actual matches.
- If you can't launch the main game in your spare time, but at least want to do some button practice!
    - Practice buttons with this app.

# Out of Scope
- Explanation of Python and module import procedures required to run this app: [issue-notes/12.md](https://github.com/cat2151/fighting-game-button-challenge/blob/main/issue-notes/12.md)
- Configuration files for anything other than SF6 Modern
- Settings GUI
- Sequence input (e.g., `DI` > `Attack + Heavy`) → Handled by a separate project: [Command Challenge](https://github.com/cat2151/command-challenge)
- Highly advanced missions
- Lavish graphics
- Elaborate sounds (e.g., mission success fanfare)
- Broad controller recognition
- Multi-platform support
- Web app conversion
- All capabilities of browser-based typing apps

# Automatic English Translation
README.md is automatically generated from README.ja.md using Gemini's translation via GitHub Actions.