import Tennis
import csv

def Toernooi():
    spelers = []

    with open('Map1.csv') as csvfile:
        ReadCSV = csv.reader(csvfile, delimiter=';')
        for row in ReadCSV:
            spelers.append(Tennis.Speler(row[0],row[1],row[2],row[3],row[4]))


    result = spelers
    ronde = 1

    while len(result) > 1:
        temp = []
        print("ronde: " + str(ronde))
        for i in range(int(len(result)/2)):
            print((result[2*i]).name + " versus " + (result[2*i+1]).name)
            temp.append(Tennis.match(result[2*i],result[2*i+1],3).winner)
        ronde+=1
        result = temp

    print("The tournament winner is: " + result[0].name)

#Toernooi()