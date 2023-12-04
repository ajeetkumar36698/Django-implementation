from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import ContactForm,studentForm
from django.views.generic.edit import FormView,CreateView,UpdateView,DeleteView
from django.contrib import messages
from django.http import HttpResponse
from .models import studentModel



from .models import studentModel
# Create your views here.
class studentView(ListView):
    model=studentModel
    template_name='school/list.html'
    context_object_name='studentModel'
    
class studentDetailView(DetailView):
    model=studentModel
    template_name='school/detail.html'
    context_object_name='studentModel'

class contactFormView(FormView):
    template_name='school/contact.html'
    form_class=ContactForm
    success_url='/contact/'
    initial={'name':'Ajeet'}
    def form_valid(self,form):
        print(form.cleaned_data['name'])
        print(form.cleaned_data['email'])
        print(form.cleaned_data['msg'])

        return HttpResponse("hhhhhhhhhhhhhhhh")
# class studentCreateView(CreateView):
#     model=studentModel
#     fields=['name','roll','course']
#     template_name='school/createView.html'
#     success_url='/studentCV/'
   
class studentCreateView(CreateView):
    form_class=studentForm
    template_name='school/createView.html'
    success_url='/stu/'

# class studentUpdateView(UpdateView):
#     model=studentModel
#     fields=['name','roll','course']
#     template_name='school/update.html'
#     success_url='/update/'
class studentUpdateView(UpdateView):
    model=studentModel
    form_class=studentForm
    # fields=['name','roll','course']
    template_name='school/update.html'
    success_url='/update/'
class studentDeleteView(DeleteView):
    model=studentModel
    success_url='/stu/'
    template_name='school/delete.html'

