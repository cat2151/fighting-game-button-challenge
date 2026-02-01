import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from missions import PHASE_1_BUTTONS, PHASE_2_MOVES


def compute_display_values(challenge_phase, mission, move_name, current_direction):
    """
    Helper function that defines the expected mission and move text
    for a given phase and direction.

    It returns a tuple (displayed_mission, displayed_move_name).
    """
    # Phase 1: show the mission text only.
    if challenge_phase == PHASE_1_BUTTONS:
        return mission, ""

    # Phase 2: hide the mission text and, if present, show the move
    # name prefixed with a direction indicator.
    if challenge_phase == PHASE_2_MOVES:
        if not move_name:
            return "", ""
        indicators = {
            "right": "（右向き）",
            "left": "（左向き）",
        }
        direction_indicator = indicators.get(current_direction, "")
        return "", f"{direction_indicator}{move_name}"

    # Default: no mission or move text.
    return "", ""


def test_mission_display_logic_phase1():
    """Test that the mission display logic shows mission in phase 1"""
    challenge_phase = PHASE_1_BUTTONS
    mission = "右 + 強"
    move_name = "Drive Impact"
    current_direction = "right"

    displayed_mission, displayed_move_name = compute_display_values(
        challenge_phase, mission, move_name, current_direction
    )

    # In phase 1, mission should be displayed (not empty)
    assert displayed_mission == mission, f"Expected mission '{mission}' to be displayed in phase 1"
    assert displayed_move_name == "", f"Expected move_name to be empty in phase 1"


def test_mission_display_logic_phase2_right():
    """Test that the mission display logic hides mission and shows move in phase 2 (right direction)"""
    challenge_phase = PHASE_2_MOVES
    mission = "右 + 強"
    move_name = "Drive Impact"
    current_direction = "right"

    displayed_mission, displayed_move_name = compute_display_values(
        challenge_phase, mission, move_name, current_direction
    )

    # In phase 2, mission should be hidden (empty string)
    assert displayed_mission == "", f"Expected mission to be hidden (empty) in phase 2, got: {displayed_mission}"
    # In phase 2, move name should be displayed with direction indicator
    assert "（右向き）" in displayed_move_name, f"Expected '（右向き）' in displayed_move_name"
    assert move_name in displayed_move_name, f"Expected '{move_name}' in displayed_move_name"


def test_mission_display_logic_phase2_left():
    """Test that the mission display logic shows correct direction in phase 2 (left direction)"""
    challenge_phase = PHASE_2_MOVES
    mission = "左 + 強"
    move_name = "Drive Impact"
    current_direction = "left"

    displayed_mission, displayed_move_name = compute_display_values(
        challenge_phase, mission, move_name, current_direction
    )

    # In phase 2, mission should be hidden
    assert displayed_mission == "", f"Expected mission to be hidden (empty) in phase 2"
    # In phase 2 left direction, should show left indicator
    assert "（左向き）" in displayed_move_name, f"Expected '（左向き）' in displayed_move_name"
    assert move_name in displayed_move_name, f"Expected '{move_name}' in displayed_move_name"


def test_mission_display_logic_phase2_no_move_name():
    """Test that when move_name is empty in phase 2, displayed_move_name is also empty"""
    challenge_phase = PHASE_2_MOVES
    mission = "右 + 強"
    move_name = ""
    current_direction = "right"

    displayed_mission, displayed_move_name = compute_display_values(
        challenge_phase, mission, move_name, current_direction
    )

    # In phase 2, mission should be hidden
    assert displayed_mission == "", f"Expected mission to be hidden (empty) in phase 2"
    # When move_name is empty, displayed_move_name should also be empty
    assert displayed_move_name == "", f"Expected displayed_move_name to be empty when move_name is empty"
