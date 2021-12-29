from django.utils import timezone
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.db.models import Q

from datetime import datetime
from numpy_financial import pmt
from decouple import config
import numpy as np
import math


from bank_loans import models


# class LoanMixin:
#     @property
#     def paymentValue(self):
#         months = self.duration * 12
#         rate = (self.interest_rate / 100) / 12
#         principal = self.amount
#         payment = pmt(rate, months, principal)
#         return -(payment)
