#  we declare to create a lists of Hero
heroes = ["saitama", "genos", "tatsumaki", "bang"]

print(heroes)  # print all heroes
# we print the 3rd hero of the lists (remember count starts at 0)
print(heroes[2])  # expected: tatsumaki
# we print heroes from first to third
print(heroes[0:3])  # expected: ["saitama", "genos", "tatsumaki"]
#  we get the last hero
print(heroes[-1])  # expected: bang
# we get the 2nd hero to the last hero
print(heroes[1:])  # expected : ['genos', 'tatsumaki', 'bang']

# Unpacking: assigning each heroes to individual variable
saitama, genos, tatsumaki, bang = heroes
# we get saitama and assign remaining heroes to other_heroes
saitama, *other_heroes = heroes
print(saitama, genos, tatsumaki, bang)
print(other_heroes)

# add new Heroes to our heroes lists

# we added new hero king to lists heroes
heroes.append("king")  # king will be added in the last index
print(heroes[-1])
# we added new hero atomic samurai in the 2nd index or 2nd item
heroes.insert(1, "atomic samurai")  # remember count starts at 0, 1 = 2nd index
print(heroes)
#  we get the index of bang
print(heroes.index("bang"))
# we remove heroes
heroes.pop()  # default is to remove the last heroes/item
print(heroes)  # king is removed

# we create new lists neo_heroes
neo_heroes = ["child emperor", "bomb"]
# we combine hereos lists with neo heroes lists
heroes.extend(neo_heroes)
# expected: ['saitama', 'atomic samurai', 'genos', 'tatsumaki', 'bang', 'child emperor', 'bomb']
print(heroes)

#  lists like:
fruits = ("bannana", "apple", "orange")
# fruits is a Tuples much alike lists but are immutable
# cannot be edited
print(fruits)
# drinks is a Set much like a lists but no items are alike
drinks = {"soda", "coffee", "milk"}
drinks.add("wine")  # this will be added
drinks.add("soda")  # this will not be added; soda already exists
print(drinks)
