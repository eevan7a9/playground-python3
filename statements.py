number = 13

if number == 12:
    print(f"you're number {number} is equal to 12")
else:
    print(f"you're number {number} is not equal to 12")

player1_score = 420
player2_score = 320

if player1_score > player2_score:
    print("player1 wins the game")
elif player1_score < player2_score:
    print("player2 wins the game")
else:
    print("its a Draw!!!")

if player2_score > 400 and player1_score > 400:
    print("both teams core over 400")

if player2_score > 400 or player1_score > 400:
    print("one of the players have more than 400 score")
