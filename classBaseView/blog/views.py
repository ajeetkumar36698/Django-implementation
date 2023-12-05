from django.shortcuts import render
from .models import postModel
from django.http import Http404

from django.views.generic import ListView
# Create your views here.
class postList(ListView):
    model=postModel
    template_name='blog/home.html'
    ordering=['id']
    paginate_by=3
    paginate_orphans=1
    def get_context_data(self,*args,**kwargs):
        try:
            return super(postList,self).get_context_data(*args,**kwargs)
        except Http404:
            self.kwargs['page']=1
            return super(postList,self).get_context_data(*args,**kwargs)
 
            