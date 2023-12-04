from django import forms
from .models import studentModel
class ContactForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    msg=forms.CharField(widget=forms.Textarea)

class studentForm(forms.ModelForm):
    class Meta:
        model=studentModel
        fields=['id','name','roll','course']
        widgets={'name':forms.TextInput(attrs={'class':'myclass'})}




