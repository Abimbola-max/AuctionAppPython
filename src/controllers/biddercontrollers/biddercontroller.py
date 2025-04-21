from flask import request, jsonify
from marshmallow import ValidationError

from src.dtos.bidderdto.bidderRequest import BidderRequestDTO
from src.dtos.bidderdto.loginrequest import LoginRequest
from src.dtos.bidderdto.loginresponse import LoginResponse
from src.dtos.sellerdto.sellerrequest import SellerRequestDTO
from src.exceptions.allexceptions import InvalidDetailsException
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

    def login_bidder(self):
        try:
            data = request.get_json()
            login_data = LoginRequest().load(data)
            response_data = self.bidder_service.login_bidder(login_data)
            return jsonify(LoginResponse().dump(response_data)), 201
        except ValidationError as err:
            return jsonify({"errors": err.messages}), 400
        except InvalidDetailsException as e:
            return jsonify({"error": str(e)}), 401
