word_1 = 'good'
word_2 = 'morning'

def greeting():
	print(word_1)


def greeting_2():
	print(word_2)
	greeting()

greeting_2()