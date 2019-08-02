# a dictionay of hero
hero = {
    "name": "saitama",
    "age": 25,
    "email": "saitama@yahoo.com",
    "purchase": [
        "bannana",
        "apple",
        "pai"
    ]
}
# we print the hero name
print(hero["name"])
# we print the entire hero dictionary
print(hero)
# we change the hero name to 'master saitama'
hero["name"] = "master saitama"
# we now print the hero name; it's now changed
print(hero["name"])
# we loop through the dictionary hero to get its key and value
for key, value in hero.items():
    print(key + " : " + str(value))
