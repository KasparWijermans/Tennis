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

class rally: 
    def __init__(self, server, receiver):
        if ((0.03*(server.service - (receiver.forehand + receiver.backhand)/2)) + servicewinrate) > random.random():
            self.winner = server
        else:
            self.winner = receiver

class game:
    def __init__(self, server, receiver):
        self.server = server
        self.receiver = receiver
        self.rally = []
        self.score =[0,0]                   
        self.winner = self.playGame()
        print("Game " + self.winner.name)
    
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
    def __init__(self, player1, player2, match):
        self.players = (player1, player2)
        self.match = match
        self.game = []
        self.score = [0, 0]
        self.winner = self.playSet()
        print("Set: " + self.winner.name)
    
    def playSet(self):
        while not self.isDecided():
            self.game.append(game(self.players[self.match.gamenumber % 2], self.players[(self.match.gamenumber + 1) % 2 ]))
            self.match.gamenumber += 1
            self.scoring()
        return self.game[-1].winner

    def scoring(self):
        if self.game[-1].winner == self.players[0]:
            self.score[0] = self.score[0] + 1 
        else:
            self.score[1] = self.score[1] + 1
        print("Setscore:" + str(self.score))
    
    def isDecided(self):
        if self.score == [6, 6]:
            print("Tiebreaker:")
            self.game.append(tiebreak(self.players[self.match.gamenumber % 2], self.players[(self.match.gamenumber + 1) % 2 ], self.match))
            self.scoring()
            return True
        elif self.score[0] > 5 and self.score[0] > self.score[1]+1:
            return True
        elif self.score[1] > 5 and self.score[1] > self.score[0]+1:
            return True
        else:
            return False

class match:
    def __init__(self, player1, player2, setsToWin, tiebreaker):
        self.gamenumber = random.randint(0, 1)
        self.players = (player1, player2)
        self.set = []
        self.score = [0,0]
        self.setsToWin = setsToWin
        self.winner = self.playMatch()
        print("match: " + self.winner.name)
    
    def playMatch(self):
        while not self.isDecided():
            self.set.append(set(self.players[0], self.players[1], self))
            if self.set[-1].winner == self.players[0]:
                self.score[0] = self.score[0] + 1 
            else:
                self.score[1] = self.score[1] + 1
            print("Match score: "+ str(self.score))
        return self.set[-1].winner
    
    def isDecided(self):
        if self.score[0] == self.setsToWin:
            return True
        elif self.score[1] == self.setsToWin:
            return True
        else:
            return False       

class tiebreak:
    def __init__(self, player1, player2, match):
        self.players = (player1, player1, player2, player2)
        self.rallynr = 1
        self.match = match
        self.score = [0,0]
        self.rally = []
        self.winner = self.playTiebreak()
    
    def playTiebreak(self):
        while not self.isDecided():
            self.rally.append(rally(self.players[self.rallynr % 4], self.players[(self.rallynr + 1) % 4 ]))
            self.match.gamenumber += (self.rallynr % 2)
            self.rallynr += 1
            if self.rally[-1].winner == self.players[0]:
                self.score[0] = self.score[0] + 1 
            else:
                self.score[1] = self.score[1] + 1
            print(self.score)
        return self.rally[-1].winner
        # winner == winner set
    
    def isDecided(self):
        if self.score[0] > 6 and self.score[0] > self.score[1]+1:
            return True
        elif self.score[1] > 6 and self.score[1] > self.score[0]+1:
            return True
        else:
            return False



Nadal = Speler("Rafael", 10, 7, 8, 9)
Federer = Speler("Roger", 8, 9, 9, 8)

match(Federer,Nadal, 3, bool(1))
