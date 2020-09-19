import time
from selenium.webdriver import Chrome, Firefox, Ie

from settings import (
    CHROMEDRIVER_PATH, 
    GECKODRIVER_PATH,
    IEDRIVER_PATH,
    SLEEP_TIME_FOR_LOGIN, 
    SLEEP_TIME_FOR_NEXT_PAGE
)


class SingletonMetaclass(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(SingletonMetaclass, cls).__call__(*args, **kwargs)

        return cls.__instances[cls]


class Browser:
    ALIEXPRESS_LOGIN_URL = "https://login.aliexpress.ru/"

    def login(self):
        self._browser.get(self.ALIEXPRESS_LOGIN_URL)
        time.sleep(SLEEP_TIME_FOR_LOGIN)

    def get_page(self, url):
        self._browser.get(url)
        time.sleep(SLEEP_TIME_FOR_NEXT_PAGE)
        return self._browser.page_source


class ChromeBrowser(Browser, metaclass=SingletonMetaclass):
    def __init__(self):
        self._browser = Chrome(executable_path=CHROMEDRIVER_PATH)
        self.login()



class FirefoxBrowser(Browser, metaclass=SingletonMetaclass):
    def __init__(self):
        self._browser = Firefox(executable_path=GECKODRIVER_PATH)
        self.login()


class IeBrowser(Browser, metaclass=SingletonMetaclass):
    def __init__(self):
        self._browser = Ie(executable_path=IEDRIVER_PATH)
        self.login()