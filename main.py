import utilities.generator as generator


def main():
    consumers = generator.generateConsumers(50)
    producers = generator.generateProducers(50)

    #Maximum number of epochs
    numEpochs = 10000
    averagePrice = []
    numSold = []

    for i in range(numEpochs):
        #Consumers purchasing goods
        for con in consumers:
            for prod in producers:
                if not prod.sold:
                    if prod.price <= con.price:
                        con.bought = True
                        prod.sold = True
                        break

        numberSold = 0
        for prod in producers:
            if prod.sold:
                numberSold += 1
        numSold.append(numberSold)

        totalRevenue = 0
        for prod in producers:
            totalRevenue += prod.price
        averagePrice.append(totalRevenue / len(producers))

        if(numSold == len(producers)):
            break
        #Producers adjusting price based on sales
        for prod in producers:
            if not prod.sold:
                prod.price -= 0.1
            else:
                prod.price += 0.1
        #Reset status
        for prod in producers:
            prod.sold = False
        for con in consumers:
            con.bought = False
    bestEpoch = 0
    mostSold = 0
    for epoch in range(len(numSold)):
        if numSold[epoch] > mostSold:
            bestEpoch = epoch
            mostSold = numSold[epoch]
    print("The best epoch was {} where {} were sold for an average price of {}".format(bestEpoch,numSold[bestEpoch],averagePrice[bestEpoch]))








if __name__ == '__main__':
    main()