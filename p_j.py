import json

with open("people.json","r") as file:
    people=json.load(file)

print("Cilvēki vecāki par 30 gadiem:")
for person in people:
    if person["age"] > 30:
        print(person["name"])
