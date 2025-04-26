from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required

from src.dtos.biddto.bidresponse import BidResponse
from src.exceptions.allexceptions import *
from src.services.bidderservices.bidderservice import BidderService


class BidController:
    def __init__(self, bidder_service: BidderService):
        self.bidder_service = bidder_service
        self.bid_response = BidResponse()

    @jwt_required()
    def place_bid(self):
        try:
            data = request.get_json()
            product_id = data.get('product_id')
            amount = data.get('amount')

            if not product_id or not amount:
                return jsonify({"error": "Missing product_id or amount"}), 400

            try:
                amount = int(amount)
            except ValueError:
                return jsonify({"error": "Amount must be a number"}), 400

            bidder_id = get_jwt_identity()

            bid_data = self.bidder_service.place_bid(
                product_id=product_id,
                amount=amount,
                bidder_id=bidder_id
            )

            return self.bid_response.dump({
                "message": "Bid placed successfully",
                **bid_data
            }), 201

        except NotFoundException as e:
            return jsonify({"error": str(e)}), 404
        except InvalidAmountException as e:
            return jsonify({"error": str(e)}), 400
        except ValueError as e:
            return jsonify({"error": str(e)}), 400