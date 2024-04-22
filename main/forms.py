from .models import News
from django.forms import ModelForm, TextInput, Textarea


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ["title", "content"]
        widgets = {
            "title": TextInput(
                attrs={"class": "form-control", "placeholder": "News title"}
            ),
            "content": Textarea(
                attrs={"class": "form-control", "placeholder": "News content"}
            ),
        }
