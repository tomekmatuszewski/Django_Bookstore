from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.transaction import atomic
from django.forms import ImageField, ModelForm

from accounts.models import Profile


class SingUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ["username", "first_name"]

    @atomic
    def save(self, commit=True):
        self.instance.is_active = False
        result = super().save(commit)
        profile = Profile(user=result)
        if commit:
            profile.save()
        return result


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]


class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["image"]
