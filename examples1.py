#Next
old_salary = [35000, 50000, 65000, 49000, 55000]
new_salary = []
for salary in old_salary:
    new_salary.append(salary * 1.9)
print(new_salary)
#
myList.sort()
myList.sort(reverse=True)
myList.sort(reverse=False)
lowest_val = min(myList)
#
my_friends = ['Дмитрий', 'Евгений', 'Елена', 'Михаил', 'Елена', 'Татьяна', 'Антон', 'Елена']
popular_name = my_friends.count('Елена')
print(popular_name)
#
my_list = []
for x in range (1, 25, 2):
    my_list.append(x)
# shorter equivalent is so called list comprehension:
my_list = [x for x in range(1, 25, 2)]
#[1,3,5,...,21,23]
#
#other examples:
numbers = [x for x in range(3,100,3)]
#числа от 3 до 99, кратные трём
#task2
numbers = [x**2 for x in range(10, 100, 5)]
#квадраты всех двузначных чисел, кратных пяти
#Task3
numbers = [x*y for x in range(1, 10) for y in [3, 5, 7]]
print(numbers)
#[3, 5, 7, 6, 10, 14, 9, 15, 21, 12, 20, 28, 15, 25, 35, 18, 30, 42, 21, 35, 49, 24, 40, 56, 27, 45, 63]
#числа от 1 до 63 включительно, кратные 3, 5 или 7
#N4
numbers = [x for x in range(1, 100) if x == 0 or x == 0 or x == 0]
print(numbers)
#[3, 5, 6, 7, 9, 10, 12, 14, 15, 18, 20, 21, 24, 25, 27, 28, 30, 33, 35, 36, 39, 40,
#42, 45, 48, 49, 50, 51, 54, 55, 56, 57, 60, 63, 65, 66, 69, 70, 72, 75, 77, 78, 80,
#81, 84, 85, 87, 90, 91, 93, 95, 96, 98, 99]
#числа от 1 до 99, кратные 3, 5 или 7
#
#N5 - best for list comprehension
numbers = [x for x in range(3,100) if [x for y in range(2,x)].count(0) == 0]
#все простые числа в интервале от 3 до 100
#
#N6
#Какой код можно использовать для создания списка, содержащего согласные буквы из слова "привет"?
#my_list = [x for x in 'привет' if x in ['п', 'р', 'в', 'т']]
my_list = [x for x in 'privet' if x in ['p', 'r', 'v', 't']]
print(my_list)
#N7
#Какой код можно использовать для создания списка, содержащего буквы из слова "синхрофазотрон", расставленные в алфавитном порядке?
my_list = sorted([x for x in 'синхрофазотрон'])
print(my_list)
#N8
#Какой код можно использовать для создания списка, содержащего значения 90%, 100% и 110% от каждого целого числа в интервале от 11 до 19 включительно?
my_list = [x*y for x in range(11,20) for y in [0.9, 1, 1.1]]
print(my_list)
#N9
my_list = []
for x in range(1, 50):
    if x == 0:
        my_list.append(x**0.5)
#equialent list coprehension:
my_list = [x**0.5 for x in range(1,50) if x==0 ]
#N10
my_list = []
for x in range(90, 100):
    first_digit = x//10
    last_digit = x
    my_list.append(first_digit + last_digit)
#equialent list coprehension:   
my_list = [x//10+x for x in range(90,100)]
#
#vocabs
employee_base = {'Мария Никитина': '+79033923029'}
employee_base = {
    'Мария Никитина': '+79033923029',
    'Егор Савичев': '+78125849204',
}
print(employee_base['Мария Никитина'])
for name in employee_base:
    print(employee_base[name])
#При обращении к ключу словаря этот ключ должен обязательно быть в словаре. Иначе мы получим ошибку (KeyError).
#Для работы с sic cases es 2 standard способа
#№1
for name in request:
    if name in employee_base:
        print(employee_base[name])
    else:
        print('Неизвестный сотрудник')
#№2 setdefault
#метод создает ключ, указанный в 1-м параметре метода, если он не существует в словаре,
#и присваивает значение, указанное вторым параметром.
#Если же ключ существует в словаре, то значение не меняется
for name in request:
    employee_base.setdefault(name, 'Неизвестный сотрудник')
    print(employee_base[name])
 #Для перебора ключей
 for employee in employee_base:
    print(employee)
#или
for employee in employee_base.keys():
    print(employee)
#Перебор ключей и значений 1t'y
for employee, position in employee_base.items():
    if position == 'разработчик':
        print(employee)
#
dict_expences=[]
# error! so s'abdo'd list, ma ne dict!
dict_expences['2019-04-01']=2504
dict_expences['2019-04-02']=4994
dict_expences['2019-04-03']=6343
print(dict_expences)
#Traceback (most recent call last):
 # File "D:/MyFilesCur/MyPrgs/pt/CurProbe.py", line 2, in <module>
 #   dict_expences['2019-04-01']=2504
#TypeError: list indices must be integers, not str
dict_expences={}
dict_expences['2019-04-01']=2504
dict_expences['2019-04-02']=4994
dict_expences['2019-04-03']=6343
print(dict_expences)
#{'2019-04-01': 2504, '2019-04-02': 4994, '2019-04-03': 6343}
dict_expences={}
dict_expences['2019-04-01']=2504
dict_expences['2019-04-02']=4994
dict_expences['2019-04-03']=6343
print(dict_expences)
#
sum=0
for date in dict_expences:
    sum=sum+dict_expences[date]
    print(sum)
print(sum)
print()
# 2-q vrn
sum=0
for date, cost in dict_expences.items():
    sum=sum+cost
    print(sum)
print(sum)
#
phones = {
'Гордиенко Виктория': 5140,
'Анисимов Кирилл': 5145,
'Кузнецова Дарья': 5142
}
if phones['Кузнецова Дарья'] == 5142:
print('Номер верен')
for name, phone in phones.items():
if name == 'Кузнецова Дарья' and phone == 5142:
print('Номер верен')
for record in phones:
if record == 'Кузнецова Дарья' and phones[record] == 5142:
print('Номер верен')
#
#lebe hab csv-file
csv_file = [
    ['100412', 'Ботинки для горных лыж ATOMIC Hawx Prime 100', 9],
    ['100728', 'Скейтборд Jdbug RT03', 32],
    ['100732', 'Роллерсерф Razor RipStik Bright', 11],
    ['100803', 'Ботинки для сноуборда DC Tucknee', 20],
    ['100898', 'Шагомер Omron HJA-306', 2],
    ['100934', 'Пульсометр Beurer PM62', 17],
]
print(csv_file[4])
#Результат: ['100898', 'Шагомер Omron HJA-306', 2]
print(csv_file[4][2])
#Результат: 2
for record in csv_file:
    if record[1] == 'Шагомер Omron HJA-306':
        print('Количество шагомеров на складе - {}шт'.format(record[2]))
#
results = [
{'cost': 98, 'source': 'vk'},
{'cost': 153, 'source': 'yandex'},
{'cost': 110, 'source': 'facebook'},
]
#print(min(results[0]['costs']))
#task: find min
#vrn 1:
count=0
for rslt in results:
    count=count+1
    curCost=rslt['cost']
    if count==1:
        minimum=curCost
    else:
        if curCost<minimum:
            minimum=curCost
print('habemus data:',results)
print(' Task: find min cost')
print('1) min(own alg)=',minimum)
#vrn 2:
costs=[x['cost'] for x in results]
print('2) min(costs)=',min(costs))
#vrn 3:
print('3) min(costs)(single)=',min([x['cost'] for x in results]))
#
currency = {
'AMD': {
'Name': 'Armenian Drahm',
'Nominal': 100,
'Value': 13.121
},

'AUD': {
'Name': 'Australian dollar',
'Nominal': 1,
'Value': 45.5309
},

'INR': {
'Name': 'UIndian roupy',
'Nominal': 100,
'Value': 92.9658
},

'MDL': {
'Name': 'Moldavian Leo',
'Nominal': 10,
'Value': 36.9305
},
}
headers=[]
cources=[]
for index, data in currency.items():
    headers.append('Index')
    #for name, value in data.items(): # also works gut
    #   headers.append(name)
    for key in data.keys():          # also works gut 
        headers.append(key)
    headers.append('Cource')
    break;
print(headers)
for index, data in currency.items():
    values=[index,]
    cource=data['Nominal']/data['Value']
    #for DataName, DataValue in data.items(): #also works gut
    #    values.append(DataValue)
    for DataValue in data.values():          # also works gut 
        values.append(DataValue)
    cources.append(cource)
    values.append(cource)
    print(values)
print('min cource=',min(cources))
#
bodycount = {
'Проклятие Черной жемчужины': {
'человек': 17
},

'Сундук мертвеца': {
'человек': 56,
'раков-отшельников': 1
},

'На краю света': {
'человек': 88
},

'На странных берегах': {
'человек': 56,
'русалок': 2,
'ядовитых жаб': 3,
'пиратов зомби': 2
}
}
Count=0
creaturesQuantities=[]
for filName, filmData in bodycount.items():
    for name, quantity in filmData.items():
        creaturesQuantities.append(quantity)
        Count=Count+quantity
print(creaturesQuantities)
print('sf sum=',sum(creaturesQuantities))
print('ownsum=',Count)
# ###############
import json
with open('data.json', 'rb') as infile:
    data = json.load(infile)
# type(data)
# dict
# data.keys()
# dict_keys(['events_data'])
# data['events_data']
# data_list
# ce name of dict, qam all data s'kept
# total quantity of events in .json log file
import collections
c = collections.Counter()
for category in categories:
    c[category] += 1
print (c)
#
#
# str in Py s' unicode const
# its max len depends on x32 or x64
# strs, zb, lists et dicts, s'iter'bl objs - abl be
#
string = 'Вы - самый крутой студент в SkillFactory'
for letter in string:
    print(letter, end = '')
#end - not CR, ma empty line
#py 2 ne inved egal sign af end !
#
basic_word='программирование'
#basic_word='0202qwerrewq2020'
inverted_word=''
verdict=''
L=len(basic_word)
print('L=',L)
CountNonFitting=0
for i in range(1,L+1):
    N=L-i+1
    #print ('i=',i,' N=',N)
    str1=basic_word[(i-1):(i-1)+1]
    str2=basic_word[N-1:N-1+1]
    #print ('si=',str1,' sN=',str2)
    print ('si=',basic_word[(i-1):(i-1)+1],' sN=',basic_word[N-1:N-1+1])
    #inverted_word[i-1]=str2 #error such assignment in strs s' ne supported
    inverted_word=inverted_word+str2
    if str1!=str2:
        CountNonFitting=CountNonFitting+1
        #print(str1,'!=',str2)
    else:
        #print(str1,'==',str2)
print(inverted_word)
if CountNonFitting==0:
    print('Слово '+'"'+basic_word+'"'+' является палиндромом')
else:
    print('Слово '+'"'+basic_word+'"'+' это не палиндром')
#
emails_list = ['vasya@mail.ru',
          'akakiy@yandex.ru',
          'spyderman@yandex.ru',
          'XFiles@gmail.com',
          'hello@mail.ru',
          'noname@gmail.com',
          'DonaldTrump@mail.ru',
          'a768#af@yandex.ru',
          'Ivan_Ivanovich@yandex.ru',
          'thebestmail@yandex.ru']
domains=[]
quantities=[]
domain_dict={}
CountAddresses=0
CountUniqueDomains=0
for email in emails_list:
    CountAddresses=CountAddresses+1
    domain=email[email.find('@')+1:]
    print(CountAddresses,') ',email, domain)
    if CountAddresses==1:
        CountUniqueDomains=CountUniqueDomains+1
        domains.append(domain)
        quantities.append(1)
        domain_dict[domain]=1
        print('Erst. Domains','\n',domains,' \n quantities:',quantities,'dict:',domain_dict)
    else:
        N=0
        FoundN=0
        for domainPresent in domains:
            N=N+1
            if domain==domainPresent:
                FoundN=N
                print(domain,'=',domainPresent,' it is in N ',FoundN)
        if FoundN==0:
            CountUniqueDomains=CountUniqueDomains+1
            print('new unique domain! N ',CountUniqueDomains,' : ',domain)
            domains.append(domain)
            quantities.append(1)
            domain_dict[domain]=1
            print(CountUniqueDomains, domain,domain_dict[domain])
            domain_dict[domain]=quantities[CountUniqueDomains-1]
            print(CountUniqueDomains, domain,domain_dict[domain])
        else:
            quantities[FoundN-1]=quantities[FoundN-1]+1
            domain_dict[domain]=domain_dict[domain]+1
            domain_dict[domain]=quantities[FoundN-1]
            print('this domain is already present at N ',FoundN,' and occurs already ',quantities[FoundN-1],' times')
            #print('this domain is already present. Now quantities:\n',quantities)
        #print(domains)
        #print(quantities)
        print(domain_dict)
print('Finally:')
#print(domains)
#print(quantities)
print(domain_dict)
print('Or better')
CountDictItems=0
NLen=len('N ')
DomainLen=len('Domain ')
QuantityLen=len('Quantity')
for domain, quantity in domain_dict.items():
    CountDictItems=CountDictItems+1
    if len(str(CountDictItems))>NLen:
       NLen=len(str(CountDictItems))
    if len(domain)>DomainLen:
        DomainLen=len(domain)
    if QuantityLen<len(str(quantity)):
        QuantityLen=len(str(quantity))
print('N','Domain','Quantity')
CountDictItems=0
for domain, quantity in domain_dict.items():
    CountDictItems=CountDictItems+1
    print(CountDictItems, domain, quantity)
#строка — это неизменяемый объект.  . В Python предусмотрено несколько методов, которые можно применять к строкам и ...
#при использовании метода строка изменится только на то время, пока выполняется команда.
#Само значение строковой переменной останется прежним.
#Регулярные выражения — это формальный язык, основанный на использовании метасимволов
#или так называемых символов-джокеров),
#который применяется для работы с подстроками в тексте.
#