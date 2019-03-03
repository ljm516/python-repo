import sys

from git_collaborator.git_utils import *

# when run this script, need two parameters, the no.1 is repo name and the no.2 is your github name

if len(sys.argv) != 3:
    print('repo name and your github name is necessary')
    exit(-1)


def add_member(repo_name, member_name):
    repo = get_user_repo(repo_name)
    if repo is None:
        print('repo > ' + repo_name + ' not exist')
        exit(-1)
    repo.add_to_collaborators(member_name)
    print('add ' + repo.name + ' success')


if __name__ == '__main__':
    add_member(sys.argv[1], sys.argv[2])
