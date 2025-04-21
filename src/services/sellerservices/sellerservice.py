from datetime import timedelta

from flask_jwt_extended import create_access_token

from src.data.models.seller import Seller
from src.data.repositories.sellerrepo.sellerrepository import SellerRepository
from src.dtos.sellerdto.sellerresponse import SellerResponseDTO
from src.exceptions.allexceptions import *
from src.services.passwordsecurity.passwordencrypt import PasswordEncrypt


class SellerService:

    def __init__(self, seller_repo: SellerRepository):
        self.seller_repo = seller_repo

    def register_seller(self, seller_data_request):
        if self.seller_repo.email_exists(seller_data_request['email']):
            raise EmailAlreadyExistException("A user with this email already exists.")
        hashed_password = PasswordEncrypt.encrypt_password(seller_data_request["password"])
        seller = Seller(
            first_name=seller_data_request["first_name"],
            last_name=seller_data_request["last_name"],
            email=seller_data_request["email"],
            password=hashed_password,
            account_number=seller_data_request["account_number"],
            bank_name=seller_data_request["bank_name"]
        )

        saved_seller = self.seller_repo.save_seller(seller)
        access_token = create_access_token(
            identity=str(saved_seller.seller_id),
            expires_delta=timedelta(minutes=45)
        )
        seller_response_dto = SellerResponseDTO()
        response_data = {"message": "You have successfully registered.", "seller_id": str(saved_seller.seller_id), "token": access_token}
        return seller_response_dto.dump(response_data)


    def login_seller(self, seller_login_request):

        email = seller_login_request['email']
        password = seller_login_request['password'].strip()

        seller = self.seller_repo.find_by_email(email)
        if not seller:
            raise NotFoundException("Seller not found.")

        hashed_password = seller.password

        if not PasswordEncrypt.verify_password(password, hashed_password):
            raise InvalidDetailsException("Invalid details.")
        access_token = create_access_token(
            identity=str(seller.seller_id),
            expires_delta=timedelta(minutes=45)
        )
        return {
            "message": "login successful.",
            "first_name": f"Welcome {seller.first_name} {seller.last_name}",
            "seller_id": str(seller.seller_id),
            "token": access_token
        }


