from django.db import models

# Create your models here.
class Customer(models.Model):
    ids = models.IntegerField(null = False , blank = False )
    name = models.CharField(max_length = 200)
    email = models.EmailField(max_length = 200,unique = True,null = False , blank = False)
    curr_bal = models.DecimalField(decimal_places = 2,max_digits = 8)

class Hist(models.Model):
    
    From = models.EmailField(max_length = 200,unique = True,null = False , blank = False)
    To = models.EmailField(max_length = 200,unique = True,null = False , blank = False)
    amount =  models.DecimalField(decimal_places = 2,max_digits = 8)
    timestamp = models.DateTimeField(auto_now_add=True)

