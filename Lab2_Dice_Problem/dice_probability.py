def calculate_probability(target_number, total_sides=6):
    if 1 <= target_number <= total_sides:
        probability = 1 / total_sides
        return probability
    else:
        return 0
    
def main():
    sides = 6
    target = 6
    prob = calculate_probability(target, sides) 
    print (f"Probability of rolling a {target} on a {sides}-sided dice: {prob:.2f}")
    
    
    #Bonus: probability of rolling an even number
    even_count = len([n for n in range(1, sides + 1) if n % 2 == 0])
    even_probability = even_count / sides
    print(f"Probability of rolling an even number is: {even_probability:.2f}")

if __name__ == "__main__":
    main()
    
        