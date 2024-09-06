from django import forms
from .models import Language, Level, Quiz, StudentProfile, UserMst

class languageform(forms.ModelForm):
    class Meta:
        model=Language
        fields='__all__'

class levelform(forms.ModelForm):
    class Meta:
        model=Level
        fields='__all__'

class quizform(forms.ModelForm):
    class Meta:
        model=Quiz
        fields='__all__'

class studentform(forms.ModelForm):
    class Meta:
        model=StudentProfile
        fields='__all__'

class userform(forms.ModelForm):
    class Meta:
        model=UserMst
        fields='__all__'