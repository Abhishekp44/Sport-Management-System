from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Player, Team, Coach, Schedule
from .forms import PlayerForm, CoachLoginForm, TeamForm, ScheduleForm, AddTeamForm
from django.contrib import messages

# Player Registration
def register_player(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Player registered successfully!')
            return redirect('register_player')
    else:
        form = PlayerForm()
    return render(request, 'register_player.html', {'form': form})

# Coach Authentication
def coach_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('coach_dashboard')  
        else:
            return render(request, 'coach_login.html', {'error': 'Invalid login credentials'})
    return render(request, 'coach_login.html') 

#coach logout
def coach_logout(request):
    logout(request)
    return redirect('/login')

#coach dashboard
@login_required
def coach_dashboard(request):
    teams = Team.objects.all() 
    schedules = Schedule.objects.all()
    
    if request.method == "POST":
        form = AddTeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('coach_dashboard')  
    else:
        form = AddTeamForm()  

    return render(request, 'coach_dashboard.html', {
        'teams': teams,
        'schedules': schedules,
        'form': form, 
    })

#add team schedule
def add_schedule(request):
    if request.method == "POST":
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('coach_dashboard') 
    else:
        form = ScheduleForm() 
    return render(request, 'manage_schedule.html', {'form': form})  

#edit team schedule
def edit_schedule(request, id):
    schedule = get_object_or_404(Schedule, id=id)

    if request.method == 'POST':
        form = ScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            return redirect('coach_dashboard')  
    else:
        form = ScheduleForm(instance=schedule)

    return render(request, 'schedule_form.html', {'form': form})

#delete
def delete_schedule(request, id):
    schedule = get_object_or_404(Schedule, id=id)
    schedule.delete()
    return redirect('coach_dashboard')

#add team
def add_team(request):
    if request.method == "POST":
        form = AddTeamForm(request.POST)  
        if form.is_valid():
            form.save()
            return redirect('dashboard')  
    else:
        form = AddTeamForm() 
    return render(request, 'add_team.html', {'form': form})

#view team details
def team_details(request, id):
    team = get_object_or_404(Team, id=id)  
    return render(request, 'team_details.html', {'team': team})

#edit team 
def edit_team(request, id):
    team = get_object_or_404(Team, id=id)  

    if request.method == 'POST':
        form = AddTeamForm(request.POST, instance=team)  
        if form.is_valid():
            form.save()  
            return redirect('coach_dashboard')  
    else:
        form = AddTeamForm(instance=team)

    return render(request, 'edit_team.html', {'form': form, 'team': team})  

#delete team
def delete_team(request, id):
    team = get_object_or_404(Team, id=id) 
    team.delete()  
    return redirect('coach_dashboard')  

