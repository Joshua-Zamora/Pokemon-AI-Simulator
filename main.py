import random
import time

GREETINGS = [
    "YOOOO WADDUP",
    "HEY BESTIE",
    "OH MY GOSH HI",
    "AYYYY IT'S",
    "WELL WELL WELL, IF IT ISN'T",
    "*GASP* OMG IT'S",
    "BROOOO IT'S",
]

REACTIONS = [
    "how are you doing on this FINE day",
    "you look absolutely SWAGGY today",
    "did you eat breakfast? because you SHOULD have",
    "I was JUST thinking about you (I wasn't)",
    "you are literally my favorite person (don't tell the others)",
    "no way you're actually here right now",
]

FAREWELLS = [
    "ok BYE bestie",
    "peace out ✌️",
    "smell ya later",
    "don't forget to hydrate",
    "go touch some grass (lovingly)",
]


def print_hi(name):
    greeting = random.choice(GREETINGS)
    reaction = random.choice(REACTIONS)
    farewell = random.choice(FAREWELLS)

    print(f"\n{'='*40}")
    print(f"  {greeting} {name.upper()}!!!")
    print(f"{'='*40}")

    time.sleep(0.3)
    print(f"\n  ...and {reaction} 🤔")

    time.sleep(0.3)
    print(f"\n  anyway... {farewell}\n")


if __name__ == '__main__':
    print_hi('a Faggot')
