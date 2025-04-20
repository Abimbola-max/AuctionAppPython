from flask import Flask

from src.controllers.productcontrollers.productcontroller import ProductController
from src.controllers.sellercontrollers.sellercontroller import SellerController
from src.data.repositories.productrepo.productrepository import ProductRepository
from src.data.repositories.sellerrepo.sellerrepository import SellerRepository
from src.services.productservices.productservice import ProductService
from src.services.sellerservices.sellerservice import SellerService

app = Flask(__name__)

seller_repo = SellerRepository()
seller_service = SellerService(seller_repo)
seller_controller = SellerController(seller_service)

product_repo = ProductRepository()
product_service = ProductService(product_repo, seller_repo)
product_controller = ProductController(product_service)


@app.route('/register_seller', methods=['POST'])
def register_seller():
    return seller_controller.register_seller()

@app.route('/create_product', methods=['POST'])
def create_product():
    return product_controller.create_product()


if __name__ == '__main__':
    app.run(debug=True)
