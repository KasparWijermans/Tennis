#%% Import statements
from os import name
from tkinter import *
from tkinter import ttk
import Tennis
import toernooi
import csv

#%% Speler import
AlleSpelers = []
with open('Map1.csv') as csvfile:
    ReadCSV = csv.reader(csvfile, delimiter=';')
    for row in ReadCSV:
        AlleSpelers.append(Tennis.Speler(row[0],row[1],row[2],row[3],row[4]))

ActiveSpelers = []


#%% Create basic frame and tabs
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

#%% Spelers tabblad invullen
'''spelers kiezen tabblad'''

def activateSpeler():
    def fun(i):
        for speler in AlleSpelers:
            if spelerlijst.get(i) == speler.name:
                return speler
    temp = spelerlijst.curselection()
    for i in temp:
        selectedspelerslijst.insert(i, spelerlijst.get(i))
        ActiveSpelers.append(fun(i))
    for i in temp:
        spelerlijst.delete(i)
    

def deactivateSpeler():
    def fun(i):
        for speler in AlleSpelers:
            if spelerlijst.get(i) == speler.name:
                return speler
    temp = selectedspelerslijst.curselection()
    for i in temp:
        spelerlijst.insert(i, selectedspelerslijst.get(i))
        ActiveSpelers.remove(fun(i))
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


''' Spelers wijzigen tabblad'''
selected = AlleSpelers[0]
def updateWijzigSpelersTab(var):
    for speler in AlleSpelers:
        if speler.name == var:
            selected = speler
            break
    FHfield.set(str(selected.forehand))
    BHfield.set(str(selected.backhand))
    SVfield.set(str(selected.service))
    STfield.set(str(selected.stamina))

def savePlayerStats():
    def fitNumber(number):
        if number < 1:
            return 1
        elif number > 10:
            return 10
        else:
            return number

    for speler in AlleSpelers:
        if speler.name == variable.get():
            selected = speler
            break
    selected.forehand = fitNumber(int(FHfield.get()))
    selected.backhand = fitNumber(int(BHfield.get()))
    selected.service  = fitNumber(int(SVfield.get()))
    selected.stamina  = fitNumber(int(STfield.get()))



OptionList = [

] 

for i in AlleSpelers:
    OptionList.append(i.name)

variable = StringVar()
variable.set(OptionList[0])

opt = OptionMenu(tab3, variable, *OptionList, command=updateWijzigSpelersTab)
opt.config(width=90, font=('Times New Roman', 12))
opt.pack()


FHLabel = Label(tab3, text="Forehand")
FHLabel.pack()
FHfield = StringVar()
FHfield.set(str(selected.forehand))
FHText = Entry(tab3, textvariable=FHfield)
FHText.pack()
BHLabel = Label(tab3, text= "Backhandhand" ,)
BHLabel.pack()
BHfield = StringVar()
BHfield.set(str(selected.backhand))
BHText = Entry(tab3, textvariable=BHfield)
BHText.pack()
SLabel = Label(tab3, text= "Service" ,)
SLabel.pack()
SVfield = StringVar()
SVfield.set(str(selected.service))
SVText = Entry(tab3, textvariable=SVfield)
SVText.pack()
STLabel = Label(tab3, text= "Stamina" ,)
STLabel.pack()
STfield = StringVar()
STfield.set(str(selected.stamina))
STText = Entry(tab3, textvariable=STfield)
STText.pack()

buttonSavePlayerChanges = Button(tab3, text = "Save", command= savePlayerStats)
buttonSavePlayerChanges.pack(padx = 50, pady = 20)



''' Toernooi spelen tabblad'''

def StartToernooi():
    p2 = [2]
    while p2[-1]*2 <= len(AlleSpelers):
        p2.append(p2[-1]*2)

    if len(ActiveSpelers) in p2:
        ToernooiOutput.delete('1.0', END)
        toernooi.Toernooi(ActiveSpelers)
    else:
        ToernooiOutput.delete('1.0', END)
        print("Selected players: " + str(len(ActiveSpelers)))
        print("Number of selected players must be a power of two")

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


#%%Settings tabblad logica
'''Settings tabblad'''

def updateSettings():
    Tennis.MatchOutput = settingMatchOutput.get()
    Tennis.PointOutput = settingPointOutput.get()
    Tennis.GameOutput = settingGameOutput.get()
    Tennis.SetOutput = settingSetOutput.get()
    Tennis.TiebreakOutput = settingTiebreakOutput.get()
    Tennis.TiebreakRule = settingTiebreakRule.get()
    
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

Label(tabSettings, text='grandslam regelset').grid(row=5)
values = {"US Open" : "1", 
        "Australian Open" : "2", 
        "Wimbledon" : "3", 
        "Roland Garros" : "0"} 

settingTiebreakRule = IntVar(value=Tennis.TiebreakRule)

for (text, value) in values.items(): 
    Radiobutton(tabSettings, text = text, variable = settingTiebreakRule, 
        value = value, command=updateSettings).grid() 

#%% Actually run everything
'''Run GUI'''
root.title("Tennis")
root.mainloop()

