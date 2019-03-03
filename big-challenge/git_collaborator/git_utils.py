from github import Github

TOKEN = 'your github token'


def connect_github():
    return Github(TOKEN)


def get_user_repo(repo_name):
    g = connect_github()
    return g.get_user().get_repo(repo_name)
