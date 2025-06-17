



def singulars_and_plurals(words):
    singulars = []
    plurals = []

    for word in words:
        if word.endswith("s"):
            plurals.append(word)
        else:
            singulars.append(word)

    return {
        "singulars": singulars,
        "plurals": plurals
    }


print(singulars_and_plurals(["tomato", "tomatoes", "potato", "potatoes", "cars", "unicorns", "horse", "cow"]))


