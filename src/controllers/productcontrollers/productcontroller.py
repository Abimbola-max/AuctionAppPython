from flask import request, jsonify
from flask_jwt_extended import jwt_required
from marshmallow import ValidationError

from src.dtos.productdto.productrequest import ProductRequest


class ProductController:
    def __init__(self, product_service):
        self.product_service = product_service

    @jwt_required()
    def create_product(self):
        try:
            data = request.get_json()
            product_data = ProductRequest().load(data)

            errors = ProductRequest().validate(product_data)
            if errors:
                return jsonify(errors), 400

            if 'image' not in request.files:
                return jsonify({"error": "No image provided"}), 400

            image_file = request.files['image']
            if image_file.filename == '':
                return jsonify({"error": "Empty image filename"}), 400
            saved_product = self.product_service.create_product(product_data, image_file)

            return jsonify({
                "message": "Product created successfully.",
                "product_id": saved_product.product_id,
                "image_url": saved_product.image_url,
            }), 201

        except ValidationError as err:
            return jsonify({"errors": err.messages}), 400
        except PermissionError as err:
            return jsonify({"error": str(err)}), 403
        except Exception as e:
            return jsonify({"error": str(e)}), 500