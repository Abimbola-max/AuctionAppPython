from flask import request, jsonify

from src.dtos.bidderdto.bidderRequest import BidderRequestDTO
from src.dtos.sellerdto.sellerrequest import SellerRequestDTO
from src.services.bidderservices.bidderservice import BidderService


class BidderController:

    def __init__(self, bidder_service: BidderService):
        self.bidder_service = bidder_service

    def register_bidder(self):
        data = request.get_json()
        try:
            bidder_data_request = BidderRequestDTO().load(data)

            response_data = self.bidder_service.register(bidder_data_request)
            return jsonify(response_data), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 400
