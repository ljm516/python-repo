import sys

import javalang

from chanllenge.data_handler.query_field_from_halo import *
from chanllenge.module.module import *

CONTROLLER_CONTENT_LIST = []
username = ''
password = ''

if len(sys.argv) != 2:
    print('format [yolar/galaxy]')
    exit(-1)


# recursive get controller.java in repo, set in a list
def get_controller_file(repo, path):
    content_file_list = repo.get_contents(path, 'master')
    for content_file in content_file_list:
        if content_file.type == 'file' and 'Application' in content_file.name:
            continue
        if content_file.type == 'file' and 'YHJExceptionController' in content_file.name:
            continue
        if content_file.type == 'file' and 'BaseController' in content_file.name:
            continue
        if content_file.type == 'file' and 'Controller' in content_file.name:
            print('add ' + content_file.name + ' to list')
            CONTROLLER_CONTENT_LIST.append(content_file)
        if content_file.type == 'dir':
            get_controller_file(repo, content_file.path)

    return CONTROLLER_CONTENT_LIST


def init_markdown(md):
    d = {}
    api_list = md.api_list
    for controller_api_list in api_list:
        for controller_api in controller_api_list:
            d[controller_api.name.replace('\'', '"')] = transform_to_dict(controller_api)

    d = query_field_from_halo(username, password, d, sys.argv[1])
    transform_to_markdown(d, sys.argv[1])


def get_repo_content(uname, pwd, git_repo_name):
    md = MarkDownData
    repo = UserRepo.get_user_repo(uname, pwd, git_repo_name)
    if repo.name == 'CurvatureDrive':
        path = 'src/main/java/com/youhujia/curvature'
    elif '-' in repo.name:
        if repo.name == 'wall-breaker':
            path = 'src/main/java/com/youhujia/wbreaker'
        elif repo.name == 'phantom-countdown':
            path = 'src/main/java/com/youhujia/bye'
        else:
            path = 'src/main/java/com/youhujia/' + repo.name.replace('-', '')
    elif repo.name == 'cms':
        path = 'src/main/java/com/youhujia'

    else:
        path = 'src/main/java/com/youhujia/' + sys.argv[1]
    controller_list = get_controller_file(repo, path)

    md.title = sys.argv[1] + ' api document'
    md.api_list = deal_controller_content(controller_list)
    init_markdown(md)


def deal_controller_content(controller_list):
    api_dict_tuple = []
    if len(controller_list) > 0:
        for controller_content in controller_list:
            api_dict_tuple.append(transform_to_api_list(controller_content))

    return api_dict_tuple


def get_need_class_annotations(class_declaration):
    class_annotation_list = class_declaration[0].annotations
    need_annotation_list = []
    for class_annotation in class_annotation_list:
        if class_annotation.name != 'Service':
            need_annotation_list.append(class_annotation)

    return need_annotation_list


def transform_to_api_list(controller_content):
    # how deal with this content -> use python third library: javalang
    java_code = Base64Decode.decode_string(controller_content.content)
    tree = javalang.parse.parse(java_code)

    class_declaration = tree.types
    class_name = class_declaration[0].name
    print('Controller name ' + class_name)
    need_class_annotations = get_need_class_annotations(class_declaration)
    class_request_url = get_class_request_url(need_class_annotations)
    class_methods = class_declaration[0].methods
    api_list = []
    for method in class_methods:
        method_annotation = method.annotations
        if len(method_annotation) == 0:
            continue
        for annotation in method_annotation:
            if annotation.name != 'RequestMapping':
                method_annotation.remove(annotation)

        if len(method_annotation) == 0:
            continue
        annotation_element = method_annotation[0].element
        a = Api('', '', '', '', '', None)
        a.name = method.name
        a.desc = get_method_desc(method)
        a.request_url = get_method_request_url(annotation_element, class_request_url)
        a.method = get_request_method(annotation_element)
        a.response_obj = get_return_obj(method)
        a.parameters = get_request_parameter(method)
        api_list.append(a)

    return api_list


def get_class_request_url(class_annotation):
    if len(class_annotation) > 1:
        class_element = class_annotation[1].element
        if isinstance(class_element, list):
            class_request_url = class_element[0].value.value
        elif class_element is None:
            class_request_url = ''
        else:
            class_request_url = class_element.value
    else:
        class_request_url = ''

    return class_request_url


def get_method_desc(method):
    if method.documentation is None:
        return 'null'
    else:
        return method.documentation


def get_method_request_url(annotation_element, class_request_url):
    if isinstance(annotation_element, list):
        if annotation_element[0].value.value != '""':
            url = class_request_url + annotation_element[0].value.value
        else:
            url = class_request_url
    else:
        if annotation_element.value != '""':
            url = class_request_url + annotation_element.value
        else:
            url = class_request_url

    return url.replace('"', '')


def get_request_method(annotation_element):
    if isinstance(annotation_element, list):
        if len(annotation_element) > 1:
            return annotation_element[1].value.member
        else:
            return ''
    else:
        return ''


def get_return_obj(method):
    if method.return_type.sub_type is None:
        return method.return_type.name
    else:
        return method.return_type.name + '.' + method.return_type.sub_type.name


def get_request_parameter(method):
    class_parameters = method.parameters
    parameters = []
    for parameter in class_parameters:
        p = RequestParameter('', '', '')
        p.name = parameter.name
        para_arguments = parameter.type.arguments
        arg = ''
        if para_arguments is None:
            if parameter.type.sub_type is None:
                p.para_type = parameter.type.name
            else:
                p.para_type = parameter.type.name + '.' + parameter.type.sub_type.name
        else:
            if len(para_arguments) > 1:
                arg = '<' + para_arguments[0].type.name + ', ' + para_arguments[1].type.name + '>'
            if len(para_arguments) == 1:
                if para_arguments[0].type.sub_type is None:
                    arg = '<' + para_arguments[0].type.name + '>'
                else:
                    arg = '<' + para_arguments[0].type.name + '.' + para_arguments[0].type.sub_type.name + '>'
            if arg == '':
                if parameter.type.sub_type is None:
                    p.para_type = parameter.type.name
                else:
                    p.para_type = parameter.type.name + '.' + parameter.type.sub_type.name
            else:
                p.para_type = parameter.type.name + arg

        parameters.append(p)
    return parameters


if __name__ == '__main__':
    print('please enter your github username:')
    username = input()
    print('please enter your github pasword')
    password = input()
    get_repo_content(username, password, sys.argv[1])
