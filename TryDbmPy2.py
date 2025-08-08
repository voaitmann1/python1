#import dbm                  # получить интерфейс: bsddb, gnu, ndbm, dumb
import anydbm
#file = dbm.open('movie', 'c')  # создать файл DBM с именем 'movie'
file = anydbm.open('movie', 'c')
file['Batman'] = 'Pow!'        # сохранить строку с ключом 'Batman'
print(file.keys())                    # получить список ключей в файле
file['Batman']                 # извлечь значение по ключу 'Batman'
b'Pow!'
who = ['Robin', 'Cat-woman', 'Joker']
what = ['Bang!', 'Splat!', 'Wham!']
for i in range(len(who)):
    file[who[i]] = what[i]     # добавить еще 3 "записи"
print(file.keys())
print(len(file), 'Robin' in file, file['Joker'])
file.close()
class Complex:
    def __init__(self,re=0,im=0):
        self.re=re
        self.im=im
def Re(x):
    return x.re
def Im(x):
    return x.im
x=Complex(20,10)
P=pickle.Pickler('C:\temp\s.txt') 
P.dump(x)
y-pickle.Unpickler('C:\temp\s.txt')
print(y)
