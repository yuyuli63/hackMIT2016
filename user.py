class User:
	count = 0

	def __init__(self, name, balance):
		User.count += 1
		self.ID = User.count
		self.name = name
		self.balance = balance
		self.bets = []
		self.nums = 0

	def getId(self):
		return self.ID

	def setId(self, idnum):
		self.ID = idnum

	def getName(self):
		return self.name

	def setName(self, name):
		self.name = name

	def getBalance(self):
		return self.balance

	def setBalance(self, balance):
		self.balance = balance

	def getBets(self):
		return self.bets

	def setBets(self, open_bets):
		self.bets = open_bets

	def getNums(self):
		return self.nums

	def setNums(self, bet_count):
		self.nums = bet_count

	#def proposeBet(self):

	#def acceptBet(self, bet):

	def __str__(self):
		s = "******************************"
		s += "\n ID: " + str(self.ID)
		s += "\n Name: " + self.name
		s += "\n Balance: $" + str(self.balance)
		s += "\n Open Bets: " + str(self.bets)
		s += "\n Bet Count: " + str(self.nums)
		s += "\n******************************"
		return s

def main(): 
	x = User("Yuyu Li", "500")
	print x.__str__()

if __name__ == '__main__':main()


