from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    mobile = forms.CharField(max_length=15)
    course = forms.CharField(max_length=50)
    semester = forms.CharField(max_length=10)
    batch = forms.CharField(max_length=50)
    roll_number = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            user_profile = UserProfile.objects.create(
                user=user,
                mobile=self.cleaned_data['mobile'],
                course=self.cleaned_data['course'],
                semester=self.cleaned_data['semester'],
                batch=self.cleaned_data['batch'],
                roll_number=self.cleaned_data['roll_number']
            )
            user_profile.save()
        return user
