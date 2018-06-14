import os

def get_file_list(dir):
    flist = os.listdir(dir)
    flist_ret = []
    for ifile in flist:
        flist_ret.append(dir + '/' + ifile)
    return flist_ret