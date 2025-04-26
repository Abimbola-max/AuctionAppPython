import os
from datetime import timedelta

import cloudinary
from dotenv import load_dotenv
from flask import Flask
from flask_jwt_extended import JWTManager

from src.controllers.admincontrollers.admincontroller import AdminController
from src.controllers.bidcontrollers.bidcontroller import BidController
from src.controllers.biddercontrollers.biddercontroller import BidderController
from src.controllers.productcontrollers.productcontroller import ProductController
from src.controllers.sellercontrollers.sellercontroller import SellerController
from src.data.models.admin import Admin
from src.data.repositories.adminrepo.adminrepository import AdminRepository
from src.data.repositories.bidderrepo.bidderrepository import BidderRepository
from src.data.repositories.bidrepo.bidrepository import BidRepository
from src.data.repositories.productrepo.productrepository import ProductRepository
from src.data.repositories.sellerrepo.sellerrepository import SellerRepository
from src.services.adminservices.adminservice import AdminService
from src.services.bidderservices.bidderservice import BidderService
from src.services.bidservices.bidservices import BidService
from src.services.productservices.productservice import ProductService
from src.services.sellerservices.sellerservice import SellerService

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "233-ERD-WEE"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=45)
app.config['JWT_TOKEN_LOCATION'] = ['headers']
app.config['JWT_HEADER_NAME'] = 'Authorization'
app.config['JWT_HEADER_TYPE'] = 'Bearer'
jwt = JWTManager(app)

load_dotenv()

cloudinary.config(
    cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME'),
    api_key=os.getenv('CLOUDINARY_API_KEY'),
    api_secret=os.getenv('CLOUDINARY_API_SECRET')
)


seller_repo = SellerRepository()
product_repo = ProductRepository()
bid_repo = BidRepository(product_repo)
bidder_repo = BidderRepository()
admin_repo = AdminRepository()

seller_service = SellerService(seller_repo)
admin_service = AdminService(admin_repo)
seller_controller = SellerController(seller_service)
admin_controller = AdminController(admin_service)
product_service = ProductService(product_repo, seller_repo)
bidder_service = BidderService(bidder_repo, bid_repo)

product_controller = ProductController(product_service)

bid_service = BidService(bid_repo)
bid_controller = BidController(bidder_service)

bidder_controller = BidderController(bidder_service)


@app.route('/register_seller', methods=['POST'])
def register_seller():
    return seller_controller.register_seller()

@app.route('/create_product', methods=['POST'])
def create_product():
    return product_controller.create_product()

@app.route('/login_seller', methods=['POST'])
def login_seller():
    return seller_controller.login_seller()

@app.route('/register_bidder', methods=['POST'])
def register_bidder():
    return bidder_controller.register_bidder()

@app.route('/login_bidder', methods=['POST'])
def login_bidder():
    return bidder_controller.login_bidder()

@app.route('/place_bid', methods=['POST'])
def place_bid():
    return bid_controller.place_bid()

@app.route('/login_admin', methods=['POST'])
def login_admin():
    return admin_controller.admin_login()


if __name__ == '__main__':
    app.run(debug=True)
