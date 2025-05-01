class Auction:

    def __init__(self, product_id, start_time, end_time, highest_bidder=None, final_price: float = None, auction_id=None):
        self.product_id = product_id
        self.start_time = start_time
        self.end_time = end_time
        self.highest_bidder = highest_bidder
        self.final_price = final_price
        self.auction_id = auction_id