import random

# Initial list of words for the game
initial_words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]

# Function to play best-of-3 rock-paper-scissors
def rps():
    options = ["rock", "paper", "scissors"]
    player_wins = 0
    ai_wins = 0
    
    while player_wins < 2 and ai_wins < 2:
        ai_choice = random.choice(options)
        player_choice = input("Choose rock, paper, or scissors: ").lower()
        
        if player_choice == ai_choice:
            print("Tie! No points awarded.")
        elif (player_choice == "rock" and ai_choice == "scissors") or \
             (player_choice == "scissors" and ai_choice == "paper") or \
             (player_choice == "paper" and ai_choice == "rock"):
            player_wins += 1
            print(f"You win this round! (Player: {player_wins}, AI: {ai_wins})")
        else:
            ai_wins += 1
            print(f"AI wins this round! (Player: {player_wins}, AI: {ai_wins})")
        
        if player_wins == 1 and ai_wins == 1:
            print("Match point! Next win decides the round.")
    
    if player_wins == 2:
        return "player"
    else:
        return "ai"

# Function to get player's name
def get_player_name():
    return input("Enter your name: ")

# Function to risk tic points
def risk_tic_points(player_tic_points, ai_tic_points):
    player_choice = float(input("Choose a number (up to 10000): "))
    ai_choice = random.uniform(0, 10000)  # AI chooses a random number
    target = random.uniform(0, 10000)
    
    player_diff = abs(player_choice - target)
    ai_diff = abs(ai_choice - target)
    
    print(f"AI chose: {ai_choice}")

    if player_diff < ai_diff:
        print("You were closer to", target, "! You gain 2 tic points.")
        player_tic_points += 2
    else:
        print("AI was closer to", target, "! AI gains 2 tic points and you lose 1 tic point.")
        ai_tic_points += 2
        player_tic_points -= 1 if player_tic_points > 0 else 0

    return player_tic_points, ai_tic_points

# Function to risk regular points with a riddle
def risk_regular_points(player_points, ai_points):
    riddles = [
        ("I turn polar bears white and I will make you cry. "
         "I make guys have to pee and girls comb their hair. "
         "I make celebrities look stupid and normal people look like celebrities. "
         "I turn pancakes brown and make your champagne bubble. "
         "If you squeeze me, I’ll pop. If you look at me, you’ll pop. "
         "Can you guess the riddle?", ["pressure", "time"]),
        ("7 men have 7 wives each man and each wife have 7 children. What is the total number of people?", ["63"])
    ]
    
    riddle, correct_answers = random.choice(riddles)
    answer = input(f"Riddle: {riddle}\nYour answer: ").strip().lower()
    
    if answer in correct_answers:
        print("Correct! You gain 2 points.")
        player_points += 2
    else:
        print("Incorrect. AI gains 2 points and you lose 1 point.")
        ai_points += 2
        player_points -= 1 if player_points > 0 else 0
    
    return player_points, ai_points

# Game variables
player_name = get_player_name()
player_points = 0
ai_points = 0
player_tic_points = 0
ai_tic_points = 0
# Main game loop for 3 rounds
for round_num in range(1, 4):
    print(f"Round {round_num}")

    # Generate a new list of 10 words for each round
    words = random.sample(initial_words, 10)

    ai_word = random.choice(words)
    print("Choose a word from the list:", words)
    player_word = input("Your choice: ").lower()

    if player_word == ai_word:
        player_points += 1
        print("You guessed the same word as the AI! You get a point.")
        if player_points > 0:
            risk_regular_choice = input("Do you want to risk your points? (yes/no): ").lower()
            if risk_regular_choice == "yes":
                player_points, ai_points = risk_regular_points(player_points, ai_points)
        else:
            print("You don't have any points to risk.")
    else:
        ai_points += 1
        print(f"Wrong guess. AI chose '{ai_word}'. AI gets a point.")
        print("Time to play Rock-Paper-Scissors (best of 3) to win a tic point.")
        result = rps()
        
        if result == "player":
            player_tic_points += 1
            print("You won Rock-Paper-Scissors! You get a tic point.")
        else:
            ai_tic_points += 1
            print("AI won Rock-Paper-Scissors! AI gets a tic point.")
    
    # Risk feature for tic points
    if player_tic_points > 0:
        risk_choice = input("Do you want to risk your tic points? (yes/no): ").lower()
        if risk_choice == "yes":
            player_tic_points, ai_tic_points = risk_tic_points(player_tic_points, ai_tic_points)

    # Show score after each round
    print("\nScore after Round", round_num)
    print(f"Player Points: {player_points}")
    print(f"AI Points: {ai_points}")
    print(f"Player Tic Points: {player_tic_points}")
    print(f"AI Tic Points: {ai_tic_points}")
    print("-" * 20)

# Final results
print("\nFinal Results:")
print(f"Player Points: {player_points}")
print(f"AI Points: {ai_points}")
print(f"Player Tic Points: {player_tic_points}")
print(f"AI Tic Points: {ai_tic_points}")

# Determine the winner
if (player_points + player_tic_points) > (ai_points + ai_tic_points):
    print(f"Congratulations, {player_name}! You won the game!")
elif (player_points + player_tic_points) == (ai_points + ai_tic_points):
    print("AI and, {player_name}!, have tied" )
else:
    print("AI won the game. Better luck next time!")

print("We appreciate you taking the time to play our game. ")

