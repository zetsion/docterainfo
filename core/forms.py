from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import ContactMessage


class LoginForm(AuthenticationForm):
        username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-indigo-500',
            'placeholder': 'Username'
        }),
        error_messages={
            'required': 'Please enter your username.'
        }
    )
        password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-indigo-500',
            'placeholder': 'Password'
        }),
        error_messages={
            'required': 'Please enter a password.'
        }
    )



class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-indigo-500',
            'placeholder': 'Email Address'
        }),
        error_messages={
            'required': 'Please enter your email address.',
            'invalid': 'Enter a valid email address.'
        }
    )

    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-indigo-500',
            'placeholder': 'Username'
        }),
        error_messages={
            'required': 'Please enter your username.'
        }
    )

    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-indigo-500',
            'placeholder': 'Password'
        }),
        error_messages={
            'required': 'Please enter a password.'
        }
    )

    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-indigo-500',
            'placeholder': 'Confirm Password'
        }),
        error_messages={
            'required': 'Please confirm your password.'
        }
    )

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'content']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border rounded', 
                'placeholder': 'Your Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-3 py-2 border rounded', 
                'placeholder': 'Your Email'
            }),
            'content': forms.Textarea(attrs={
                'class': 'w-full px-3 py-2 border rounded', 
                'placeholder': 'Your message...'
            }),
        }

        error_messages = {
            'name': {'required': 'Please enter your name.'},
            'email': {'required': 'Please enter your email address.'},
            'content': {'required': 'Please enter your message.'},
        }
