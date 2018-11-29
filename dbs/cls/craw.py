from lxml import html

class Craw:

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, url):
        self.__url = url

    def urlCraw(self):
        print(self.url)