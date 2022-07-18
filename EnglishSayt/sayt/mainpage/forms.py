from .models import Task
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title','nameZone']
        widgets = {'title': TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите название'
        }),
            'nameZone': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
        }

