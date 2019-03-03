class Article(object):
    """docstring for Article"""

    def __init__(self):
        self.__title = None
        self.__content = None

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, content):
        self.__content = content
