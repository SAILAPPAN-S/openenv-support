from fastapi import FastAPI
import uvicorn

from env.environment import SupportEnv
from models.schemas import Action

app = FastAPI()
env = SupportEnv()


@app.post("/reset")
def reset():
    return env.reset()


@app.post("/step")
def step(action: Action):
    return env.step(action)


@app.get("/state")
def get_state():
    return env.state()


# ✅ REQUIRED main() function
def main():
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)


# ✅ REQUIRED for OpenEnv
if __name__ == "__main__":
    main()