import os

class BasicSearchEngine:
    def __init__(self, cache):
        #implement cache
        self.index = {}
        self.web_pages = {}

    def index_web_pages(self, folder):
        if not os.path.exists(folder):
            return f"Invalid Directory {folder}"




# print(os.path.exists("web_pages"))