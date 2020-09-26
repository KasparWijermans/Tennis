import random 
import configparser
config = configparser.ConfigParser()
config.read('Settings.ini')

servicewinrate = float(config['TENNIS']['ServiceWinrate'])


class Speler:
    def __init__ (self, name, forehand, backhand, service, stamina):
        self.name = name
        self.forehand = int(forehand)
        self.backhand = int(backhand)
        self.service = int(service)
        self.stamina = int(stamina)


Nadal = Speler("Rafael", 10, 7, 8, 9)
Federer = Speler("Roger", 8, 9, 9, 8)


class rally: 
    def __init__(self, server, receiver):
        #self.server = server
        #self.receiver = receiver
        if ((0.03*(server.service - (receiver.forehand + receiver.backhand)/2)) + servicewinrate) > random.random():
            self.winner = server
        else:
            self.winner = receiver
        
#exhaustion = stamina - rally_num  


class game:
    def __init__(self, server, receiver):
        self.server = server
        self.receiver = receiver
        self.rally = []
        self.score =[0,0]                   
        self.winner = self.playGame()

    def playGame(self):
        while  not self.isDecided():
            self.rally.append(rally(self.server, self.receiver))
            if self.rally[-1].winner == self.server:
                self.score[0] = self.score[0] + 1 
            else:
                self.score[1] = self.score[1] + 1
            print(self.score)
        return self.rally[-1].winner

    def isDecided(self):
        if self.score[0] > 3 and self.score[0] > self.score[1]+1:
            return True
        elif self.score[1] > 3 and self.score[1] > self.score[0]+1:
            return True
        else:
            return False



print(game(Federer,Nadal).winner.name)
