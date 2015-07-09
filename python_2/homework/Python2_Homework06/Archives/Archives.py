import os
import glob
import zipfile


def archivedir(path):
    '''
    This function takes a directory path and
    creates an archive of the directory only.
    '''
    basedir = os.path.dirname(path)
    relativedir = os.path.basename(path)

    startpath = os.curdir
    os.chdir(basedir)

    # Select files to compress
    filenames = glob.glob(os.path.join(relativedir, "*"))
    for fn in filenames:
        if not os.path.isfile(basedir + '\\' + fn):
            filenames.remove(fn)

    # Make archive and compress files
    archive_fn = path + ".zip"
    
    zf = zipfile.ZipFile(archive_fn, "w")
    for fn in filenames:
        zf.write(fn)

    # close the zip file
    zf.close()

    os.chdir(startpath)