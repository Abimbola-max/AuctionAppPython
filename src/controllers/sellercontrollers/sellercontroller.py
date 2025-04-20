from flask import request, jsonify

from src.data.repositories.sellerrepo.sellerrepository import SellerRepository
from src.dtos.sellerdto.sellerrequest import SellerRequestDTO
from src.services.sellerservices.sellerservice import SellerService


class SellerController:

    def __init__(self, seller_service: SellerService):
        self.seller_service = seller_service

    def register_seller(self):
        data = request.get_json()
        try:
            seller_data_request = SellerRequestDTO().load(data)

            response_data = self.seller_service.register_seller(seller_data_request)
            return jsonify(response_data), 201

        except Exception as e:
            return jsonify({'error': str(e)}), 400