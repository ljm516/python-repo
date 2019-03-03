class Api(object):
    def __init__(self, name, request_url, response_obj, method, desc, parameters):
        self.name = name
        self.request_url = request_url
        self.response_obj = response_obj
        self.method = method
        self.parameters = parameters
        self.desc = desc


class RequestParameter(object):
    def __init__(self, name, para_type, field):
        self.name = name
        self.para_type = para_type
        self.field = field


class MarkDownData(object):
    def __init__(self, title, api_list):
        self.title = title
        self.api_list = api_list


