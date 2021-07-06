import utilities.generator as generator
import random
import numpy as np
import matplotlib.pyplot as plot


def main():
    consumers = generator.generateConsumers(50)
    producers = generator.generateProducers(50)

    # Maximum number of epochs
    numEpochs = 1000

    epoch_quantity_demanded = np.array([0 for i in range(numEpochs)])
    epoch_quantity_supplied = np.array([0 for i in range(numEpochs)])
    epoch_market_price = np.array([0 for i in range(numEpochs)])
    marketPrice = random.randrange(1, 100)

    for i in range(numEpochs):
        # Consumers purchasing goods
        for con in consumers:
            if con.price >= marketPrice:
                for prod in producers:
                    if not prod.sold:
                        if prod.price <= con.price and prod.price <= marketPrice:
                            con.bought = True
                            prod.sold = True
                            break
        quantity_demanded = 0
        for con in consumers:
            if con.price >= marketPrice:
                quantity_demanded += 1

        quantity_supplied = 0
        for prod in producers:
            if prod.price <= marketPrice:
                quantity_supplied += 1

        if quantity_demanded > quantity_supplied:
            marketPrice += 1
        elif quantity_demanded < quantity_supplied:
            marketPrice -= 1

        np.put(epoch_quantity_demanded, i, quantity_demanded)
        np.put(epoch_quantity_supplied, i, quantity_supplied)
        np.put(epoch_market_price,i,marketPrice)

        # Reset status
        for prod in producers:
            prod.sold = False
        for con in consumers:
            con.bought = False

    demandQuantity = []
    priceLevel = []
    supplyQuantity = []

    for i in range(100):
        priceLevel.append(i)
        qd = 0
        qs = 0
        for con in consumers:
            if i <= con.price:
                qd += 1
        for prod in producers:
            if i >= prod.price:
                qs += 1
        demandQuantity.append(qd)
        supplyQuantity.append(qs)
    plot.plot(demandQuantity,priceLevel)
    plot.plot(supplyQuantity,priceLevel)
    plot.plot(epoch_quantity_demanded[numEpochs - 1] if epoch_quantity_demanded[numEpochs -1] < epoch_quantity_supplied[numEpochs -1]
              else epoch_quantity_supplied[numEpochs -1]
              ,epoch_market_price[numEpochs - 1], 'o-')
    plot.show()

if __name__ == '__main__':
    main()