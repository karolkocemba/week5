class CoinDispenser:
	
	coins = [25, 10, 5, 1]

	def make_change(self,amount):
		change = [0,0,0,0]
		balance = amount
		while balance != 0:
			for i in range(4):
				while balance // self.coins[i] > 0:
					change[i] += 1
					balance -= self.coins[i]
		return change

