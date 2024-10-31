import json

data={
    "name":"Anna",
    "age":25,
    "city":"Riga"
}

with open("data.json","w",encoding='utf-8') as file:
    json.dump(data,file,indent=4)

print(f'Name:',data["name"])


people=[{
    {"name":"Janis","age":30,"city":"Riga"},
   {"name":"Anna","age":25,"city":"Jelgava"},
    {"name":"Peteris","age":40,"city":"Liepaja"}
}]

with open("people.json","w",encoding='utf-8') as file:
    json.dump(data,file,indent=4)