from fastapi import FastAPI
from state_control import set_state, get_state, log_state, get_stored_results
import os

app = FastAPI()

@app.post("/set_fill_state/")
async def set_fill_state(is_full: bool) -> None:
    old_state = get_state()
    if old_state != is_full:
        log_state(is_full)
    set_state(is_full)


@app.get("/get_fill_state/")
async def get_fill_state() -> dict:
    return {"answer": get_state()}

@app.get("/get_logs/")
async def get_logs():
    stored_result = ''
    if os.path.exists('memory.json'): 
        stored_result = get_stored_results()
    else:
        print('File does not exist')
    return stored_result

    

