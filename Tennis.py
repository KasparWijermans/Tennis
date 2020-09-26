import random 
import configparser
config = configparser.ConfigParser()
config.read('Settings.ini')
#ja doeiiii
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

class set:
    def __init__(self, player1, player2):
        self.players = (player1, player2)
        self.game = []
        self.score = [0, 0]
        self.winner = self.playSet()
    
    def playSet(self):
        while not self.isDecided():
            self.game.append(game(self.players[len(self.game) % 2], self.players[(len(self.game) + 1) % 2 ]))
            if self.game[-1].winner == self.players[0]:
                self.score[0] = self.score[0] + 1 
            else:
                self.score[1] = self.score[1] + 1
            print("Setscore:")
            print(self.score)
        return self.game[-1].winner


    def isDecided(self):
        if self.score[0] > 5 and self.score[0] > self.score[1]+1:
            return True
        elif self.score[1] > 5 and self.score[1] > self.score[0]+1:
            return True
        else:
            return False


print(set(Federer,Nadal).winner.name)
