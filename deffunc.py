#! /usr/bin/python

def get_information(*cmd):
    global test_result
    test_result = []
    test_result.append(cmd)
    for i in range(20):
        test_result.append(i)
    test_result.append('-'*80)
    #print(test_result)

#get_information()

def write_into_file(id):
    with open(id, 'w') as f:
        for content in test_result:
            f.write(str(content))
        f.write('\n')
    we = open(id).read()
    print(we) 

#get_information('add string')
#write_into_file('00001')
#
#get_information()
#write_into_file('00002')
