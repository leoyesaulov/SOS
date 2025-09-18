from fastapi import FastAPI
from state_control import set_state, get_state

app = FastAPI()

@app.post("/set_fill_state/")
async def set_fill_state(is_full: bool):
    set_state(is_full)

@app.get("/get_fill_state/")
async def get_fill_state():
    return get_state()

