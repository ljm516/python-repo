from github import Github

g = Github('ljm516', 'password')

for repo in g.get_user().get_repos():
    print(repo.name)
