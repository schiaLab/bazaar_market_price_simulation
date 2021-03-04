import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def generationIterate(min, max, up):

    sequence = np.array([])

    for n in np.linspace(min, max, max-min+1):

        if up:

            sequence = np.append(sequence, np.repeat(n, n ** 2))

        else:

            sequence = np.append(sequence, np.repeat((max - n + 1), n ** 2))


    return sequence







def initiate(min, max):


    demander = generationIterate(min, max, up=False)
    suppler = generationIterate(min, max, up=True)

    return suppler, demander


def trade(suppler, demander):

    supplyMarket = np.random.choice(suppler, replace=False, size=len(suppler))
    demandMarket = np.random.choice(demander, replace=False, size=len(demander))

    trade = demandMarket - supplyMarket

    price = (demandMarket + supplyMarket) / 2

    utility = (demandMarket - price) + (price - supplyMarket)

    tradeResult = np.where(trade>0, trade, np.nan)

    price = price[~np.isnan(tradeResult)]

    actualUtility = np.sum(utility[~np.isnan(tradeResult)])

    supplyMarket = supplyMarket[np.isnan(tradeResult)]

    demandMarket = demandMarket[np.isnan(tradeResult)]

    return price, supplyMarket, demandMarket, actualUtility


def tradeIterate(initSuppler, initDemander, iterNum):

    priceResult = np.array([])

    volResult = []

    utility = 0


    supply = initSuppler

    demand = initDemander


    for n in range(iterNum):

        price, nextSupply, nextDemand , au = trade(supply, demand)

        utility += au

        volResult.append(len(price))

        priceResult = np.append(priceResult, price)

        supply, demand = nextSupply, nextDemand

        print("%dth Trade Complete. %d Individuals Traded."%(n, len(price)))


    return priceResult, volResult, utility


















