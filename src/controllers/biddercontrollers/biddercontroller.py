from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import ValidationError

from src.dtos.bidderdto.bidderrequest import BidderRequestDTO
from src.dtos.bidderdto.loginrequest import LoginRequest
from src.dtos.bidderdto.loginresponse import LoginResponse
from src.dtos.sellerdto.sellerrequest import SellerRequestDTO
from src.exceptions.allexceptions import *
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
            return jsonify({"error": str(e)}), 500

    @jwt_required()
    def update_bid(self):
        try:
            data = request.get_json()
            product_id = data.get('product_id')
            bid_price = data.get('amount')
            bidder_id = get_jwt_identity()

            if not product_id or bid_price is None:
                return jsonify({'error': 'Missing required fields'}), 400

            current_price = self.bidder_service.get_current_price(product_id)
            if bid_price <= current_price:
                return jsonify({
                    'error': f'Your bid must be greater than the current price (${current_price})'
                }), 400

            result = self.bidder_service.place_bid(
                product_id=product_id,
                amount=bid_price,
                bidder_id=bidder_id
            )

            return jsonify({
                "message": "Bid placed successfully",
                "new_price": result["new_price"],
                "bid_id": str(result["bid_id"])
            }), 200

        except NotFoundException as e:
            return jsonify({'error': str(e)}), 404
        except InvalidAmountException as e:
            return jsonify({'error': str(e)}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500