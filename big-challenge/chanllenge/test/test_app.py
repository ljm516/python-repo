from chanllenge.util.chanllenge_utils import *

repo = UserRepo.get_user_repo('peewee-learn')
print
repo.name
readme = repo.get_readme('master')
print
readme

# the content encode by base64
print
Base64Decode.decode_string(readme.content)
