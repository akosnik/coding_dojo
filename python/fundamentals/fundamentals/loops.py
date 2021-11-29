def print150():
    for i in range(151):
        print(i)


def multiple5():
    for i in range(0, 1001, 5):
        print(i)


def countDojo():
    for i in range(101):
        if (i % 10 == 0):
            print("Dojo")
        elif (i % 5 == 0):
            print("Coding")
        else:
            print(i)


def sigma(num):
    sum = 0
    for i in range(num):
        sum += i
    print(sum)


def countDownByFour():
    for i in range(2018, 0, -4):
        print(i)


def flexCounter(lowNum, highNum, mult):
    for i in range(lowNum, highNum):
        if (i % mult == 0):
            print(i)


flexCounter(0, 20, 3)
