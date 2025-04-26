from enum import Enum


class ProductPhase(Enum):

    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    AUCTIONED_OUT = "AUCTIONED_OUT"
    PENDING = "PENDING"
    ONGOING = "ONGOING"