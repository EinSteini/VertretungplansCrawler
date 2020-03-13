import urllib.request
import datetime

urlToCheck = []
vtrList = []

# --Making a list with all forms in school--
site = urllib.request.urlopen('https://gymnasium-remigianum.net/webuntis/frames/navbar.htm').read()
forms = (str(site).split('var classes = ["')[1]).split('"];')[0].split('","')

# --Getting the current week dates--
weeknumber = datetime.datetime.today().isocalendar()[1]
weekday = datetime.datetime.today().weekday()

url = "https://gymnasium-remigianum.net/webuntis/"+str(weeknumber)+"/w/w00001.htm"
src = urllib.request.urlopen(url).read()

tbl = str(src).split('<a name="') #Split source code into days

try:
    affectedForms = tbl[weekday+1].split('Betroffene Klassen&nbsp;</td><td align="left">')[1].split('</td></tr>')[0].split(', ') #Get the affected Forms
    for i in range(len(affectedForms)):
        urlToCheck.append("https://gymnasium-remigianum.net/webuntis/"+str(weeknumber)+"/w/w000"+str(forms.index(affectedForms[i])+1).zfill(2)+".htm")

    for url in urlToCheck:
        src = urllib.request.urlopen(url).read()
        currentDay = str(src).split('<a name="')[weekday + 1]
        vertretungen = currentDay.split(
            '>Klasse(n)</th><th class="list" align="center">Raum</th><th class="list" align="center">Text</th></tr>')[
            1].split("<tr class='list")

        for i in range(len(vertretungen)):
            vtrList.append(vertretungen[i].split(' >'))
            for j in range(len(vtrList)):
                for k in range(len(vtrList[j])):
                    vtrList[j][k] = vtrList[j][k].split('</td')[0]

except IndexError:
    print("Die Vertretungen für diesen Tag sind noch nicht freigegeben")

