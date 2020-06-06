# Dictionnarie You have key and Variable
# you can also put number in the key

NicknamesConversions = {
    "jit": "Amine jit",
    "stiv": "Stivie jordan",
    "Hamri": "Alex",
    "cbz": "Ilyes Chambaz",
}

# how to reffer to a key and have the actual value of this key
# first method
#exemple

print(NicknamesConversions["jit"])
# Second Method
# you can also the get function to specifies a default value
print(NicknamesConversions.get("jit"))
# you can also specifies what to write when you have a default value
print(NicknamesConversions.get("Ouss", "Valeur négative"))