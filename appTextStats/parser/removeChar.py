import os
import re
import string
class RemoveCharParser:

    #def __init__(self, tmp_dir):
    #    self.tmp_dir = tmp_dir

    def parse(self,document,charList):

        pattern = '\r'
        carriage = "\r"
        newLine = "\n"
        space = "\s"
        tab = "\t"

        pattern = ''.join(charList)
        pattern = pattern + "\r"
        pattern = '[%s]+' % pattern
        #legal_chars = '[^%s\s\n]+' % re.escape(legal_chars)
                
        f = open(document,'r')
        c = f.read()
        print(pattern)

        op = re.sub(pattern,r'',c)
        f.close()
        return({'removeChar' : op})

        