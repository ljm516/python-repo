import base64
import codecs
import os

from github import Github
from jinja2 import Template
from chanllenge.util.wayknew import *

template = Template('''
## {{api_name}}

**description**

```
{{desc}}
```
**method**

```
{{method}}
```
**URL**

```
{{url}}
```
**parameters**

```
{{parameters}}
```
**response**

```
{{response}}
```
''')


class UserRepo(object):
    @classmethod
    def get_user_repo(cls, username, password, repo_name):
        g = Github(username, password)
        return g.get_user().get_repo(repo_name)


class Base64Decode(object):
    @classmethod
    def decode_string(cls, content):
        return base64.b64decode(content)


def transform_p_to_dict(p):
    return {
        'name': p.name.replace('\'', '"'),
        'type': p.para_type.replace('\'', '"'),
        'field': p.field.replace('\'', '"')
    }


def transform_parameter_to_dict(parameters):
    l = []
    for p in parameters:
        l.append(transform_p_to_dict(p))
    return l


def transform_to_dict(api):
    return {
        "name": api.name.replace('\'', '"'),
        "requestUrl": api.request_url.replace('\'', '"'),
        "response_obj": api.response_obj.replace('\'', '"'),
        "method": api.method.replace('\'', '"'),
        "parameters": transform_parameter_to_dict(api.parameters),
        "desc": api.desc.replace(' ', '')
    }


def transform_to_markdown(d, api_repo):
    markdown_file = os.path.dirname(os.path.realpath(__file__)) + '/api_doc/' + api_repo + '_api.md'
    markdown_doc = '# ' + api_repo + ' api document'
    for key in d.keys():
        api = d[key]
        parameters = api['parameters']
        md_api_parameters = ''
        for p in parameters:
            if p['field'] == '' or p['field'] is None:
                md_api_parameters += p['type'] + ' ' + p['name'] + '\n'
            else:
                md_api_parameters += p['type'] + ' ' + p['name'] + '\n' + p['field'] + '\n'

        markdown_doc += template.render(api_name=api['name'], desc=api['desc'], method=api['method'],
                                        url=api['requestUrl'],
                                        parameters=md_api_parameters, response=api['response_obj'])

    with codecs.open(markdown_file, 'w', 'UTF-8') as output_file:
        output_file.write(markdown_doc)

    print('api document build finished!')

    write_to_wayknew(api_repo, markdown_doc)
