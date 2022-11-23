from django.http import HttpResponse
from django.views.generic import ListView
from URL.models import Contact

class ListContactView(ListView):

      model = Contact
      template_name = 'contact_list.html'
def index(reqest):
    return HttpResponse("NEW PROJECT METANIT.COM")