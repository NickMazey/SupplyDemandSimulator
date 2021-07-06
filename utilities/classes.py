class consumer():
    """
    Represents consumers in the market
    Consumers have a fixed maximum price they are willing to buy at
    """
    def __init__(self,price):
        self.price = price
        self.bought = False

class producer():
    """
    Represents producers in the market
    Producers have a fixed minimum price they are willing to sell for
    """
    def __init__(self,price):
        self.price = price
        self.sold = False
