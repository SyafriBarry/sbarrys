from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from wishlist.models import BarangWishlist

# Create your views here.
def show_wishlist(request):
    data_barang_wishlist = BarangWishlist.objects.all()
    context = {
    'list_barang': data_barang_wishlist,
    'nama': 'Syafri Barry Salim',
    'npm' : '2106752136'
    }
    #return render(request, "wishlist.html", context)

def show_xml(request):
    data = BarangWishlist.objects.all()
    context = {
    'list': data,
    'nama': 'Syafri Barry Salim',
    'npm' : '2106752136'
    }
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    