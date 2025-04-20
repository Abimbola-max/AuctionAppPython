from flask import Flask

from src.controllers.sellercontrollers.sellercontroller import SellerController
from src.data.repositories.sellerrepo.sellerrepository import SellerRepository
from src.services.sellerservices.sellerservice import SellerService

app = Flask(__name__)

seller_repo = SellerRepository()
seller_service = SellerService(seller_repo)
seller_controller = SellerController(seller_service)


@app.route('/register_seller', methods=['POST'])
def register_seller():
    return seller_controller.register_seller()


if __name__ == '__main__':
    app.run(debug=True)
