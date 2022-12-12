from .models import UserProfile
from django.forms import ModelForm

class UserEditForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'