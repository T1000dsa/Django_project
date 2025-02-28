from django import forms
from .models import Category, TagModel, Worker, Helmet
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError

class AddPostForm(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Category not choiced', label='Category', required=False)
    #helmet = forms.ModelChoiceField(queryset=Helmet.objects.all(), required=False, empty_label='Helmet not choiced', label='Helmet')
    class Meta:
        model = Worker
        fields = ['title', 'slug', 'content', 'photo', 'is_published'] # '__all__'
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-input'}),
            'content':forms.Textarea(attrs={'cols':50, 'rows':5})
        }
        labels = {'slug':'URL'}
    def clean_data(self):
        title = self.cleaned_data['title']
        if len(title)>128:
            raise ValidationError('Title is too long')
        else:
            return title


class UploadClassForm(forms.Form):
    file = forms.ImageField(label='File')