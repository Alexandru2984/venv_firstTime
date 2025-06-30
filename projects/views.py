from django.shortcuts import render
from .models import Project, GitHubRepo
import requests
from datetime import datetime
# Create your views here.

def home(request):
    projects = Project.objects.all()
    return render(request, 'projects/home.html', {
        'projects': projects,
        'current_year' : datetime.now().year
    })

def github_projects(request):
    username = "micutuco"  # înlocuiește cu userul tău
    url = f"https://api.github.com/users/{username}/repos"

    response = requests.get(url)
    if response.status_code == 200:
        repos = response.json()

        # Șterge toate repo-urile existente (dacă vrei să nu le dublezi)
        GitHubRepo.objects.all().delete()

        for repo_data in repos:
            GitHubRepo.objects.create(
                name=repo_data['name'],
                html_url=repo_data['html_url'],
                description=repo_data.get('description')
            )

    # Citește datele salvate în DB
    all_repos = GitHubRepo.objects.all()

    return render(request, 'projects/github_projects.html', {'repos': all_repos})

