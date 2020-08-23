import urllib.request
import datetime
import os
from shutil import copyfile
import csv

# Variables for developing
weekoffset = 1
dayoffset = -5

urlToCheck = []
vtrList = []
basic = os.listdir("./data/basic/")

# --Making a list with all forms in school--
site = urllib.request.urlopen('https://gymnasium-remigianum.net/webuntis/frames/navbar.htm').read()
forms = (str(site).split('var classes = ["')[1]).split('"];')[0].split('","')

# --Getting the current week dates--
weeknumber = datetime.datetime.today().isocalendar()[1]
weekday = datetime.datetime.today().weekday()
date = str(datetime.datetime.today()).split('-')

url = "https://gymnasium-remigianum.net/webuntis/"+str(weeknumber+weekoffset)+"/w/w00001.htm"
src = urllib.request.urlopen(url).read()

tbl = str(src).split('<a name="') #Split source code into days

if True:
    affectedForms = []
    for form in forms:
        if '<th class="list' in tbl[weekday+1+dayoffset]:
            affectedForms.append(form)
    print(affectedForms)

    for i in range(len(affectedForms)):
        urlToCheck.append("https://gymnasium-remigianum.net/webuntis/"+str(weeknumber+weekoffset)+"/w/w000"+str(forms.index(affectedForms[i])+1).zfill(2)+".htm")

    for url in urlToCheck:
        src = urllib.request.urlopen(url).read()
        currentDay = str(src).split('<a name="')[weekday+1-dayoffset]
        vertretungen = currentDay.split('<th class="list" align="center">Raum</th><th class="list" align="center">Text</th><th class="list" align="center">(Raum)</th></tr>')[1].split("<tr class='list")

        for i in range(len(vertretungen)):
            vtrList.append(vertretungen[i].split(' >'))
            for j in range(len(vtrList)):
                for k in range(len(vtrList[j])):
                    vtrList[j][k] = vtrList[j][k].split('</td')[0]


url = "https://www.nrw-ferien.de/nrw-ferien-"+date[0]+".html"
holidayStart = str(urllib.request.urlopen(url).read()).split("title='Sommerferien 2020 in Nordrhein-Westfalen' hreflang='de-de'>Sommerferien</a></h3><p class='f_datum'>")[1].split("-")[0].split(" ")[1].split(".")

if int(date[1]) <= int(holidayStart[1]) and int(date[2].split(' ')[0]) <= int(holidayStart[0]):
    scndHalf = True
else:
    scndHalf = False

if not os.path.exists("./data/" + str(int(date[0])-int(scndHalf)) + "_" + str(int(date[0])-int(scndHalf)+1)):
    os.makedirs("./data/" + str(int(date[0])-int(scndHalf)) + "_" + str(int(date[0])-int(scndHalf)+1))
    for file in basic:
        copyfile("./data/basic/"+file, "./data/"+str(int(date[0])-int(scndHalf)) + "_" + str(int(date[0])-int(scndHalf)+1)+"/"+file)


# with open('data.csv', encoding='utf8') as csv_file:
#     data = csv.DictReader(csv_file)
#     for dat in data:
#         print(dat)
