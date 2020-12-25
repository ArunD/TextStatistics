import os
import re
import string
class SpecialCharParser:

    #def __init__(self, tmp_dir):
    #    self.tmp_dir = tmp_dir

    def parse(self,document):
        
        f = open(document,'r')
        c = f.read()
        #print(c)
        legal_chars =  string.ascii_letters + string.digits
        legal_chars = '[^%s\n]+' % re.escape(legal_chars)

        l = re.findall(legal_chars,c)
        s = ' '.join(set(l))
        f.close()
        return({'specialChar' : s})

        