
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


#barecovidurl = "https://disease.sh/v3/covid-19/countries"

#newinput = input("Geef een land in aub (engelse naamgeving) : \n")
#land = str(newinput)

#covidurl = barecovidurl + "/" + newinput
#covidresponse =  requests.get(covidurl)
#covidinfo = covidresponse.json()

#cases = "{:,.2f}".format(covidinfo["cases"])
#deaths = "{:,.2f}".format(covidinfo["deaths"])
#recovered = "{:,.2f}".format(covidinfo["recovered"])

#print("Cases reported in " + land + " : " + str(cases))
#print("Deaths reported in " + land + " : " + str(deaths))
#print("Recovered patients reported in " + land + " : " + str(recovered))




### Doel : Haal een  mop op via API en toon deze.
### zoek een API die willekeurig moppen levert (bijv. jokeapi)
### maak een script dat een mop ophaalt en weergeeft
### Voeg een loop toe zodat de gebruiker meerdere moppen kan ophalen.


#amountofjokes = input("Hoeveel moppen wil je zien? \n")
#x = 0

#while int(amountofjokes) > x:
#    jokesurl = "https://v2.jokeapi.dev/joke/Any" 
#    jokes = requests.get(jokesurl)
#    jokes = jokes.json()

#    try: 
#        setup = jokes["setup"]
#    except: 
#        setup = ""

#    try:
#        delivery = jokes["delivery"]
#    except:
#        delivery = ""
#        
#    print(setup +"\n" + delivery +"\n")
#    x+=1



#hardswareurl = "http://localhost:8085/data.json"

#hardwarejson = requests.get(hardswareurl)
#hardwarejson = hardwarejson.json()

#print(hardwarejson)





### https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric
### je hebt een gratis API sleutel nodig, registreren op OpenWeatherMap-website
### Vraag de gebruiker om een sta in te voeren (vb : Amsterdam)
### Maak een get-verzoek naar de openweathermap API
###  Haal de volgnede gegevens op en toon ze:
### temp in C, Weerbeschrijving, vochtigheid%, windsnelheid (km/h)


APIkey = "08c9fe4800ecffe9e0af86c9836f5c6c"
cityinput = input("Voeg in het engels een stad in: \n")

#weatherurl = "https://api.openweathermap.org/data/2.5/weather?q=" + str(cityinput) + "&appid=" + str(APIkey) + "&units=metric"
weatherurl2 = "https://api.openweathermap.org/data/2.5/weather?q=" + cityinput + "&appid=" + APIkey + "&units=metric"

print(weatherurl2)

weather = requests.get(weatherurl2)
weatherjson = weather.json()

temp = weatherjson["main"]["temp"]
weatherdis = weatherjson["weather"][0]["description"]
humidity = weatherjson["main"]["humidity"]
buffor = weatherjson["wind"]["speed"]

print(temp)
print(weatherdis)
print(humidity)
print(buffor)


















