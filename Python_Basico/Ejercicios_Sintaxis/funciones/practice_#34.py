word = "hello word"


def reversed():
	for i in range(len(word)-1,-1,-1):
		print(word[i])

reversed()