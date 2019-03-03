import ast
import re

import github

from chanllenge.util.chanllenge_utils import *

type_list = ['int64', 'string', 'bool', 'int32']
repo_name = 'halo'
pattern = re.compile('.*?message (.*?)\s?{\n(.*?)\n}.*?', re.S)
upper_pattern = re.compile('')
api_contained_message_dict = {}
proto_message_dict = {}
result = 'message Result {\n optional bool success = 1;\n optional int64 code = 2;\n}'


def get_halo_proto_content(username, pwd, current_build_repo, para_type, repo):
    if para_type == 'shooter':
        return get_halo_proto_content_from_itself(username, pwd, current_build_repo, para_type)
    if para_type == 'msg':
        para_type = 'singer'
    if para_type == 'hf':
        para_type = 'huformation'
    if para_type == 'taskengine':
        para_type = 'sophon'
    print('get halo proto ing....')
    path = 'src/main/resources/' + para_type + '.proto'
    try:
        proto_file = repo.get_contents(path, 'master')
    except github.UnknownObjectException:
        print(para_type + '.proto not in halo, maybe find in itself')
        return get_halo_proto_content_from_itself(username, pwd, current_build_repo, para_type)
    return proto_file.content


def get_halo_proto_content_from_itself(username, pwd, current_build_repo, para_type):
    print('get proto from current build repo ing...')
    current_repo = UserRepo.get_user_repo(username, pwd, current_build_repo)
    path = 'src/main/resources/' + para_type + '.proto'
    try:
        proto_file = current_repo.get_contents(path, 'master')
        return proto_file.content
    except github.UnknownObjectException:
        print(para_type + '.proto also not in ' + current_repo.name + ', I can not find it, must be proto error')
        exit(-1)


def build_proto_dict(username, pwd, current_build_repo, para_type, repo):
    proto_content = get_halo_proto_content(username, pwd, current_build_repo, para_type, repo)
    proto_str = Base64Decode.decode_string(proto_content).decode('UTF-8')
    message_list = re.findall(pattern, proto_str)
    for message in message_list:
        proto_message_dict[message[0]] = message[1]
    print('build proto dict success')
    return proto_message_dict


def remove_some_char(content):
    return content.replace('*', '').replace('@', '').replace('', '')


def transform_string_dict(string_content):
    return ast.literal_eval(string_content)


def query_field_from_halo(git_username, git_password, d, dist_name):
    repo = UserRepo.get_user_repo(git_username, git_password, repo_name)
    username = git_username
    pwd = git_password
    proto_dict = {}
    if dist_name == 'CurvatureDrive':
        proto_type = 'curvature'
    elif '-' in dist_name:
        if dist_name == 'phantom-countdown':
            proto_type = 'bye'
        else:
            proto_type = dist_name.replace('-', '')
    elif dist_name == 'redcoast':
        proto_type = 'followup'
    else:
        proto_type = dist_name

    if dist_name != 'wall-breaker':
        proto_dict = build_proto_dict(git_username, git_password, dist_name, proto_type, repo)

    for key in d:
        controller = d[key]
        if '.' in controller['response_obj']:
            message_name = controller['response_obj'].split('.')[1]
            message_type = controller['response_obj'].split('.')[0]
            if message_type.lower() != dist_name:
                print('build other dict....')
                other_dict = build_proto_dict(username, pwd, dist_name, message_type.lower(), repo)
                controller['response_obj'] = remove_some_char(
                    'message ' + message_name + ' { \n' + other_dict[message_name] + '\n}')
            else:
                if message_name in proto_dict.keys():
                    controller['response_obj'] = remove_some_char(
                        'message ' + message_name + ' { \n' + proto_dict[message_name] + '\n}')
        parameters = controller['parameters']
        for para in parameters:
            if '.' in para['type']:
                if '>' in para['type']:
                    if para['type'].split('.')[1][:-1] not in proto_dict.keys():
                        print('build other parameter dict....no.1 condition')
                        other_parameter_dict = build_proto_dict(username, pwd, dist_name, para['type'].split('.')[0]
                                                                .split('<')[1].lower(), repo)
                        para['field'] = remove_some_char(
                            'message ' + para['type'].split('.')[1][:-1] + ' { \n' + other_parameter_dict[
                                para['type'].split('.')[1][:-1]] + '\n}')
                    else:
                        para['field'] = remove_some_char(
                            'message ' + para['type'].split('.')[1][:-1] + ' { \n' + proto_dict[
                                para['type'].split('.')[1][:-1]] + '\n}')
                else:
                    if para['type'].split('.')[1] not in proto_dict.keys():
                        print('build other parameter dict....no.2 condition')
                        other_parameter_dict = build_proto_dict(username, pwd, dist_name, para['type'].split('.')[0].lower(), repo)
                        para['field'] = remove_some_char(
                            'message ' + para['type'].split('.')[1] + ' { \n' + other_parameter_dict[
                                para['type'].split('.')[1]] + '\n}')
                    else:
                        para['field'] = remove_some_char('message ' + para['type'].split('.')[1] + ' { \n' + proto_dict[
                            para['type'].split('.')[1]] + '\n}')

    return deal_api_dto_option(d)


def deal_api_dto_option(d):
    for key in d.keys():
        api = d[key]
        response_obj = api['response_obj']
        line_list = response_obj.split('\n')
        api['response_obj'] += get_optional_object_field(line_list)
        parameters = api['parameters']
        for p in parameters:
            if '.' in p['type']:
                field = p['field']
                field_line_list = field.split('\n')
                p['field'] += get_optional_object_field(field_line_list)

    return d


def get_optional_object_field(optional_list):
    optional_object_field = ''
    for line in optional_list:
        if 'optional' in line or 'repeated' in line:
            word_list = remove_none_in_line(line)
            if len(word_list) < 1:
                continue
            # if not isinstance(word_list, list):
            #     continue
            for word in word_list:
                if word == '':
                    continue
                if word not in type_list and word in proto_message_dict.keys():
                    is_exist_optional = '\nmessage ' + word + '{\n' + proto_message_dict[word] + '\n}'
                    if is_exist_optional not in optional_object_field:
                        optional_object_field += '\nmessage ' + word + '{\n' + proto_message_dict[word] + '\n}'
                        if word not in proto_message_dict.keys():
                            sub_message = proto_message_dict[word]
                            if word in sub_message:
                                continue
                            optional_object_field = optional_object_field + '\n' + get_optional_object_field(
                                sub_message.split('\n'))

    return optional_object_field


def remove_none_in_line(word_line):
    l = []
    for w in word_line.split(' '):
        if w != '':
            l.append(w)
    return l

