def custombasename(fullname):
    return os.path.basename(os.path.splitext(fullname)[0])
#fullname = '/mnt/nfshome1/FRACTAL/vijay.dubey/Dev_Kit/DOTA_devkit-master/example/labelTxt/P0039.txt'
#returns P0039

def GetFileFromThisRootDir(dir,ext = None):
'''Can also filter for a given extension'''
    allfiles = []
    needExtFilter = (ext != None)
    for root,dirs,files in os.walk(dir):
        for filespath in files:
            filepath = os.path.join(root, filespath)
            extension = os.path.splitext(filepath)[1][1:]
            if needExtFilter and extension in ext:
                allfiles.append(filepath)
            elif not needExtFilter:
                allfiles.append(filepath)
    return allfiles
