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
            # Use camelCase keys here (matching data_key in the schema)
            product_data = {
                "name": request.form.get('name'),
                "description": request.form.get('description'),
                "sellerID": request.form.get('sellerID'),  # camelCase key!
                "bidMinimumPrice": request.form.get('bidMinimumPrice'),  # camelCase key!
                # "bidStartTime": request.form.get('bidStartTime'),
                # "bidEndTime": request.form.get('bidEndTime')
            }

            validated_data = ProductRequest().load(product_data)

            missing_fields = [key for key, value in product_data.items() if value is None]
            if missing_fields:
                return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400

            if 'image' not in request.files:
                return jsonify({"error": "No image provided"}), 400
            image_file = request.files['image']
            if image_file.filename == '':
                return jsonify({"error": "Empty image filename"}), 400

            saved_product = self.product_service.create_product(validated_data, image_file)

            return jsonify({
                "message": "Product created successfully.",
                "product_id": saved_product.product_id,
                "image_url": saved_product.image_url,
            }), 201

        except ValidationError as err:
            return jsonify(err.messages), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500