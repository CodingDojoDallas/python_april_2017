name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def making_dicts(keys, values):
    dictionary = dict(zip(keys, values))
    print(dictionary)
making_dicts(name, favorite_animal)
