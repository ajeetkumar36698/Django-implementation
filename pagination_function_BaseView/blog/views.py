from django.shortcuts import render
from .models import postModel
from django.core.paginator import Paginator

# Create your views here.
def postList(request):
    all_data=postModel.objects.all().order_by('id')
    paginator=Paginator(all_data,2,orphans=1)
    page_number=request.GET.get("page")
    
    page_obj=paginator.get_page(page_number)
    
    return render(request,'blog/home.html',{'posts':page_obj})
