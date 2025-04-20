from flask import request, jsonify
from marshmallow import ValidationError

from src.dtos.productdto.productrequest import ProductRequest


class ProductController:
    def __init__(self, product_service):
        self.product_service = product_service

    def create_product(self):
        try:
            data = request.get_json()
            product_data = ProductRequest().load(data)

            saved_product = self.product_service.create_product(product_data)

            return jsonify({
                "message": "Product created successfully.",
                "product_id": saved_product.product_id,
                "created_at": saved_product.created_at
            }), 201

        except ValidationError as err:
            return jsonify({"errors": err.messages}), 400
        except PermissionError as err:
            return jsonify({"error": str(err)}), 403
        except Exception as e:
            return jsonify({"error": str(e)}), 500