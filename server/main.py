from fastapi import FastAPI
from state_control import set_state, get_state, state, log_state

app = FastAPI()

@app.post("/set_fill_state/")
async def set_fill_state(is_full: bool) -> None:
    old_state = get_state()
    if old_state != is_full:
        log_state(is_full)
    set_state(is_full)


@app.get("/get_fill_state/")
async def get_fill_state() -> bool:
    return get_state()

