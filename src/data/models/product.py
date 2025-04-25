from datetime import datetime


class Product:

    def __init__(self, name: str, description: str, seller_id: str, starting_price, bid_start_time: datetime, bid_end_time: datetime, image_url: str, created_at=None, _id=None):
        self.name = name
        self.description = description
        self.starting_price = starting_price
        self.image_url = image_url
        self.bid_start_time = bid_start_time
        self.bid_end_time = bid_end_time
        self.seller_id = seller_id
        self.created_at = created_at
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
    def bid_minimumprice(self):
        return self.__starting_price

    @bid_minimumprice.setter
    def bid_minimumprice(self, starting_price):
        self.__starting_price = starting_price

    @property
    def bid_start_time(self):
        return self.__bid_start_time

    @bid_start_time.setter
    def bid_start_time(self, bid_start_time):
        self.__bid_start_time = bid_start_time

    @property
    def bid_end_time(self):
        return self.__bid_end_time

    @bid_end_time.setter
    def bid_end_time(self, bid_end_time):
        self.__bid_end_time = bid_end_time

    @property
    def seller_id(self):
        return self.__seller_id

    @seller_id.setter
    def seller_id(self, seller_id):
        self.__seller_id = seller_id

    @property
    def created_at(self):
        return self.__created_at

    @created_at.setter
    def created_at(self, created_at):
        self.__created_at = created_at

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


