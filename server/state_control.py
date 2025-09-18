import json

state = False # Resembles the state of the system: false if empty (sensor does not detect the bottle constantly), true when otherwise

def swap_state() -> bool:
    """
    Switches the current state (see docs for get_state for state)\n
    Returns: new state
    """
    global state
    state = not state
    return state

def set_state(new_state: bool) -> bool:
    """
    Sets the current state (see docs for get_state for state)\n
    Params: desired new state\n
    Returns: the state after update
    """
    global state
    state = new_state
    return state

def get_state() -> bool:
    """
    Resembles the state of the system: false if empty (sensor does not detect the bottle constantly), true when otherwise\n
    Returns: current state
    """
    return state

def log_state(new_state: bool):
    """Logs the current state to json file. No inputs, no outputs\n"""
    with open("memory.json", mode='a') as file:
        data = {
                "timestamp": f"{datetime.now()}",
                "state": f"{new_state}"
                }
        file.write(f"{json.dumps(data)}\n")
        file.close()
