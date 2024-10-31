kop=0
vid=0
skaits=0
with open("products.json","r") as file:
    data=json.load(file)

    for i in data:
        kop+= i["price"]
        skaits += 1

vid=kop/ skaits

print(f"videjais ir {vid}") 