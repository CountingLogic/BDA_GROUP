import random


def rolls_before_6():
    rolls = []
    for i in range(1000000):
        roll = random.randint(1,6) 
        if roll != 6:
            rolls.append(roll)
        else:
            rolls.append(6)
            return rolls


def E_x_y(x,y):
    #We do 1000 trials
    sum  = 0
    N = 10000
    i = 0
    while i < N:
        a = rolls_before_6()
        print(a)
        if len(a) == y:
            sum = sum + a.count(x)
            i  = i+1
    E_x_y = sum/N

    return E_x_y


