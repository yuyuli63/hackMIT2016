class active_bets:
    def __init__(self):
        self.list = []

    def getList(self):
        return self.list

    def setList(self, list):
        self.list = list

    def addBet(self, bet):
        self.list.append(bet)

    def removeBet(self, bet):
        self.list.remove(bet)

    def getCount(self):
        return self.list.count()
