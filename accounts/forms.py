from django.forms import ModelForm
from accounts.models import *

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__' #order so tae model ko kyi pee shi tha mhya field ko form a nay nae te sout
        #fields = ['status', 'name'] --> lo chin tae field ko pl swl htote ml so list nae pya
        