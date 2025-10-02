import random
import matplotlib.pyplot as plt

def simulate_dice_rolls(num_rolls):
    return [random.randint(1, 6) for _ in range(num_rolls)]

def count_results(rolls):
    counts = {i: 0 for i in range(1, 7)}
    for roll in rolls:
        counts[roll] += 1
    return counts

def plot_distribution(counts):
    sides = list(counts.keys())
    values = list(counts.values())

    plt.bar(sides, values, color='skyblue')
    plt.xlabel("Dice Face")
    plt.ylabel("Frequency")
    plt.title("Dice Roll Distribution (1000 Rolls)")
    plt.xticks(sides)
    plt.grid(True, axis='y')
    plt.show()

def main():
    rolls = simulate_dice_rolls(1000)
    results = count_results(rolls)

    for face, count in results.items():
        print(f"Face {face}: {count} times")

    plot_distribution(results)

if __name__ == "__main__":
    main()
