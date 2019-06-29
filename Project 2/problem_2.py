import os
from os import listdir
def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    lst=[]
    last_var=suffix
    if path:
        last_var=suffix+'/'+path
    for f in listdir(last_var):
        f1= last_var + '/' + f
        if os.path.isdir(f1):
            lst=find_files(last_var,f)

        elif os.path.isfile(f1) and f1.endswith(".c"):
             lst.append(f1)

    return lst

#Test case -1 
print(find_files('.', 'testdir-2'))
"""
output:['./testdir-2/subdir1/a.c']
"""
#Test case-2
print(find_files('.', 'testdir-2/subdir2'))
"""
outuput: [] As, there are no .c files present in the directory it returns an empty list
"""

#Test case-3
print(find_files('.', 'testdir-2/subdir3'))
"""
output:['./testdir-2/subdir3/subsubdir1/b.c']
"""


