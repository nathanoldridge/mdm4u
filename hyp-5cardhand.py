import random

spades = [0,0,0,0,0,0]
h = 0

while True:
    cards = ["H"]*13+["C"]*13+["D"]*13+["S"]*13
    hand = ""
    for r in range(5):
        #print(len(cards),len(hand))
        x = random.randint(0,len(cards)-1)
        #print(x)
        hand = hand + str(cards[x])
        cards.pop(x)
    #print(hand)
    spades[hand.count("S")] += 1
    h = h + 1
    if h%200000==0:
        print("")
        print(h/1000000, "Million hands dealt")
        print("--------------")
        for s in range(len(spades)):
            print(s, "spades:\t", str(spades[s]/sum(spades)*100)[:5], "%")
