from django import forms


class InvestigacaoForm(forms.Form):
    suspeito = forms.IntegerField(label='Suspeito do crime')
    arma = forms.IntegerField(label='Arma do crime')
    local = forms.IntegerField(label='Local do crime')