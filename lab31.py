## --- TASK 1 ---##
def string_to_seconds(t): # function to convert mm:ss to ss
    """Returns seconds from time."""
    m, s = t.split(':')
    if int(s) >= 60 or len(t) != 2:
        return int(m) * 60 + int(s)
# Test for task 1
#print(string_to_seconds('4:50'))

## --- TASK 2 ---##
## A ##
def read_library(file):
    lib = open(file, 'r')
    print(lib.read())
    lib.close()
    
#Test for task 2.a
# read_library('80s_library.txt')

## B ##
