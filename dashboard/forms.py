from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class UserRegistrationForm(UserCreationForm):
    profile_picture = forms.ImageField(required=False)
    mobile = forms.CharField(max_length=15, required=False)
    course = forms.CharField(max_length=50, required=False)
    semester = forms.CharField(max_length=10, required=False)
    batch = forms.CharField(max_length=50, required=False)
    roll_number = forms.CharField(max_length=20, required=False)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'profile_picture', 'mobile', 'course', 'semester', 'batch', 'roll_number')

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        if commit:
            user.save()
            UserProfile.objects.create(
                user=user,
                profile_picture=self.cleaned_data.get('profile_picture'),
                mobile=self.cleaned_data.get('mobile'),
                course=self.cleaned_data.get('course'),
                semester=self.cleaned_data.get('semester'),
                batch=self.cleaned_data.get('batch'),
                roll_number=self.cleaned_data.get('roll_number')
            )
        return user
