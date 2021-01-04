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
tabControl.add(tab1, text= "Speler toevoegen")
tabControl.add(tab2, text= "Speler lijst")
tabControl.add(tab3, text= "Speler wijzigen")
tabControl.add(tab4, text= "Toernooi spelen")
tabControl.pack(expand=1, fill="both")
root.geometry("800x600")

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

def openNewWindow(): 
    newWindow = Toplevel(root) 

    newWindow.title("New Window") 

    newWindow.geometry("200x200") 

    Label(newWindow,  
        text ="Kies je speler").pack() 

button4 = Button(tab4, text = "Start toernooi", command= toernooi.Toernooi)
button4.pack(padx = 50, pady = 50)

root.title("Tennis")
root.mainloop()

