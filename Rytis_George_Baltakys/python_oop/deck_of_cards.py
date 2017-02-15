import random

class Deck(object):
	def __init__(self):
		self.reset()

	def getDeck(self):
		return self.cards

	def shuffle(self):
		for i in range(1001):
			random1 = random.randrange(0, 52)
			random2 = random.randrange(0, 52)
			temp = self.cards[random1]
			self.cards[random1] = self.cards[random2]
			self.cards[random2] = temp
		return self

	def reset(self):
		# Diamonds, Heards, Spades, Clubs
		# Values 2 - 10 Jack, Queen, King, Ace
		self.cards = ['JD','QD','KD','AD','JH','QH','HK','AH','JS','QS','KS','AS','JC','QC','KC','AC']
		for i in range(2,11):
			self.cards.append(str(i) + 'D')
			self.cards.append(str(i) + 'H')
			self.cards.append(str(i) + 'S')
			self.cards.append(str(i) + 'C')
		self.cards.sort()
		return self

	def deal(self):
		return self.cards.pop()

class Player(object):
	def __init__(self, name):
		self.name = name
		self.hand = []

	def draw(self, card):
		self.hand.append(card)

	def discard(self, card):
		return self.hand.remove(card)

deck = Deck()
print deck.getDeck()
print deck.shuffle().getDeck()

player = Player('bob')
player.draw(deck.deal())
player.draw(deck.deal())
player.draw(deck.deal())

print player.hand
print deck.getDeck()
