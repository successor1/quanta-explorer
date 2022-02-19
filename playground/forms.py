from django import forms

class IndexForm(forms.Form):
    Search = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'block height, block hash, transaction hash, QRL address'}))
