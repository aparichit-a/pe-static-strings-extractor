import json, re

ascii_strings = []
unicode_strings = []

sample_data = open("file-absolute-path", "rb").read()  # read pe file

re_string = re.compile(b'[\x20-\x7E]{3,}')  # compile the first pattern to find Ascii strings and find all in data
string_list = re_string.findall(sample_data)
for f in string_list:
    f = f.decode(errors='ignore')
    # discarding the strings having less than 4 chars or greater than 2500.
    if len(f.strip()) > 4 and len(f) < 2500 and re.search('[a-zA-Z0-9]', f):
        ascii_strings.append(f)

pat = re.compile(b'(?:[\x20-\x7E][\x00]){3,}')  # compile the pattern to find Unicoded strings and find all in data
words = [w.decode('utf-16le') for w in pat.findall(sample_data)]
for w in words:
    if len(w.strip()) > 4 and len(w) < 2500 and re.search('[a-zA-Z0-9]', w):
        unicode_strings.append(w)

# create new files and dump the data
with open("ascii_strings.txt") as a_obj, open("unicode_strings.txt") as u_obj:
    json.dump(ascii_strings, a_obj)
    json.dump(unicode_strings, u_obj)
