from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from marshmallow import ValidationError

from src.dtos.admindto.adminrequest import AdminRequest
from src.dtos.admindto.adminresponse import AdminResponse
from src.services.adminservices.adminservice import AdminService


class AdminController:

    def __init__(self, admin_service: AdminService):
        self.admin_service = admin_service

    def admin_login(self):
        try:
            data = request.get_json()
            validated_data = AdminRequest().load(data)
            admin = self.admin_service.login_admin(validated_data)

            access_token = create_access_token(identity=admin.email)

            response = {
                "message": "Login successful",
                "token": access_token,
                "admin": AdminResponse().dump(admin)
            }
            return jsonify(response), 200

        except ValidationError as err:
            return jsonify({"errors": err.messages}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    @jwt_required()
    def start_auction(self):
        try:
            self.admin_service.start_auction()
            return jsonify({'message': 'Dear esteemed Customers, Auction has started'}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    @jwt_required()
    def end_auction(self):
        try:
            self.admin_service.end_auction()
            return jsonify({'message': 'Dear esteemed Customers, Auction has started'}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    @jwt_required()
    def approve_product(self, product_id: str):
        try:
            self.admin_service.accept_product(product_id)
            return jsonify({"message": "Product approved"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    @jwt_required()
    def reject_product(self, product_id: str):
        try:
            self.admin_service.reject_product(product_id)
            return jsonify({"message": "Product rejected"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400

