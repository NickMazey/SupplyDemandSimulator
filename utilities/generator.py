import random
import numpy as np
from utilities.classes import consumer
from utilities.classes import producer
def generateConsumers(number):
    """
    Method to generate a number of consumers for the simulation
    :param number: the number of consumers to be generated
    :return: a list of generated consumers
    """
    consumers = [None for i in range(number)]
    for i in range(number):
        consumers[i] = consumer(generatePrice())
    return np.array(consumers)

def generateProducers(number):
    """
    Method to generate a number of producers for the simulation
    :param number: the number of producers to be generated
    :return: a list of generated producers
    """
    producers = [None for i in range(number)]
    for i in range(number):
        producers[i] = producer(generatePrice())
    return np.array(producers)

def generatePrice():
    return random.randrange(1,100)