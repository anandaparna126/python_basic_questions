import random, itertools
deck = list(itertools.product(range(1,14), ["Spade","Club","Hearts","Diamond"]))
random.shuffle(deck)
print(deck, "\n")

print("top five cards are: ")

for i in range(5):
    print(deck[i][0], "of", deck[i][1])
