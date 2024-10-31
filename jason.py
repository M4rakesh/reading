import json

data={
    "name":"Anna",
    "age":25,
    "city":"Riga"
}

with open("data.json","w",encoding='utf-8') as file:
    json.dump(data,file,indent=4)

print(f'Name:',data["name"])



with open("people.json","w",encoding='utf-8') as file:
    json.dump(data,file,indent=4)