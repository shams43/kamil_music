from django import forms


from .models import Song, Author, Janr


class AddSongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = '__all__'
class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
class AddJanrForm(forms.ModelForm):
    class Meta:
        model = Janr
        fields = '__all__'