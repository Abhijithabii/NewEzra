from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('mobile', 'address','district', 'state', 'pincode', 'image',)
        widgets = {
            'mobile': forms.TextInput(attrs={'class' : 'form-control','minlength': 10, 'maxlength': 10}),
            'address':forms.TextInput(attrs={'class' : 'form-control'}),
            'district':forms.Select(attrs={'class' : 'form-control'}),
            'state':forms.Select(attrs={'class' : 'form-control'}),
            'pincode':forms.TextInput(attrs={'class' : 'form-control','minlength': 6, 'maxlength': 6}),
            'image':forms.FileInput(attrs={'class' : 'form-control'}),
            
        }
        # def clean_mobile(self):
        #     mobile = self.cleaned_data['mobile']
        #     try:
        #         int(mobile)
        #     except ValueError:
        #         raise ValidationError('Mobile number must contain only digits.')
        #     return mobile



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')
        widgets = {
            'first_name': forms.TextInput(attrs={'class' : 'form-control'}),
            'last_name' : forms.TextInput(attrs={'class' : 'form-control'}),
        }


# class CustomerProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ['mobile','address','image','district','state','pincode']
#         widgets = {
#             'mobile': forms.NumberInput(attrs={'class' : 'form-control col-3'}),
#             'address':forms.TextInput(attrs={'class' : 'form-control col-3'}),
#             'image':forms.ImageField(attrs={'class' : 'form-control col-3'}),
#             'district':forms.CharField(attrs={'class' : 'form-control col-3'}),
#             'state':forms.CharField(attrs={'class' : 'form-control col-3'}),
#             'pincode':forms.NumberInput(attrs={'class' : 'form-control col-3'}),
#         }