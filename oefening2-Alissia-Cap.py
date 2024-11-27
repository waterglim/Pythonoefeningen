### Vraag de gebruiker om een reeks cijfers in te voeren, 
### Bepaal: 
### Het hoogste getal 
### Het laagste getal 
### De som van de cijfers 


print("Gelieve enkele cijfers in te geven, 1 per keer.")
a = input("1ste getal : ")
b = input("2de getal : ")
c = input("3rde getal : ")
d = input("4de getal : ")

newlist = [a,b,c,d]
maxi = max(newlist)
mini = min(newlist)
som = float(a)+float(b)+float(c)+float(d)

print(maxi)
print(mini)
print(int(som))







