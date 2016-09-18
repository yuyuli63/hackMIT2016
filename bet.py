class bet:
    count = 0

    def __init__(self, text, company, amount, proposer):
        count += 1
        self.ID = count
        self.txt = text
        self.co = company
        self.amt = amount
        self.prop = proposer
        self.accept = None
        self.win = 0

    def getID(self):
        return self.ID

    def setID(self, ID):
        self.ID = ID

    def getText(self):
        return self.txt

    def setText(self, text):
        self.txt = txt

    def getCompany(self):
        return self.co

    def setCompany(self, company):
        self.co = company

    def getAmount(self):
        return self.amt

    def setAmount(self, amount):
        self.amt = amt

    def getProposer(self):
        return self.prop

    def setProposer(self, proposer):
        self.prop = proposer

    def getAcceptor(self):
        return self.accept

    def setAcceptor(self, acceptor):
        self.accept = acceptor

    def getWin(self):
        return self.win

    def setWin(self, win):
        self.win = win

    def __str__(self):
        x = "******************************\n"
        x += "Bet ID: " + self.ID
        x += self.txt
        x += "\nCompany: " + self.co
        x += "\nAmount: $" + str(self.amt)
        x += "\nProposed by: " + self.prop
        x += "\nAccepted by: " + self.acceptString()
        x += "\nOutcome: " + self.outcomeString()
        x += "\n******************************"

        return x

    def acceptString(self):
        if self.accept == None:
            return "No one has yet accepted this bet"
        else:
            return self.accept

    def outcomeString(self):
        if self.win == 1:
            return (self.prop + " wins $" + str(self.amt))
        elif self.win == -1:
            return (self.accept + " wins $" + str(self.amt))
        else:
            return "No outcome"

def main():
    x = bet("I bet that Yuyu will grow a mustache", "Yuyu, Inc", 500, "kmorris")
    x.setAcceptor("yli")
    #print x.__str__()
    x.setWin(1)
    print x.__str__()

main()
