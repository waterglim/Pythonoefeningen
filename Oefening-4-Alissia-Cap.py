### Zoek de naam van de leerling met de hoogste score, toon dit resultaat. 
### scores = {Alice:85,"Bob":92,"Charlie":88,"diana":95}

scores = {"Alice":85,"Bob":92,"Charlie":88,"diana":95}
names = []
score = []
highestscore = ""


for x in scores.values():
    score.append(x)
for x in scores.keys():
    names.append(x)

score.sort()
highestscore = score.pop()
namehighestscore = scores.get(highestscore)

print(namehighestscore)




