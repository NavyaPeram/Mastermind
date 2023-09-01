class Game:
    def __init__(self, id):
        self.p1Went = False
        self.p2Went = False
        self.ready = False
        self.id = id
        self.moves = [None, None]
        self.wins = [0,0]
        self.ties = 0

    def get_player_move(self, p):
        """
        :param p: [0,1]
        :return: Move
        """
        return self.moves[p]

    def play(self, player):
        # self.moves[player] = move
        if player == 0:
            self.p1Went = True
        else:
            self.p2Went = True

    def connected(self):
        return self.ready

    def bothWent(self):
        return self.p1Went and self.p2Went

    def resetWent(self):
        self.p1Went = False
        self.p2Went = False

    def winner(self,player,count):
        self.wins[player]=count
        print(self.wins[player])

    def check(self):
        if(self.wins[0]==0 or self.wins[1]==0):
            return 0
        else:
            return 1

    def win(self):
        if(self.wins[0]==5 and self.wins[1]==5):
            return -1
        if(self.wins[0]>self.wins[1]):
            return 0
        elif (self.wins[0]<self.wins[1]):
            return 1
        else:
            return 2