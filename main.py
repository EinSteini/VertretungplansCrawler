import urllib.request
import datetime

urlToCheck = []

# --Making a list with all forms in school--
site = urllib.request.urlopen('https://gymnasium-remigianum.net/webuntis/frames/navbar.htm')
srcnav = site.read()
split = (str(srcnav).split('var classes = ["')[1]).split('"];')[0]
forms = split.split('","')

# --Getting the current week dates--
weeknumber = datetime.datetime.today().isocalendar()[1]
weekday = datetime.datetime.today().weekday()

url = "https://gymnasium-remigianum.net/webuntis/"+str(weeknumber)+"/w/w00001.htm"
site = urllib.request.urlopen(url)
src = site.read()

tbl = str(src).split('<a name="') #Split source code into days

try:
    affectedForms = tbl[weekday+1].split('Betroffene Klassen&nbsp;</td><td align="left">')[1].split('</td></tr>')[0].split(', ') #Get the affected Forms
    for i in range(len(affectedForms)):
        urlToCheck.append("https://gymnasium-remigianum.net/webuntis/"+str(weeknumber)+"/w/w000"+str(forms.index(affectedForms[i])+1).zfill(2)+".htm")



except IndexError:
    print("Die Vertretungen für diesen Tag sind noch nicht freigegeben")

