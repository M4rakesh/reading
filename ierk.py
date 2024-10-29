#Ierakstīšāna
with open("vardi.txt","a",encoding="utf-8") as fail:
    while True:
        vards=input("Ievadiet vārdu(ievadiet'beigt',lai pabeigtu):")
        if vards.lower() == 'beigt':
            break
        fail.write(vards + "\n")

#lasīšāna
print("\nIevadiet vārdi: ")
with open("vardi.txt","r",encoding="utf-8") as fail:
    for rinda in fail:
        print(rinda.strip())

