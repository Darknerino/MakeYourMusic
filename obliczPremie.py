def obliczPremie (x):
    if (x < 10000):
        return 0.10
    elif (x >= 10000 and x < 15000):
        return 0.12
    elif (x >= 15000 and x < 18000):
        return 0.14
    elif (x >= 18000 and x < 22000):
        return 0.10
    elif (x >= 22000):
        return 0.2