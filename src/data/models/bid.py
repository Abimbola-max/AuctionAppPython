from datetime import datetime


class Bid:

    def __init__(self, product_id: str, amount: int, bidder_id: int):
        self.product_id = product_id
        self.amount = amount
        self.bidder_id = bidder_id
        self.bid_time = datetime.now()

    @property
    def product_id(self):
        return self.__product_id

    @product_id.setter
    def product_id(self, product_id):
        self.__product_id = product_id

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, amount):
        self.__amount = amount

    @property
    def bidder_id(self):
        return self.__bidder_id

    @bidder_id.setter
    def bidder_id(self, bidder_id):
        self.__bidder_id = bidder_id

    @property
    def bid_time(self):
        return self.__bid_time

    @bid_time.setter
    def bid_time(self, bid_time):
        self.__bid_time = bid_time