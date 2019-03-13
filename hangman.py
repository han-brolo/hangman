import random

def hangman(word):
	wrong = 0
	stages = ["",
			"________		",
			"|				",
			"|		 |		",
			"|		 0		",
			"|		/|\		",
			"|		/ \		",
			"|				"
			]
	rletters = list(word)
	board = ["__"] * len(word)
	win = False
	print("Welcome to Hangman")

	while wrong < len(stages) -1:
		print("\n")
		guess = "Guess a letter:\n"
		char = input(guess)
		if char in rletters:
			cind = rletters.index(char)
			board[cind] = char
			rletters[cind] = '$'
		else:
			wrong += 1
		print((" ".join(board)))
		e = wrong + 1
		print("\n".join(stages[0: e]))
		if "__" not in board:
			print("You win! The word was: ")
			print(" ".join(board))
			win = True
			break
		else:
			print("\nDEAD\nThe word was: " + word)

wordpool = ["testing", "theorizing", "believing", "disruption", "embargo", "telekenesis"]
hangman(random.choice(wordpool))