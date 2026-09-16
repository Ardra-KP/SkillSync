from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Project, Proposal

def home(request):
    developers = UserProfile.objects.filter(role__iexact='developer')[:4]
    for dev in developers:
        dev.skills_list = [s.strip() for s in dev.skills.split(',')] if dev.skills else []
    return render(request, 'accounts/home.html', {'developers': developers})

def developer_list(request):
    developers = UserProfile.objects.filter(role__iexact='developer')
    for dev in developers:
        dev.skills_list = [s.strip() for s in dev.skills.split(',')] if dev.skills else []
    return render(request, 'accounts/developers.html', {'developers': developers})

def project_list(request):
    projects = Project.objects.all().order_by('-id')
    return render(request, 'accounts/projects.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    has_applied = False
    if request.user.is_authenticated:
        has_applied = Proposal.objects.filter(project=project, developer=request.user).exists()

    if request.method == 'POST' and request.user.is_authenticated:
        cover = request.POST.get('cover_letter')
        bid = request.POST.get('bid_amount')
        # duplicate apply thadayan
        if not has_applied and cover and bid:
            try:
                bid_int = int(bid)
            except:
                bid_int = 0
            Proposal.objects.create(
                project=project,
                developer=request.user,
                cover_letter=cover,
                bid_amount=bid_int
            )
            return redirect('project_detail', pk=pk)

    return render(request, 'accounts/project_detail.html', {
        'project': project,
        'has_applied': has_applied
    })

def developer_detail(request, pk):
    profile = get_object_or_404(UserProfile, pk=pk)
    profile.skills_list = [s.strip() for s in profile.skills.split(',')] if profile.skills else []
    return render(request, 'accounts/developer_detail.html', {'profile': profile})

@login_required
def post_a_project(request):
    if request.method == 'POST':
        Project.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            budget=request.POST.get('budget'),
            skills_required=request.POST.get('skills_required'),
            posted_by=request.user
        )
        return redirect('my_projects')
    return render(request, 'accounts/post_a_project.html')

@login_required
def my_projects(request):
    projects = Project.objects.filter(posted_by=request.user).order_by('-id')
    return render(request, 'accounts/my_projects.html', {'projects': projects})

@login_required
def my_project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk, posted_by=request.user)
    proposals = project.proposals.all().order_by('-created_at')
    return render(request, 'accounts/my_project_detail.html', {
        'project': project,
        'proposals': proposals
    })

@login_required
def project_for_you(request):
    projects = Project.objects.exclude(posted_by=request.user).order_by('-id')[:20]
    return render(request, 'accounts/project_for_you.html', {'projects': projects})

@login_required
def my_profile(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    profile.skills_list = [s.strip() for s in profile.skills.split(',')] if profile.skills else []
    return render(request, 'accounts/my_profile.html', {'profile': profile})

@login_required
def edit_profile(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        profile.title = request.POST.get('title')
        profile.skills = request.POST.get('skills')
        profile.bio = request.POST.get('bio')
        profile.save()
        return redirect('my_profile')
    return render(request, 'accounts/edit_profile.html', {'profile': profile})