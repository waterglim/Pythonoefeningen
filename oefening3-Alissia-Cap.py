### Maak een leeg woordenboek genaamd telefoonboek. 
### Zorg ervoor dat gebruikers hiermee kunnen interageren.  
### Werk dit uit naar jou kunnen en kennen. 
### Dit is een vrije oefening, deze vul je in zoals je wil en kan.  

## from random import randint
## telefoonnummerdeel = randint(10000000,99999999)
    

telefoonboek = {"Kevin":"03 250 99 60","Olivier":"03 270 30 71","Doris":"02 150 22 57","Collin":"03 375 80 65"}
numbers = []
names = []
index = 0

print("Beste, welcome bij het online telefoonboek, om het boek in te kijken, type T.\nOm een persoon te zoeken, type hun naam.\nOm een telefoonnummer te zoeken, type het nummer.")
userinput = input()
searchname = False

if telefoonboek.get(userinput,"None") != "None":
    searchname = True

if userinput == "T":
    for i in telefoonboek.keys() : 
        names.append(i)
    for j in telefoonboek.values() :
        numbers.append(j)
    for i in telefoonboek:
        tempvalue = names[index]
        tempnumb = numbers[index]
        index += 1 
        print(tempvalue + " | " + tempnumb)

elif searchname == True:
    search = telefoonboek.get(userinput,"Not found")
    print(search)



### toon telefoonboek  OK
### zoek op naam       OK
### zoek op nummer     NOK





