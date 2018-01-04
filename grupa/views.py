
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User


from .forms import DeleteGroupForm, NewGroupForm, NewMemberForm, MemberForm
from .models import CustomGroup





@login_required
def grupy(request):
    current_user = request.user

    groups_created_by_current_user = CustomGroup.objects.all().filter(group_creator = current_user)

    # sprawdz czy current user jest group_creator ktorejs z grup
    # jesli tak, to wyszczególnij te grupy
    # jesli nie, to lepiej nie pisac calego akapitu

    grupy = current_user.groups.all()
    return render(request, 'grupa/grupy.html', {
        'current_user': current_user,
        'groups_created_by_current_user': groups_created_by_current_user,
        'grupy': grupy,
        })




@login_required
def nowa(request):
    group_creator = request.user
    if request.method == 'POST':
        form = NewGroupForm(request.POST)
        if form.is_valid():
            group_name = form.cleaned_data['group_name']
            new_group = CustomGroup.objects.create(name=group_name, group_creator = request.user.username)
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
def group_created(request, group_name):
    current_user = request.user
    group = CustomGroup.objects.get(name = group_name)
    group_creator = group.group_creator
    if not request.user.username == group_creator:
        return HttpResponseRedirect('/accounts/profile/')
    else:
        members = group.user_set.all()

        return render(request, 'grupa/group_created.html', {
            'current_user': current_user,
            'group_name': group_name,
            'members': members})

@login_required
def delete_group(request, group_name):
    group = CustomGroup.objects.get(name = group_name)
    group_creator = group.group_creator
    if not request.user.username == group_creator:
        return HttpResponseRedirect('/accounts/profile/')
    else:
        form = DeleteGroupForm(instance = group)
        if request.method == 'POST':
            form = DeleteGroupForm(request.POST, instance = group)
            if form.is_valid():
                group.delete()
                return HttpResponseRedirect('/dodane/')

        members = group.user_set.all()
        return render(request, 'grupa/delete_group.html', {
            'group_name': group_name,
            'members': members,
            'form': form,
            })



@login_required
def add_member(request, group_name):

    group = CustomGroup.objects.get(name = group_name)
    group_creator = group.group_creator
    if not request.user.username == group_creator:
        return HttpResponseRedirect('/accounts/profile/')


    if request.method == 'POST':
        form = NewMemberForm(request.POST)
        if form.is_valid():
            new_member_name = form.cleaned_data['new_member_name']
            users_names = []
            all_users = User.objects.all()
            for user in all_users:
                users_names.append(user.username)
            if new_member_name in users_names:
                new_member = User.objects.get(username = new_member_name)

                new_member.groups.add(group)
                return HttpResponseRedirect('/dodane/')
            else:
                return HttpResponseRedirect('/niedodane/')

    else:
        form = NewMemberForm()

    return render(request, 'grupa/add_member.html', {'form': form})


@login_required
def member(request, group_name, member):
    member_object = User.objects.get(username = member)
    form = MemberForm(instance = member_object)
    if request.method == 'POST':
        form = MemberForm(request.POST, instance = member_object)
        if form.is_valid():
            member_name = form.cleaned_data['username']
            member = User.objects.get(username = member_name)
            group = CustomGroup.objects.get(name = group_name)
            group.user_set.remove(member)
            return HttpResponseRedirect('/dodane/')



    return render(request, 'grupa/member.html',
        {
            'group_name': group_name,
            'member': member,
            'member_object': member_object,
            'form': form,
            })




