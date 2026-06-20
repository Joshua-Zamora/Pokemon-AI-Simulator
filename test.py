import sys
import random
from collections import defaultdict

sys.path.insert(0, "/home/workdir")

from cg.game import battle_start, battle_select, battle_finish
from cg.api import to_observation_class
from main import agent

# ==================== CONFIG ====================
NUM_GAMES = 1000          # Change this to run more/less games
PRINT_EVERY = 100         # Print progress every N games
# ===============================================

# Load your deck
with open("deck.csv") as f:
    deck = [int(line) for line in f.read().splitlines() if line.strip()]


def random_agent(obs_dict: dict) -> list[int]:
    """Simple random agent that picks valid random choices."""
    obs = to_observation_class(obs_dict)
    if obs.select is None:
        return deck  # Shouldn't happen during a game

    select = obs.select
    min_c = max(0, select.minCount)
    max_c = min(len(select.option), select.maxCount)

    if max_c == 0:
        return []

    n = random.randint(min_c, max_c)
    return random.sample(range(len(select.option)), n)


# ==================== RUN GAMES ====================
wins = 0
total_turns = 0
game_results = []

print(f"Running {NUM_GAMES} games: Your Agent vs Random Agent\n")

for game_num in range(1, NUM_GAMES + 1):
    obs, _ = battle_start(deck, deck)
    turn = 0

    while True:
        if obs.get("select") is None:
            break

        current = obs.get("current") or {}
        if current.get("result", -1) != -1:
            break

        turn += 1
        player = current.get("yourIndex", 0)

        if player == 0:
            choice = agent(obs)
        else:
            choice = random_agent(obs)

        # Safety fallback
        if not choice and obs["select"]["minCount"] > 0:
            if len(obs["select"]["option"]) > 0:
                choice = [0]

        obs = battle_select(choice)

    # Game finished
    final_result = (obs.get("current") or {}).get("result", -1)
    total_turns += turn

    if final_result == 0:
        wins += 1
        result_str = "WIN"
    elif final_result == 1:
        result_str = "LOSS"
    else:
        result_str = "DRAW"

    game_results.append(result_str)

    if game_num % PRINT_EVERY == 0:
        current_winrate = (wins / game_num) * 100
        print(f"Game {game_num:3d} | Result: {result_str} | Winrate so far: {current_winrate:.1f}% | Turns: {turn}")

# ==================== SUMMARY ====================
winrate = (wins / NUM_GAMES) * 100
avg_turns = total_turns / NUM_GAMES

print("\n" + "="*50)
print("FINAL RESULTS")
print("="*50)
print(f"Games played : {NUM_GAMES}")
print(f"Wins         : {wins}")
print(f"Losses       : {NUM_GAMES - wins}")
print(f"Win rate     : {winrate:.2f}%")
print(f"Average turns: {avg_turns:.1f}")
print("="*50)