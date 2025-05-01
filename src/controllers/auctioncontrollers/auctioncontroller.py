from flask_jwt_extended import jwt_required

from src.services.adminservices.adminservice import AdminService


class  AuctionController:

    def __init__(self, admin_service: AdminService):
        self.admin_service = admin_service

    # @jwt_required()
    # def start_auction(self):
    #