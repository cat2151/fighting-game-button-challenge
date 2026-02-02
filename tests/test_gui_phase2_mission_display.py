import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from missions import PHASE_1_BUTTONS, PHASE_2_MOVES


def compute_display_values(challenge_phase, mission, move_name, current_direction):
    """
    Helper function that defines the expected mission and direction arrow
    for a given phase and direction.

    It returns a tuple (displayed_mission, direction_arrow).
    """
    # Phase 1: show the mission text only.
    if challenge_phase == PHASE_1_BUTTONS:
        return mission, ""

    # Phase 2: hide the mission text and show only direction arrow
    if challenge_phase == PHASE_2_MOVES:
        direction_arrow = "→" if current_direction == "right" else "←"
        return "", direction_arrow

    # Default: no mission or direction arrow.
    return "", ""


def test_mission_display_logic_phase1():
    """Test that the mission display logic shows mission in phase 1"""
    challenge_phase = PHASE_1_BUTTONS
    mission = "右 + 強"
    move_name = "Drive Impact"
    current_direction = "right"

    displayed_mission, direction_arrow = compute_display_values(
        challenge_phase, mission, move_name, current_direction
    )

    # In phase 1, mission should be displayed (not empty)
    assert displayed_mission == mission, f"Expected mission '{mission}' to be displayed in phase 1"
    assert direction_arrow == "", f"Expected direction_arrow to be empty in phase 1"


def test_mission_display_logic_phase2_right():
    """Test that the mission display logic hides mission and shows right arrow in phase 2"""
    challenge_phase = PHASE_2_MOVES
    mission = "右 + 強"
    move_name = "Drive Impact"
    current_direction = "right"

    displayed_mission, direction_arrow = compute_display_values(
        challenge_phase, mission, move_name, current_direction
    )

    # In phase 2, mission should be hidden (empty string)
    assert displayed_mission == "", f"Expected mission to be hidden (empty) in phase 2, got: {displayed_mission}"
    # In phase 2, direction arrow should be displayed
    assert direction_arrow == "→", f"Expected '→' for right direction, got: {direction_arrow}"


def test_mission_display_logic_phase2_left():
    """Test that the mission display logic shows left arrow in phase 2 (left direction)"""
    challenge_phase = PHASE_2_MOVES
    mission = "左 + 強"
    move_name = "Drive Impact"
    current_direction = "left"

    displayed_mission, direction_arrow = compute_display_values(
        challenge_phase, mission, move_name, current_direction
    )

    # In phase 2, mission should be hidden
    assert displayed_mission == "", f"Expected mission to be hidden (empty) in phase 2"
    # In phase 2 left direction, should show left arrow
    assert direction_arrow == "←", f"Expected '←' for left direction, got: {direction_arrow}"


def test_mission_display_logic_phase2_no_move_name():
    """Test that direction arrow is shown in phase 2 regardless of move_name"""
    challenge_phase = PHASE_2_MOVES
    mission = "右 + 強"
    move_name = ""
    current_direction = "right"

    displayed_mission, direction_arrow = compute_display_values(
        challenge_phase, mission, move_name, current_direction
    )

    # In phase 2, mission should be hidden
    assert displayed_mission == "", f"Expected mission to be hidden (empty) in phase 2"
    # In phase 2, direction arrow should be displayed regardless of move_name
    assert direction_arrow == "→", f"Expected '→' for right direction, got: {direction_arrow}"
