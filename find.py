text_file = open("orig.htm", "r", encoding='utf-8')
data = text_file.read()
text_file.close()


splited = data.split("(Endpoint Address: 0x2)")
nw = splited[3].split('<td valign="top" class="st08"><pre>')[1].replace('</pre></td>','').replace('\n','').replace(' ','')
print(str(nw))
new_data = b''

check_string = '30FF0BAD0007FF020060A2A1039D00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'

for one in splited:
    try:
        string = one.split('<td valign="top" class="st08"><pre>')[1].replace('</pre></td>','').replace('\n','').replace(' ','')
        if string != check_string:
            new_data = new_data + bytearray.fromhex(string)
    except Exception as e:
        print(one)
        print('\n\n\n\n\n\n\n\n')
        print(e)


with open("new.bin", "wb") as new:
    new.write(new_data)