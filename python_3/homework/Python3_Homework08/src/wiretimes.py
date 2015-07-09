'''
Created on June 13 2015

@author: cbabilotte

reads a wireshark trace and prints the
timestamp for each packet in seconds and microseconds.
'''
import struct

def parse_trace(filename):
    '''
    Parses trace file
    return the timestamp list containing each 
    packet timestamp in seconds and microseconds
    '''
    
    offset = 24
    packets_timestamps = []
    with open(filename, 'rb') as fh:
        while True:
            # Skip through the header offset
            fh.seek(offset)
            # Skip to the first packet
            data = fh.read(16)
            if not data:
                break
            # Grab our entry headers
            ts_sec, ts_usec, incl_len, orig_len = struct.unpack('=4L', data)
            # Advance our offset to get the next timestamp
            offset = fh.tell() + incl_len
            packets_timestamps.append('Timestamp: {} seconds, {} microseconds'.format(ts_sec, ts_usec))
    return packets_timestamps
    
if __name__ == "__main__":
    file = 'wireshark.bin'
    timestamps = parse_trace(file)
    for timestamp in timestamps:
        print(timestamp)
    
    
    
    
    
    
    