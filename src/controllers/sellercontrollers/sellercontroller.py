from flask import request, jsonify
from marshmallow import ValidationError

from src.data.repositories.sellerrepo.sellerrepository import SellerRepository
from src.dtos.sellerdto.loginresponse import LoginResponse
from src.dtos.sellerdto.sellerloginrequest import LoginRequest
from src.dtos.sellerdto.sellerrequest import SellerRequestDTO
from src.exceptions.allexceptions import InvalidDetailsException
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

    def login_seller(self):
        try:
            data = request.get_json()
            login_data = LoginRequest().load(data)
            response_data = self.seller_service.login_seller(login_data)
            return jsonify(LoginResponse().dump(response_data)), 201
        except ValidationError as err:
            return jsonify({"errors": err.messages}), 400
        except InvalidDetailsException as e:
            return jsonify({"error": str(e)}), 401
