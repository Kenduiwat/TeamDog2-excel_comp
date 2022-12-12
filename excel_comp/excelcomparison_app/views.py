from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from django.forms.models import model_to_dict
from .models import UserProfile
from .forms import UserEditForm

def userEdit(request, user_id):
    user = get_object_or_404(Question, pk=user_id)
    if request.method == "GET":
        form = UserEditForm(initial=model_to_dict(user))
        return render(request, 'yourapp/useredit_form.html', {'form':form)
    elif request.method == "POST":
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
             form.save()
             return HttpResponseRedirect(reverse('user_profile', kwargs={'uid':user.id}))
        else:
             return HttpResponseRedirect(reverse('some_fail_loc'))