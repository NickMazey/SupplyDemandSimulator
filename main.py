import utilities.generator as generator
import random
import numpy as np


def main():
    consumers = generator.generateConsumers(50)
    producers = generator.generateProducers(50)

    #Maximum number of epochs
    numEpochs = 10000

    epoch_quantity_demanded = np.array([0 for i in range(numEpochs)])
    epoch_quantity_supplied = np.array([0 for i in range(numEpochs)])

    for i in range(numEpochs):
        marketPrice = random.randrange(1,100)
        #Consumers purchasing goods
        for con in consumers:
             if con.price < marketPrice:
                for prod in producers:
                    if not prod.sold:
                        if prod.price <= con.price:
                            con.bought = True
                            prod.sold = True
                            break
        quantity_demanded = 0
        for con in consumers:
            if con.price <= marketPrice:
                quantity_demanded += 1

        quantity_supplied = 0
        for prod in producers:
            if prod.price >= marketPrice:
                quantity_supplied += 1

        if quantity_demanded > quantity_supplied:
            marketPrice += 0.1
        elif quantity_demanded < quantity_supplied:
            marketPrice -= 0.1

        np.put(epoch_quantity_demanded,i,quantity_demanded)
        np.put(epoch_quantity_supplied,i,quantity_supplied)

        #Reset status
        for prod in producers:
            prod.sold = False
        for con in consumers:
            con.bought = False








if __name__ == '__main__':
    main()