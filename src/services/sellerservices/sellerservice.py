from src.data.models.seller import Seller
from src.data.repositories.sellerrepo.sellerrepository import SellerRepository
from src.dtos.sellerdto.sellerrequest import SellerRequestDTO
from src.dtos.sellerdto.sellerresponse import SellerResponseDTO


class SellerService:

    def __init__(self, seller_repo: SellerRepository):
        self.seller_repo = seller_repo

    # def get_seller_by_id(self, seller_id):
    #     return self.seller_repo.f


    # def register_seller(self, seller_data_request: SellerRequestDTO):
    #     seller = Seller(
    #         first_name=seller_data_request.first_name,
    #         last_name=seller_data_request.last_name,
    #         email=seller_data_request.email,
    #         password=seller_data_request.password,
    #         account_number=seller_data_request.account_number,
    #         bank_name=seller_data_request.bank_name
    #     )
    #     saved_seller = self.seller_repo.save_seller(seller)
    #     seller_response_dto = SellerResponseDTO()
    #     seller_response_dto.message = "You have successfully registered."
    #     seller_response_dto.seller_id = str(saved_seller.firstName)
    #     response_data = seller_response_dto.dump(seller_response_dto)

    def register_seller(self, seller_data_request):
        seller = Seller(
            first_name=seller_data_request["first_name"],
            last_name=seller_data_request["last_name"],
            email=seller_data_request["email"],
            password=seller_data_request["password"],
            account_number=seller_data_request["account_number"],
            bank_name=seller_data_request["bank_name"]
        )
        saved_seller = self.seller_repo.save_seller(seller)
        seller_response_dto = SellerResponseDTO()
        response_data = {"message": "You have successfully registered.", "seller_id": str(saved_seller.seller_id)}
        return seller_response_dto.dump(response_data)