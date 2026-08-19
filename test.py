import json
f = open("gameRiddles.json","r")
riddles = json.load(f)
for item in riddles:
    for key, value in item.items():
        print(f"{key}: {value}")