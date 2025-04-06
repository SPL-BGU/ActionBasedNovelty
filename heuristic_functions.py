from syntax.state import State
import syntax.constants as constants
from collections import defaultdict

actions = None
unique_names = None
curr_list = None
check_goal = None


def start(grounded_instance):
    global actions
    global unique_names
    global curr_list
    global check_goal

    actions = grounded_instance.actions

    check_goal = lambda state: grounded_instance.goals(state, constants)

    # Assuming actions is a list of objects with a 'name' attribute
    unique_names = [act.name for act in grounded_instance.domain.actions]

    curr_list = [0] * len(unique_names)


def heuristic_function(state):
    global actions
    global unique_names
    global curr_list
    global check_goal

    if constants.CUSTOM_HEURISTIC_ID != 0:
        if check_goal(state):
            return 0

    if constants.CUSTOM_HEURISTIC_ID == 1:
        """Custom heuristic 1: number of grounded applicable actions"""
        return 1 / len(state.applicables_actions)
    elif constants.CUSTOM_HEURISTIC_ID == 2:
        """Custom heuristic 2: count activation of predecessor action"""
        return curr_list[unique_names.index(state.predecessor_action.name)]
    elif constants.CUSTOM_HEURISTIC_ID == 3:
        """Custom heuristic 3: inverse of number of novel actions"""
        lifted_actions = list(set(act.name for act in state.applicables_actions))

        binary_string = [
            1 if action in lifted_actions else 0 for action in unique_names
        ]

        novel = 0
        for i in range(len(curr_list)):
            if binary_string[i] == 1:
                novel += 1 / (curr_list[i] + 1)

        return 1 / novel
    elif constants.CUSTOM_HEURISTIC_ID == 4:
        """Custom heuristic 4: inverse of number of novel actions + activation of predecessor action"""
        lifted_actions = list(set(act.name for act in state.applicables_actions))

        binary_string = [
            1 if action in lifted_actions else 0 for action in unique_names
        ]

        novel = 0
        for i in range(len(curr_list)):
            if binary_string[i] == 1:
                novel += 1 / (curr_list[i] + 1)

        return (1 / novel) + curr_list[
            unique_names.index(state.predecessor_action.name)
        ]
    elif constants.CUSTOM_HEURISTIC_ID == 5:
        """Custom heuristic 5: number of lifted applicable actions"""
        lifted_actions = list(set(act.name for act in state.applicables_actions))
        return 1 / len(lifted_actions)

    return 0


def update_novelty(state) -> None:
    global actions
    global unique_names
    global curr_list

    if constants.CUSTOM_HEURISTIC_ID in [2, 3, 4]:
        action = state.predecessor_action
        if action is not None:
            curr_list[unique_names.index(action.name)] += 1

    return
