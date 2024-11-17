from django import forms
from application.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Full Name..'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email Address..'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Subject..'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type Your Message..'})  
        }