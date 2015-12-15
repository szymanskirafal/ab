
from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group


from .forms import NewGroupForm, NewMemberForm





@login_required
def grupa(request):
    current_user = request.user
    grupy = current_user.groups.all()
    return render(request, 'grupa/grupa.html', {
        'current_user': current_user,
        'grupy': grupy})




@login_required
def nowa(request):
    group_creator = request.user
    if request.method == 'POST':
        form = NewGroupForm(request.POST)
        if form.is_valid():
            group_name = form.cleaned_data['group_name']
            new_group = Group.objects.create(name=group_name)
            new_group.user_set.add(group_creator)

            return HttpResponseRedirect('/dodane/')
    else:
        form = NewGroupForm()

    return render(request, 'grupa/new_group.html', {'form': form})


@login_required
def group(request, group_name):
    group = Group.objects.get(name = group_name)
    members = group.user_set.all()

    return render(request, 'grupa/group.html',
        {
            'group_name': group_name,
            'members': members
            })

@login_required
def add_new_member(request, group_name):
    if request.method == 'POST':
        form = NewMemberForm(request.POST)
        if form.is_valid():
            new_member = form.cleaned_data['new_member_name']
            group = Group.objects.get(name=group_name)
            group.user_set.add(new_member)

            return HttpResponseRedirect('/dodane/')
    else:
        form = NewMemberForm()

    return render(request, 'grupa/new_member.html', {'form': form})
