from django import forms
from data01.models import feedback

class feedbackForm(forms.ModelForm):
    name= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label='이름')
    message=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}),label='피드백')
    class Meta:
        model = feedback
        fields = ('name', 'message',)
