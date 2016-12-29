from django import forms
from django.forms import Textarea,CharField,TextInput,EmailInput,FileInput
from .models import idearegister,addques
from django.utils.translation import ugettext_lazy as _

class IdeaForm(forms.ModelForm):#for idea head
    class Meta:
        model=idearegister
        fields=('firstName','lastName','sex','phoneNumber','mailId','ideaTitle','ideaFile','idea',)
        labels = {
            'ideaFile': _(''),
        }
        widgets = {
            'firstName': TextInput(attrs={'required': True}),
   #         'sex':TextInput(attrs={'required': True}),
            'lastName': TextInput(attrs={'required': True}),
            'phoneNumber': TextInput(attrs={'required': True}),
            'mailId': EmailInput(attrs={'required': True}),
            'firstName': TextInput(attrs={'required': True}),
            'idea':Textarea(attrs={'required': True}),
            'ideaFile':FileInput(attrs={'required':True}),
        }

class quesForm(forms.ModelForm): #for forum
    class Meta:
        model=addques
        fields=('name','question')
        widgets={
            'name': TextInput(attrs={'required': True}),
            'question': TextInput(attrs={'required': True}),
        }

class RegForm(forms.ModelForm): #for registration
    class Meta:
        model=idearegister
        fields=('firstName','lastName','sex','phoneNumber','mailId','ideaFile',)
        labels = {
            'ideaFile': _('Resume'),
        }
        help_texts = {
            'ideaFile': _('Name of file must have no space and have applicantname,ideaname and collegename like RajeshArtificialIntMSRIT'),
        }
        widgets = {
            'firstName': TextInput(attrs={'required': True}),
            #         'sex':TextInput(attrs={'required': True}),
            'lastName': TextInput(attrs={'required': True}),
            'phoneNumber': TextInput(attrs={'required': True}),
            'mailId': EmailInput(attrs={'required': True}),
            'firstName': TextInput(attrs={'required': True}),
            'idea': Textarea(attrs={'required': True}),
            'ideaFile': FileInput(attrs={'required': True}),
        }

class EmailIdForm(forms.Form):
    emailId = forms.EmailField(label='Your Email-Id', max_length=50)