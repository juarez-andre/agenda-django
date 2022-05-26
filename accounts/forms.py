from django import forms
from django.contrib.auth.models import User

class FormCadastro(forms.ModelForm):
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'required': True}))

    def clean(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        user = self.cleaned_data.get('username')
        emaill = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
    
        if any(char.isdigit() for char in first_name):
            self.add_error('first_name', 'Não inclua números números neste campo')

        if any(char.isdigit() for char in last_name):
            self.add_error('last_name', 'Não inclua números neste campo.')
        
        if password != password2:
            self.add_error('password2', 'As senhas não são iguais.')

        if User.objects.filter(username=user).exists():
            self.add_error('username', 'Usuário já cadastrado.')

        if User.objects.filter(email=emaill).exists():
            self.add_error('email', 'Email já cadastrado.')

        return self.cleaned_data
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
            'password2'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs= {'class': 'form-control', 'required': True}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'nome@exemplo.com', 'required': True}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'required': True}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'required': True})
        }
        labels = {
            'first_name': 'Primeiro nome', 'last_name': 'Sobrenome',
            'user': 'Usuário', 'email': 'Email'
        }
