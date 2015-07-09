'''
filewriter.py: Write a program that creates a ten megabyte data file
in two different ways and time each method. The first technique should
create a memory-mapped file and write the data by setting one chunk
at a time using successively higher indexes. The second technique
should create an empty binary file and repeatedly use the write() method 
to write a chunk of data. Show how the timings vary with the size of the chunk.
'''

import mmap
import os
from timeit import Timer


def file_mmap(file_name, file_size, chunk_size):
    ''' Create a file with memory map '''
    chunk_data = chunk_size * b'*'
    with open(file_name, 'w+b') as f:
        mapf = mmap.mmap(f.fileno(), file_size, access=mmap.ACCESS_WRITE)
        i = 0
        while i + chunk_size < file_size:
            j = i + chunk_size
            mapf[i:j] = chunk_data
            i = j
        mapf.close()
    os.unlink(file_name)


def file_fwrite(file_name, file_size, chunk_size):
    ''' Create a file using write() method '''
    chunk_data = chunk_size * b'*'
    with open(file_name, 'w+b') as f:
        i = 0
        while i < file_size:
            f.write(chunk_data)
            i += chunk_size
    os.unlink(file_name)

if __name__ == '__main__':
    CHUNK_SIZE_LIST = [1, 2, 4, 8, 16, 32, 64, 128, 512, 1024,
                       1024 * 10, 2048 * 10, 1024 * 1024, 1024 * 1024 * 10]
    FILE_NAME = "temp_file"
    FILE_SIZE = 10 * 1024 * 2014
    TRY_NUM = 1

    print("%-15s %-15s %-15s" % ('chunk_size', 'mmap', 'fwrite'))
    for chunk_size in CHUNK_SIZE_LIST:
        mmap_timer = Timer("file_mmap(FILE_NAME, FILE_SIZE, chunk_size)",
                           "from __main__ import file_mmap, FILE_NAME, FILE_SIZE, chunk_size")
        fwrite_timer = Timer("file_fwrite(FILE_NAME, FILE_SIZE, chunk_size)",
                             "from __main__ import file_fwrite, FILE_NAME, FILE_SIZE, chunk_size")
        print("%-15s %-15s %-15s" % (chunk_size,
                                     mmap_timer.timeit(number=TRY_NUM),
                                     fwrite_timer.timeit(number=TRY_NUM)))
