'''
Created on Jan 24, 2018

@author: DoubleL
'''
class urlManager(object):
    def __init__(self):
        self.new_urls = set() # list for new crawed urls
        self.old_urls = set() # list for already crawed urls
    
    def add_new_url(self, url): # one url
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
    
    def add_new_urls(self, urls): # multiple urls
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)
            
    def has_new_url(self):
        return len(self.new_urls) != 0 # len == 0 then there is no url
    
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url