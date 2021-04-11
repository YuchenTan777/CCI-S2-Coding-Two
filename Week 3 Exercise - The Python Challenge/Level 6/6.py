import zipfile as zf

name = '90052'
file = zf.ZipFile('channel.zip')
comment = ''

try:
    for i in range(len(file.namelist())):
        filename = name + '.txt'
        comment += file.getinfo(filename).comment.decode('utf-8')
        content = file.read(filename).decode('utf-8')
        name = content.split()[-1]
except BaseException as b:
    print(comment, end='')



