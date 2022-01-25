import os

def get_data(file,file_out, start, end):
    with open(file, 'rb') as infile:
        infile.seek(start)
        print(str(end-start))
        data = infile.read(end-start)
        with open(file_out, 'wb') as outfile:
            outfile.write(data)
            
def get2_data(file, start, end):
    with open(file, 'rb') as infile:
        infile.seek(start)
        print(str(end-start))
        return infile.read(end-start)

orig_file = 'Firmware Update Tool V2.5.05.exe'


#$mode=flsh_spi8m
#$sectormap=(60 x 16k, 16 x 4k)

get_data(orig_file,'lod/intel.bin',0x20C1A8,0x217061)

def getByte(data,start):
    return data[start:start+2]

with open('lod/intel.bin') as bin_file:
    full_text = ''
    lines = bin_file.readlines()
    for line in lines:
        line = line[9:-3]
        # full_text=full_text+line[9:-3]
        for i in range(0,10):
            if i % 2 != 0:
                full_text=full_text+getByte(line,i)
            
    with open('lod/intel2.txt', 'w') as f:
        f.write(full_text)


# from intelhex import hex2bin, bin2hex
# hex2bin('lod/intel.bin', 'lod/intel.hex', 0, None, 0x3E09, None)
# bin2hex('lod/intel.hex', 'lod/intel.bin', 0)



data = b''
data = data + get2_data(orig_file,0x0,0x20C1A8)
data = data + get2_data('lod/nulled.bin',0x0,os.stat('lod/nulled.bin').st_size-1)
data = data + get2_data(orig_file,0x217060,0xF89C00)


with open('nulled_dont_use.exe', 'wb') as outfile:
    outfile.write(data)

#  994 :103FF000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFD1
#  995 :00000001FF




get_data(orig_file,'lod/7cd8dd97.lod',0x247068,0x4003F1)
get_data(orig_file,'lod/7cd8dd979.lod',0x4003F3,0xA0ED38)
get_data(orig_file,'lod/end.txt',0xA0ED39,0xA1460D)