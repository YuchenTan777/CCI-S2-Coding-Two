import pickle

with open("banner.p", 'rb') as fs:
    Final_txt = pickle.load(fs)

for i in Final_txt:
    for j in i:
        print(j[0] * j[1], end='')
    print('')

