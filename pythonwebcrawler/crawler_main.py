'''
Created on Jan 24, 2018

@author: DoubleL
'''
from pythonwebcrawler import html_downloader, html_parser, html_output, url_manager
from threading import Thread
from queue import Queue, Empty
from time import time

visisted = set()
queue = Queue()

class crawlerMainThread(object): 
    
    
    def __init__(self): # initialization
        self.urls = url_manager.urlManager()
        self.downloader = html_downloader.htmlDownloader()
        self.parser = html_parser.htmlParser()
        self.output = html_output.htmlOutput()

    def craw(self, root_url): # core crawing
        count = 1 # counting urls
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url(): # main loop (when it has new url)
            try:
                new_url = self.urls.get_new_url() # get a new url
                print("craw %d : %s" % (count, new_url)) # print out number of urls and url
                html_cont = self.downloader.download(new_url) # start download content from the new url
                new_urls, new_data = self.parser.parse(new_url, html_cont) # parse new crawed urls and data
                # analizing 
                self.urls.add_new_urls(new_urls) # add new crawed urls from new url
                self.output.collect_data(new_data) # store new data
                
                if count == 1000:
                    break
                count = count + 1
            except:
                print("crawing failure")
                count = count + 1 
        
        self.output.output_html() # output new data
        
if __name__ == "__main__":
    startTime = time()
    root_url = 'https://www.sfu.ca'
    obj_crawler = crawlerMainThread()
    obj_crawler.craw(root_url)
    endTime = time()
    print('Total time cost: %s' % (endTime - startTime))