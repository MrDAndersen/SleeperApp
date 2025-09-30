# main.py — Summon a user scroll
from sleeper import SleeperUser
from sleeper import SleeperBase

if __name__ == "__main__":
    user = SleeperUser(username="mrdandersen")
    print(user.get_user_leagues())
