dati = ["Pirmais ieraksts","Otrais ieraksts","Trešais ieraksts"]
vards=[]
with open("drip.txt","w",encoding="utf-8") as fail:
    for ieraksts in dati:
        fail.write(ieraksts + "\n")
    
    #fail.write(input("Ievadit savu vārdu:" + "\n"))
    
edieni=["Kartošhecka","Makarončiki","Peļmešķi"]
with open("edieni.txt","w",encoding="utf-8") as fail:
    for ediens in edieni:
        fail.write(ediens + "\n")

'''gramata=input("ievadiet Gramatu: ")
autors=input("Ievadiet Autoru: ")
izdosanas_gads=input("Ievadiet Izdosanas gadu: ")

gram=[gramata ,autors ,str(izdosanas_gads)]'''
with open("gramatas.txt","a",encoding="utf-8") as fail:
    while True:
        jautajums=input('Vai vēlāties ierakstīt vēl vienu grāmatu? (jā / nē) ')
        if jautajums=="jā":
            gramata=input("Ievadi GRAMATU: ") 
            autors=input("Īevadiet AUTORU: ")
            gads_izdosanas=input("Ievadiet IZDOSANAS GADU: ")
            fail.write(f"Grāmatas nosaukums: {gramata} Autors: {autors} Izdošanas gads {gads_izdosanas}"+"\n")
        else:
            print('Paldies!')
            break 
with open("gramatas.txt","r",encoding="utf-8") as fail:
    for rinda in fail:
        print(rinda.strip())