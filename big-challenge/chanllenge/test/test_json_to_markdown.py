import codecs
import os

import simplejson as json
from jinja2 import Template

markdown_json = os.path.dirname(os.path.realpath(__file__)) + '/markdown.json'
markdown_file = os.path.dirname(os.path.realpath(__file__)) + '/test_api.md'
# MARKDOWN_TEMPLATE = '# yolar api document'

api_dict = json.load(codecs.open(markdown_json, "r", "utf-8"))

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

doc = '# yolar api doc\n'
for key in api_dict.keys():
    api = api_dict[key]
    parameters = api['parameters']
    md_api_parameters = ''
    for p in parameters:
        if p['field'] == '' or p['field'] is None:
            md_api_parameters += p['type'] + ' ' + p['name'] + '\n'
        else:
            md_api_parameters += p['type'] + ' ' + p['name'] + '\n' + p['field'] + '\n'
    doc += template.render(api_name=api['name'], desc=api['desc'], method=api['method'], url=api['requestUrl'],
               parameters=md_api_parameters, response=api['response_obj'])

with codecs.open(markdown_file, 'w', 'UTF-8') as output_file:
    output_file.write(doc)


