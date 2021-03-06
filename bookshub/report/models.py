from django.db import models

from ..utils.models import BaseModel
from ..users.models import User
from ..books.models import Book
from ..offers.models import Offer
from .constants import USER_REPORT, BOOK_REPORT, OFFER_REPORT


class ReportedUser(BaseModel):
    sender = models.ManyToManyField(User, related_name='sender')
    receiver = models.ForeignKey(User, related_name='receiver')

    reason = models.CharField(choices=USER_REPORT, max_length=1)

    def __str__(self):
        return self.reason


class ReportedBook(BaseModel):
    book = models.ForeignKey(Book)
    sender = models.ForeignKey(User)

    reason = models.CharField(choices=BOOK_REPORT, max_length=1)

    def __str__(self):
        return self.reason


class ReportedOffer(BaseModel):
    offer = models.ForeignKey(Offer)
    sender = models.ForeignKey(User)

    reason = models.CharField(choices=OFFER_REPORT, max_length=1)

    def __str__(self):
        return self.reason
