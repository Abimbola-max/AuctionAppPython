import datetime

import cloudinary.uploader

from src.data.models.UserType import UserType
from src.data.models.product import Product
from src.data.repositories.productrepo.productrepository import ProductRepository
from src.data.repositories.sellerrepo.sellerrepository import SellerRepository
from src.exceptions.allexceptions import InvalidRoleException, ValidationError


class ProductService:

    def __init__(self, product_repo: ProductRepository, seller_repo: SellerRepository):
        self.product_repo = product_repo
        self.seller_repo = seller_repo

    def create_product(self, product_data: dict):
        try:
            if not self.seller_repo.exists_by_id(product_data['seller_id']):
                raise ValidationError("Invalid seller_id: Seller does not exist.")
            ProductService.__validate_time(product_data)
            upload_result = cloudinary.uploader.upload(
                'firstproduct.avif',
                folder="auction_products"
            )
            image_url = upload_result['secure_url']
            product = Product(
                name=product_data['name'],
                description=product_data['description'],
                seller_id=product_data['seller_id'],
                starting_price=product_data['starting_price'],
                image_url=image_url,
                bid_start_time=product_data['bid_start_time'],
                bid_end_time=product_data['bid_end_time'],
                created_at=datetime.datetime.now().strftime("%Y-%m-%d %H:%M")            )
            saved_product = self.product_repo.create_product(product)
            return saved_product
        except Exception as err:
            if 'image_url' in locals():
                cloudinary.uploader.destroy(upload_result['public_id'])
            raise err

    @staticmethod
    def __valid_role(current_user):
        if current_user.user_type != UserType.SELLER:
            raise InvalidRoleException("Only sellers can create products")

    @staticmethod
    def __validate_time(product_data):
        date_time_now = datetime.datetime.now()
        bid_start_time = product_data['bid_start_time']
        bid_end_time = product_data['bid_end_time']

        if bid_start_time < date_time_now:
            raise ValidationError("Bid start time cannot be in the past.")
        if bid_end_time < date_time_now:
            raise ValidationError("Bid end time cannot be in the past.")
        if bid_end_time <= bid_start_time:
            raise ValidationError("Bid end time must be after bid start time.")



