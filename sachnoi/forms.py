from django import forms

class TextToSpeechForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label="Nhập văn bản", max_length=5000)