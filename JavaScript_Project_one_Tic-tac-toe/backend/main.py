from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from game import Game
import asyncio

app = FastAPI()

# CORS settings: allow frontend to access backend
origins = [
    "http://127.0.0.1:3000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # allow only frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize game state
game = Game()

@app.get("/")
def home():
    return {"message": "Backend is running"}

@app.get("/state")
def get_state():
    return {
        "board": game.board,
        "turn": game.turn,
        "winner": game.winner
    }


@app.post("/move/{index}")
async def move(index: int):
    game.make_move(index)
    if game.turn == "X" and game.winner is None:
        await asyncio.sleep(0.5)  # AI thinking 0.5 sec
    return get_state()


@app.post("/reset")
def reset():
    # Reset game state
    global game
    game = Game()
    return get_state()
