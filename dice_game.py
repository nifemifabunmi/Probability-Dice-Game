import numpy as np
import matplotlib.pyplot as plt
from itertools import product

def roll_dice(n_dice=2):
    """Simulate rolling n_dice dice with n_sides sides each.

    Args:
        n_dice (int): Number of dice to roll.
        n_sides (int): Number of sides on each die.

    Returns:
        list: A list containing the result of each die roll.
    """
    return np.random.randint(1, 7, size=n_dice)

def calculate_odds(n_dice=2, target_sum=7):
    outcomes = list(product(range(1, 7), repeat=n_dice))
    total_outcomes = len(outcomes)
    winning_outcomes = [outcome for outcome in outcomes if sum(outcome) == target_sum]
    probability = len(winning_outcomes) / total_outcomes
    payout = 6 # Example payout for hitting the target sum
    expected_value = (probability * payout) - ((1 - probability) * 1) # Assuming a $1 bet
    return probability, expected_value

def plot_probability(n_dice):
    sums = [sum(o) for o in product(range(1,7), repeat=n_dice)]
    plt.hist(sums, bins=range(n_dice,6*n_dice+2), align='left', rwidth=0.8)
    plt.xlabel("Sum of Dice")
    plt.ylabel("Frequency")
    plt.title(f"Probability Distribution for {n_dice} Dice")
    plt.show()

def main():
    print("Welcome to Probability Dice Game! 🎲")
    rounds = int(input("How many rounds do you want to play? "))
    
    for i in range(rounds):
        print(f"\n--- Round {i+1} ---")
        try:
            n_dice, player_sum = map(int, input("Enter number of dice and your guess (e.g., 2 7): ").split())
        except ValueError:
            print("Invalid input, try again.")
            continue
        dice = roll_dice(n_dice)
        print(f"Dice rolled: {dice} → Sum: {sum(dice)}")
        prob, ev = calculate_odds(n_dice, player_sum)
        print(f"Probability of sum {player_sum}: {prob:.3f}")
        show_cheat = input("See expected value? (y/n): ").lower()
        if show_cheat == 'y':
            print(f"Expected value for sum {player_sum}: {ev:.2f}")
        plot_probability(n_dice)

if __name__ == "__main__":
    main()