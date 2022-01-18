import random

numnum = 6   # Choose 2 numbers
maxnum = 49  # from 1 to 10
             # without repetition
studnums = {
"Student1":[3,12,22,30,31,41],
"Student2":[13,15,17,19,22,48],
"Student3":[6,9,12,32,33,34],
"Student4":[5,10,12,14,20,30],
"Student5":[7,14,28,29,36,37],
"Student6":[1,2,3,4,5,6],
"Student7":[7,12,17,38,40,49],
"Student8":[8,9,10,21,28,43],
"Student9":[16,18,24,25,42,45],
"Student10":[1,12,26,37,42,45],
"Student11":[6,11,27,33,47,48],
"Student12":[4,7,9,11,19,20],
"Student13":[1,6,13,27,35,47]
}
studnumslist = studnums.values()
winners = {}
draws = 0
while True:
    winnums = [random.randint(1,maxnum)]
    while len(winnums)<numnum:
        y = random.randint(1,maxnum)
        if y not in winnums:
            winnums.append(y)
    draws += 1
    winnums=sorted(winnums)
    if winnums in studnumslist:
        winner = list(studnums.keys())[list(studnums.values()).index(winnums)]
        print("Draw", draws, "WINNER FOUND:", winner)
        print("NUMBERS:", winnums)
        print()
        if winner not in winners.keys():
            winners[winner] = 1
        else:
            winners[winner] += 1
        for x in winners:
            print(x,winners[x])
    print("Press Ctrl+Z to stop")
    #if draws%2000==0:
    #    print(draws, "Draws; no wins yet")
