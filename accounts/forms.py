from django.contrib.auth.forms import (
    UserCreationForm
)
from django.contrib.auth.models import User

from accounts.models import Profile
from django.forms import ImageField, ModelForm
from django.db.transaction import atomic


class SingUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name']

    image = ImageField()

    @atomic
    def save(self, commit=True):
        self.instance.is_active = False
        result = super().save(commit)
        image = self.cleaned_data['image']
        profile = Profile(image=image, user=result)
        if commit:
            profile.save()
        return result


class UserUpdateForm(ModelForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ProfileUpdateForm(ModelForm):

    class Meta:
        model = Profile
        fields = ['image']