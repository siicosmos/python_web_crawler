'''
Created on Jan 24, 2018

@author: DoubleL
'''
import urllib.request
class htmlDownloader(object):
    
    
    def download(self, url):
        if url is None:
            return None
        
        response = urllib.request.urlopen(url)
        
        if response.getcode() != 200:
            return  None
        return response.read()
    
