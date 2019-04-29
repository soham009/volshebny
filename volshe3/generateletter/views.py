from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from generateletter.models import Visaletters

# Create your views here.

# Our original index view function
# Corresponds to original_index.html (rename it to index.html to use it!)

# def index(request):
#     my_dict = {'insert_me':"Now I am coming from first_app/index.html!"}
#     # Make sure this is pointing to the correct index
#     return render(request,'first_app/index.html',context=my_dict)


class list_view(ListView):
    model = Visaletters
    context_object_name = "list_view"
    template_name = "generateletter/list.html"


class gen_eng_visa(DetailView):
    model = Visaletters
    context_object_name = "detail_visa"
    template_name = "generateletter/gen_eng_visa.html"

class gen_rus_visa(DetailView):
    model = Visaletters
    context_object_name = "russian_visa"
    template_name = "generateletter/gen_rus_visa.html"

class gen_eng_voucher(DetailView):
    model = Visaletters
    context_object_name = "english_voucher"
    template_name = "generateletter/gen_eng_voucher.html"

class gen_rus_voucher(DetailView):
    model = Visaletters
    context_object_name = "russian_voucher"
    template_name = "generateletter/gen_rus_voucher.html"
