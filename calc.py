import random

def insult_calculator():
    print("Welcome to the PyJoke Calculator!")
    print("Enter your math problem (e.g., 2 + 2) or 'quit' to exit:")
    
    insults = [
        "Even my mentally challanged grandma could solve this, and she's dead.",
        "If brains were dynamite, you wouldn't have enough to blow your nose.",
        "I've seen smarter potatoes than you.",
        "Your math skills make a banana look like a genius.",
        "Did you get your math license from a cereal box?",
        "I'd explain this to you but I don't have any crayons handy.",
        "You couldn't count to 21 even with your shoes off.",
        "The only thing you're calculating is how to disappoint your parents.",
        "I've seen more mathematical ability in a broken abacus.",
        "Your brain is smoother than a polished marble."
    ]
    
    while True:
        user_input = input("\n> ")
        
        if user_input.lower() == 'quit':
            print("Thank goodness, my circuits were starting to atrophy from your simple problems.")
            break
            
        try:
            # Parse the input
            parts = user_input.split()
            if len(parts) != 3:
                raise ValueError("Invalid format")
                
            num1 = float(parts[0])
            operator = parts[1]
            num2 = float(parts[2])
            
            # Perform calculation
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    print("Trying to divide by zero? Your mathematical genius knows no bounds!")
                    continue
                result = num1 / num2
            else:
                print("I don't recognize that operator. Did you make it up yourself? Typical.")
                continue
                
            # Instead of showing the result, insult the user
            print(f"{random.choice(insults)}")
            
        except:
            print("Even entering numbers properly is too complex for you, isn't it?")

if __name__ == "__main__":
    insult_calculator()
