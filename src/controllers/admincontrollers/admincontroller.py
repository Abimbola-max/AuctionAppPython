from flask import request, jsonify
from flask_jwt_extended import create_access_token
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

