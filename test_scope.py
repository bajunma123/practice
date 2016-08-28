#! /usr/bin/python

class Test():
    def __init__(self, *cmd):
        self.cmd = cmd
        pass
    
    def get_information(self):
        global test_result
        test_result = []
        test_result.append(self.cmd)
        for i in range(20):
            test_result.append(i)
        test_result.append('-'*80)
        print(test_result)
#p = Test()
#p.get_information()
#print(test_result)
#t = Test('add string')
#t.get_information()
#print(test_result)
