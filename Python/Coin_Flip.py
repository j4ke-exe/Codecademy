import numpy
from typing import Tuple

def flip_coin(num_flips: int) -> Tuple[int, int]:
    coin_flip = numpy.random.binomial(n=1, p=0.5, size=num_flips)
    heads = sum(coin_flip)
    tails = num_flips - heads
    return heads, tails

def display_winner(heads: int, tails: int) -> str:
    return "Heads" if heads > tails else "Tails"

def main():
    num_flips = 1000
    heads, tails = flip_coin(num_flips)
    print("Simple Heads or Tails Game")
    print(f"A coin will flip {num_flips} times and tally up the total flips per side.")
    print(f"The side with the most flips wins.")
    print(f"Number of tails: {tails}")
    print(f"Number of heads: {heads}")
    print("-" * 20)
    print(f"Winner: {display_winner(heads, tails)}")

if __name__ == "__main__":
    main()
