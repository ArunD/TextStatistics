import os
class TextParser:

    #def __init__(self, tmp_dir):
    #    self.tmp_dir = tmp_dir

    def parse(self,document):
        #f = open('/mnt/c/Users/arund/OneDrive/Desktop/PetPRojects/FileStorage/user_2/ocrData/Q3_XlqRhcF.txt')
        #doc_path = os.path.join(self.tmp_dir,document.name)
        f = open(document,'r')
        wcl = {}
        t = []
        nl = 0
        l = 0
        wc = 0
        tu = []
        for line in f:
            #print(line)
            nl += 1
            if(not (line.startswith('\n') or line.startswith(' \n') )):
                l += 1
                t = line.strip('\n').split(' ')
                for w in t:
                    wc += 1
                    if w in wcl:
                        wcl[w] += 1
                    else :
                        wcl[w] = 1

        f   .close()
        print(wcl)

        for k,v in wcl.items():
            tu.append((k,v))

        stu = sorted(tu,key=lambda wv : wv[1],reverse=True)

        return({'nl' : nl , 'l' : l , 'wc' : wc , 'tu' : stu})
        #wf = open('/mnt/c/Users/arund/OneDrive/Desktop/PetPRojects/Udemy/WordCounter/wcl.txt','w')
        #print('Total no of lines(including Blank) : '+str(nl),file=wf)
        #print('Total no of lines : '+str(l),file=wf)
        #print('Total no of words : '+str(wc),file=wf)
        #print('************************************************************',file=wf)
        #print('Word : Count',file=wf)

        #for val in stu:
        #    print(val[0] +':' + str(val[1]),file=wf)
        #wf.close
