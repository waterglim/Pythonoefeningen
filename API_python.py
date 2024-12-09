
import requests

### URL
api_url = "https://jsonplaceholder.typicode.com/todos/1"

### GET (URL)
response = requests.get(api_url)

### De gegevens in JSON formaat zetten. (en printen om te bekijken)
#print(response.json())

### De return code of status code van respons (200 == geslaagd)
#print(response.status_code)

### Geeft het type header terug.
#print(response.headers["Content-Type"])




##### Maak GET-verzoek naar https://jsonplaceholder.typicode.com/todos/1
##### Decodeer de JSON-reactie
##### Toon de titel van de taak in de console
##### 

#decode = response.json()
#print("De titel is : " + decode["title"])



#if decode["completed"] == False : 
#    print("Er moet nog werk worden gedaan")
#else :
#    print("Goed gedaan!")



### Doel : Haal COVID-19 statistieken op voor een specifiek land
### Gebruik de disease.sh API voor COVID-19 gegevens
### Vraag de gebruiker om een land in te voeren (bvb : "Netherlands")
### Maak een GET-verzoek naar het endpoint
### https://disease.sh/v3/covid-19/countries/<land>
### Toon de volgende statistieken:
    ### Totaal aantal gevallen
    ### Totaal aantal sterfgevallen
    ### Aantal herstelde patienten


barecovidurl = "https://disease.sh/v3/covid-19/countries"

newinput = input("Geef een land in aub (engelse naamgeving) : \n")
land = str(newinput)

covidurl = barecovidurl + "/" + newinput
covidresponse =  requests.get(covidurl)
covidinfo = covidresponse.json()

cases = "{:,.2f}".format(covidinfo["cases"])
deaths = "{:,.2f}".format(covidinfo["deaths"])
recovered = "{:,.2f}".format(covidinfo["recovered"])

print("Cases reported in " + land + " : " + str(cases))
print("Deaths reported in " + land + " : " + str(deaths))
print("Recovered patients reported in " + land + " : " + str(recovered))












