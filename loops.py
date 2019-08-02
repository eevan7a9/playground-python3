# for loop
heroes = ["saitama", "genos", "tatsumaki", "bang"]
# loop through the lists of heroes
for hero in heroes:
    print(hero)

# we create a lists of number from 1 to 10
number_lists = list(range(1, 11))
#  5 is how we increment it
number_lists2 = list(range(0, 11, 5))
print(number_lists)
print(number_lists2)
# we create a list that will run 6 times
for i in range(0, 6):
    print("hello")
name = "saitama"
# we can loop through name per character
for i in name:
    print(i)

# while loop
score = 0
score_needed = 10
# as long as score is less than or equal to score_needed
while score < score_needed:
    score += 1
    # if score and score_needed is equal break
    if score == score_needed:
        print(str(score) + " I am big enough")
    else:
        print(str(score) + " I am still too small")
