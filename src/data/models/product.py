from datetime import datetime


class Product:

    def __init__(self, name: str, description: str, seller_id: str, bid_minimum_price, image_url=None, added_at=None, _id=None):
        self.name = name
        self.description = description
        self.bid_minimum_price = bid_minimum_price
        self.image_url = image_url
        # self.bid_start_time = bid_start_time
        # self.bid_end_time = bid_end_time
        self.seller_id = seller_id
        self.added_at = added_at
        self.product_id = _id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def bid_minimum_price(self):
        return self.__bid_minimum_price

    @bid_minimum_price.setter
    def bid_minimum_price(self, bid_minimum_price):
        self.__bid_minimum_price = bid_minimum_price

    # @property
    # def bid_start_time(self):
    #     return self.__bid_start_time
    #
    # @bid_start_time.setter
    # def bid_start_time(self, bid_start_time):
    #     self.__bid_start_time = bid_start_time

    # @property
    # def bid_end_time(self):
    #     return self.__bid_end_time
    #
    # @bid_end_time.setter
    # def bid_end_time(self, bid_end_time):
    #     self.__bid_end_time = bid_end_time

    @property
    def seller_id(self):
        return self.__seller_id

    @seller_id.setter
    def seller_id(self, seller_id):
        self.__seller_id = seller_id

    @property
    def added_at(self):
        return self.__added_at

    @added_at.setter
    def added_at(self, added_at):
        self.__added_at = added_at

    @property
    def product_id(self):
        return self.__product_id

    @product_id.setter
    def product_id(self, product_id):
        self.__product_id = product_id

    @property
    def image_url(self):
        return self.__image_url

    @image_url.setter
    def image_url(self, image):
        self.__image_url = image


