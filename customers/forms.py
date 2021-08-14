from django import forms
from customers.models import Hist
class MoneyTransferForm (forms.ModelForm):
    class Meta:
        model = Hist
        fields = [
            "From",
            "To",
            "amount"

        ]
