'''
Created on Jan 24, 2018

@author: DoubleL
'''
class htmlOutput(object):
    
    
    def __init__(self):
        self.datas = []
    
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    
    def output_html(self):
        fileout = open('/Users/DoubleL/Desktop/result.html', 'w')
        
        fileout.write("<html>")
        fileout.write("<body>")
        fileout.write("<table>")
        
        # ascii
        count = 0
        for data in self.datas:
            fileout.write("<tr>")
            fileout.write("<a href='%s'>%d</a>" % (data['url'], count))
            fileout.write("</tr>")
            fileout.write("<br>")
            count = count + 1
            
        fileout.write("</table>") 
        fileout.write("</body>")
        fileout.write("</html>")
    
    
    
    
    
