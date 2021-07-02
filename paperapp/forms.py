from django import forms
from .models import Paper


class PaperForm(forms.ModelForm):
	class Meta:
		model = Paper
		fields = '__all__'