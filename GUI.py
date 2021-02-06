from tkinter import *
from tkinter import ttk
import Tennis
import toernooi
import csv


AlleSpelers = []
with open('Map1.csv') as csvfile:
    ReadCSV = csv.reader(csvfile, delimiter=';')
    for row in ReadCSV:
        AlleSpelers.append(Tennis.Speler(row[0],row[1],row[2],row[3],row[4]))

root = Tk()
tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)
tabSettings = ttk.Frame(tabControl)
tabControl.add(tab1, text= "Speler toevoegen")
tabControl.add(tab2, text= "Speler lijst")
tabControl.add(tab3, text= "Speler wijzigen")
tabControl.add(tab4, text= "Toernooi spelen")
tabControl.add(tabSettings, text = "Settings")
tabControl.pack(expand=1, fill="both")
root.geometry("800x600")


'''spelers kiezen tabblad'''


def activateSpeler():
    temp = spelerlijst.curselection()
    for i in temp:
        selectedspelerslijst.insert(i, spelerlijst.get(i))
    for i in temp:
        spelerlijst.delete(i)

def deactivateSpeler():
    temp = selectedspelerslijst.curselection()
    for i in temp:
        spelerlijst.insert(i, selectedspelerslijst.get(i))
    for i in temp:
        selectedspelerslijst.delete(i)

spelerlijst = Listbox(tab2)
i=0
for i in range(len(AlleSpelers)):
    spelerlijst.insert(i+1, AlleSpelers[i].name)

spelerlijst.pack(expand = 1, fill ="y", side=LEFT)

selectedspelerslijst = Listbox(tab2)
selectedspelerslijst.pack(expand = 1, fill ="y", side=RIGHT)
tab2middleframe = Frame(tab2)
tab2middleframe.pack(expand=1)
kiesspeler = Button(tab2middleframe, command=activateSpeler, text=">>")
kiesspeler.pack()
stopspeler = Button(tab2middleframe, command=deactivateSpeler, text="<<")
stopspeler.pack()


''' Toernooi spelen tabblad'''

def StartToernooi():
    ToernooiOutput.delete('1.0', END)
    toernooi.Toernooi()

button4 = Button(tab4, text = "Start toernooi", command= StartToernooi)
button4.pack(padx = 50, pady = 20)

scroll_bar = Scrollbar(tab4)
scroll_bar.pack( side = RIGHT, 
                fill = Y, padx=0 )
ToernooiOutput = Text(tab4, yscrollcommand = scroll_bar.set)
ToernooiOutput.pack(side = LEFT, padx = 20)

def redirector(inputStr):
    ToernooiOutput.insert(INSERT, inputStr)

sys.stdout.write = redirector #whenever sys.stdout.write is called, redirector is called.

scroll_bar.config( command = ToernooiOutput.yview)

'''Settings tabblad'''

def updateSettings():
    Tennis.MatchOutput = settingMatchOutput.get()
    Tennis.PointOutput = settingPointOutput.get()
    Tennis.GameOutput = settingGameOutput.get()
    Tennis.SetOutput = settingSetOutput.get()
    Tennis.TiebreakOutput = settingTiebreakOutput.get()
    
# point game set tiebreak match, score weergeven

settingPointOutput = IntVar(value=Tennis.PointOutput)
Checkbutton(tabSettings, text="point", variable=settingPointOutput, command=updateSettings).grid(row=0, sticky=W)
settingGameOutput = IntVar(value=Tennis.GameOutput)
Checkbutton(tabSettings, text="game", variable=settingGameOutput, command=updateSettings).grid(row=1, sticky=W)
settingSetOutput = IntVar(value=Tennis.SetOutput)
Checkbutton(tabSettings, text="set", variable=settingSetOutput, command=updateSettings).grid(row=2, sticky=W)
settingTiebreakOutput = IntVar(value=Tennis.TiebreakOutput)
Checkbutton(tabSettings, text="tiebreak", variable=settingTiebreakOutput, command=updateSettings).grid(row=3, sticky=W)
settingMatchOutput = IntVar(value=Tennis.MatchOutput)
Checkbutton(tabSettings, text="match", variable=settingMatchOutput, command=updateSettings).grid(row=4, sticky=W)


'''Run GUI'''
root.title("Tennis")
root.mainloop()

