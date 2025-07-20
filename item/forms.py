from django import forms
from .models import Item


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            "name",
            "description",
            "category",
            "location",
            "price",
            "provider_name",
            "available_online",
            "image"
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full p-2 border rounded',
                'placeholder': 'Enter item name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full p-2 border rounded',
                'placeholder': 'Enter item description',
                'rows': 4
            }),
            'category': forms.Select(attrs={
                'class': 'w-full p-2 border rounded'
            }),
            'location': forms.TextInput(attrs={
                'class': 'w-full p-2 border rounded',
                'placeholder': 'Enter location'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'w-full p-2 border rounded',
                'placeholder': 'Enter price'
            }),
            'provider_name': forms.TextInput(attrs={
                'class': 'w-full p-2 border rounded',
                'placeholder': 'Enter provider name'
            }),
            'available_online': forms.CheckboxInput(attrs={
                'class': 'form-checkbox'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'w-full p-2 border rounded'
            }),
        }

    def __init__(self, *args, **kwargs):
        super(NewItemForm, self).__init__(*args, **kwargs)


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            "name",
            "description",
            "location",
            "price",
            "provider_name",
            "available_online",
            "image"
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full p-2 border rounded',
                'placeholder': 'Enter item name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full p-2 border rounded',
                'placeholder': 'Enter item description',
                'rows': 4
            }),
            'location': forms.TextInput(attrs={
                'class': 'w-full p-2 border rounded',
                'placeholder': 'Enter location'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'w-full p-2 border rounded',
                'placeholder': 'Enter price'
            }),
            'provider_name': forms.TextInput(attrs={
                'class': 'w-full p-2 border rounded',
                'placeholder': 'Enter provider name'
            }),
            'available_online': forms.CheckboxInput(attrs={
                'class': 'form-checkbox'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'w-full p-2 border rounded'
            }),
        }
