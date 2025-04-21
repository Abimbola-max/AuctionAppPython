from flask import Flask

from src.controllers.biddercontrollers.biddercontroller import BidderController
from src.controllers.productcontrollers.productcontroller import ProductController
from src.controllers.sellercontrollers.sellercontroller import SellerController
from src.data.repositories.bidderrepo.bidderrepository import BidderRepository
from src.data.repositories.productrepo.productrepository import ProductRepository
from src.data.repositories.sellerrepo.sellerrepository import SellerRepository
from src.services.bidderservices.bidderservice import BidderService
from src.services.productservices.productservice import ProductService
from src.services.sellerservices.sellerservice import SellerService

app = Flask(__name__)

seller_repo = SellerRepository()
seller_service = SellerService(seller_repo)
seller_controller = SellerController(seller_service)

product_repo = ProductRepository()
product_service = ProductService(product_repo, seller_repo)
product_controller = ProductController(product_service)

bidder_repo = BidderRepository()
bidder_service = BidderService(bidder_repo)
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


if __name__ == '__main__':
    app.run(debug=True)
