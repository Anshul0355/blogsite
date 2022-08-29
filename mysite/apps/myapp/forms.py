from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from myapp.models import Post ,Comment
# from phonenumber_field.formfields import PhoneNumberField

# Sign Up Form
class SignUpForm(UserCreationForm):

    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')
    # mobile_num = forms.IntegerField( widget=  forms.TextInput(attrs={'rows':4 ,'cols':40}), required=True)
        # mobile_num = forms.IntegerField(max_length=50, help_text='Enter mobile number*' )

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',

            'email',
            'password1',
            'password2',
            ]

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
                'email',
                'password',
        ]


class NewPostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title', 'description', 'pic']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author','content','created')