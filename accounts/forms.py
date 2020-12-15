from django.contrib.auth.forms import (
    UserCreationForm
)
from accounts.models import Profile
from django.forms import ImageField
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
