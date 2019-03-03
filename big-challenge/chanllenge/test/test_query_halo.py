import re

from chanllenge.util.chanllenge_utils import *

repo_name = 'halo'

repo = UserRepo.get_user_repo(repo_name)
path = 'src/main/resources/yolar.proto'

proto_file = repo.get_contents(path, 'master')

yolar_proto = proto_file.content
proto_str = Base64Decode.decode_string(yolar_proto).decode('utf-8')

pattern = re.compile('.*?message (.*?)\s?{\n(.*?)\n}.*?', re.S)
message_list = re.findall(pattern, proto_str)
for message in message_list:
    print('message ' + message[0] + ' {' + message[1] + '}')
