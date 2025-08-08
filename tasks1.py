or i in range(1,number+1):
      if number==0:#percent char 2x
             print(i)
#A1-1.20-3
#num_1 = int(input())
#num_2 = int(input())
num_1 = 12
num_2 = 38
for i in range(1,min(num_1, num_2)+1):
    if num_1==0 and num_2==0:#percent char 2x
        print(i)
#
#nA1-1.20-4
n=10
for i in range(1,n+1):
    if i==1:
        f=1
        fm1=0
        fm2=0
    elif i==2:
       fm2=0
       fm1=f
       f=fm1+fm2
    else:
        fm2=fm1
        fm1=f
        f=fm2+fm1
    print(f,':',fm1,fm2)
# A1-20-5
number=15
for i in range(1, 10+1):
    print(number,'X',i,'=',number*i)
#A1-1.22-1
Y=170000# sum initial
Z=1000000 #sum limit
percent=10
CurSum=Y
countYears=0
while CurSum<Z:
    countYears=countYears+1
    #added=   percent/100*Y
    #added=   percent/100*Y*1.0
    added=1.0*percent/100*Y
    #added=1.0*((float(percent))/100)*Y*1.0
    CurSum=CurSum+added
    #print('yr=', countYears,' added: ',added,' sum=',CurSum)
else:
    print(countYears)
 # ov wa probe, ud wi final
 Y=170000# sum initial
Z=1000000 #sum limit
percent=10
CurSum=Y
YearlyMultiplier=1.1
countYears=0
while CurSum<Z:
    countYears=countYears+1
    CurSum=CurSum*YearlyMultiplier
    #print('yr=', countYears,' sum=',CurSum)
else:
    print(countYears)
#A-1,1-22,2
limWeight=4000
HumanWeight=77
IniWeight=0
CurWeight=IniWeight
dw=0
while CurWeight<limWeight:
   CurWeight=CurWeight+ HumanWeight
else:
    dw=CurWeight-limWeight
    print('5@525A ',dw,' :3')
#A1,1.22,3
ini_health=500
current_health=ini_health
attack = 80
count_rounds=0
while current_health>0:
    count_rounds=count_rounds+1
    current_health=current_health-attack
else:
    print(count_rounds)
#A1, 1-22, 4
InitialBalance=10000
spent=2800
balance=InitialBalance
#print('IniBalance=',balance)
print(balance)
while balance>=0:
    balance=balance-spent
    print(balance)
else:
    print('!;8H:>< 1>;LH85 @0AE>4K')
#A1, 1-22, 5
V=1000
VAddedIniPre=0
dV=5
VAddedCur=VAddedIniPre
volume=V
countSteps=0
while volume>0:
    countSteps=countSteps+1
    VAddedCur=VAddedCur+dV
    volume=volume-VAddedCur
    #print(countSteps,') VAddedCur=',VAddedCur,' volume=',volume)
else:
    print(countSteps)
#A2, 2.65
sparta = ['20=>2', '5B@>2', '!84>@>2', '09F52', 'OB;>2',
          '>7;>2', '8A8G:8=', '3C@F>2', '0?CAB8=', '@1C7>2']
sparta = ['Ivanov', 'Petrov', 'Sidorov', 'Zaitsev', 'Dyatlov',
          'Kozlov', 'Lisichkin', 'Ogurtsov', 'Kapustin', 'Arbuzov']
#1
print(sparta[0:10:2])
#2
print(sparta[1:10:3])
#3
print(sparta[0:10:5])
#4
#print(sparta[::-3])
#['Arbuzov', 'Lisichkin', 'Zaitsev', 'Ivanov']
#5
#print(sparta[-2:1:-3])
#['Kapustin', 'Kozlov', 'Sidorov']
#A2,2.6-1
my_list = []
for number in range(1,11):
    my_list.append(number**2)
print(my_list)
#A>740QB A?8A>:, A>45@60I89 :204@0BK =0BC@0;L=KE G8A5; >B 1 4> 10
#2,2.6-2
names = ['Andr', 'Ilia', 'Alex', 'Ippolit', 'Ann', 'Cost', 'Lema', 'Mary']
my_list = []
for name in names:
    my_list.append(len(name))
name_length = min(my_list)
result = my_list.count(name_length)
print(result)
#>;8G5AB2> 8<Q= A <8=8<0;L=>9 4;8=>9 2 A?8A:5 names
#2,2.6-3
my_list = [1, 10, 45, 31, 12, 54, 111, 398, 97, 63]
my_list.sort(reverse = True)
print(my_list[2])
#97
#2,2.6-4
my_list = [1, 10, 45, 31, 12, 54, 111, 398, 97, 63]
result = max(my_list) + min(my_list) + my_list.count('batman')
print(result)
#399
#A2-2.6-5
my_list = [1, 10, 45, 31, 12, 54, 111, 398, 97, 63]
my_list.sort(reverse = True)
new_list = my_list[::2]
result = 0
for number in new_list:
    result += number
print(result)
#590
#A2-2.6-6
my_list = [1]
for i in range(10):
    my_list.append(my_list[i] * 2)
my_list.sort(reverse = True)
print(my_list)
#
#  + :064K9 A;54CNI89 M;5<5=B A?8A:0 1>;LH5 ?@54K4CI53> 2 2 @070
#  - <0:A8<0;L=K9 M;5<5=B A?8A:0 1>;LH5 <8=8<0;L=>3> 2 512 @07
#  + 2 A?8A:5 11 M;5<5=B>2
#  + my_list[5] == 32
#  + M;5<5=BK A?8A:0 C?>@O4>G5=K ?> C1K20=8N
#A2-2.6-7
fruits = 'apple banana AffelSinn ba pepeprr tomato melone ananas'.split()
my_list = []
for fruit in fruits:
    my_list.append(fruit[0])
my_list.sort()
print(my_list)
print(my_list.count(my_list[0]))
#M;5<5=BK A?8A:0  1C:2K #?5@2K5
#A2-2.6-8
my_list=[]
result=0
for i in range(1,50+1):
    if i==0:
        my_list.append(i)
        result=result+i
        print(i, result)
print(result)
#408
#A2-2.6-9
my_list=[]
count=0
for word in raw_list:
    count=count+1
    my_list.append(len(word));
#print(raw_list)
#print(my_list)
result=max(my_list)+min(my_list)
print(result)
#15
#A2-2.6-10
raw_list=[2,8,10,23,64,49,11,52,71,14]
x_min=min(raw_list)
x_max=max(raw_list)
my_list=[]
for old_element in raw_list:
    if(old_element==0):
        my_list.append(old_element*x_min)
    else:
        my_list.append(old_element*x_max)
result=max(my_list)
print(result)
#[4, 16, 20, 1633, 128, 3479, 781, 104, 5041, 28]
#5041
#A2-2.7-1
numbers = [x for x in range(3,100,3)]
#G8A;0 >B 3 4> 99, :@0B=K5 B@Q<
#task2
numbers = [x**2 for x in range(10, 100, 5)]
#:204@0BK 2A5E 42C7=0G=KE G8A5;, :@0B=KE ?OB8
#Task3
numbers = [x*y for x in range(1, 10) for y in [3, 5, 7]]
print(numbers)
#[3, 5, 7, 6, 10, 14, 9, 15, 21, 12, 20, 28, 15, 25, 35, 18, 30, 42, 21, 35, 49, 24, 40, 56, 27, 45, 63]
#G8A;0 >B 1 4> 63 2:;NG8B5;L=>, :@0B=K5 3, 5 8;8 7
#N4
numbers = [x for x in range(1, 100) if x == 0 or x == 0 or x == 0]
print(numbers)
#[3, 5, 6, 7, 9, 10, 12, 14, 15, 18, 20, 21, 24, 25, 27, 28, 30, 33, 35, 36, 39, 40,
#42, 45, 48, 49, 50, 51, 54, 55, 56, 57, 60, 63, 65, 66, 69, 70, 72, 75, 77, 78, 80,
#81, 84, 85, 87, 90, 91, 93, 95, 96, 98, 99]
#G8A;0 >B 1 4> 99, :@0B=K5 3, 5 8;8 7
#N5
numbers = [x for x in range(3,100) if [x for y in range(2,x)].count(0) == 0]
#2A5 ?@>ABK5 G8A;0 2 8=B5@20;5 >B 3 4> 100
#N6
#0:>9 :>4 <>6=> 8A?>;L7>20BL 4;O A>740=8O A?8A:0, A>45@60I53> A>3;0A=K5 1C:2K 87 A;>20 "?@825B"?
#my_list = [x for x in '?@825B' if x in ['?', '@', '2', 'B']]
my_list = [x for x in 'privet' if x in ['p', 'r', 'v', 't']]
print(my_list)
#N7
#0:>9 :>4 <>6=> 8A?>;L7>20BL 4;O A>740=8O A?8A:0, A>45@60I53> 1C:2K 87 A;>20 "A8=E@>D07>B@>=", @0AAB02;5==K5 2 0;D028B=>< ?>@O4:5?
my_list = sorted([x for x in 'A8=E@>D07>B@>='])
print(my_list)
#N8
#0:>9 :>4 <>6=> 8A?>;L7>20BL 4;O A>740=8O A?8A:0, A>45@60I53> 7=0G5=8O 90%, 100% 8 110% >B :064>3> F5;>3> G8A;0 2 8=B5@20;5 >B 11 4> 19 2:;NG8B5;L=>?
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
#A 2-8
#A 2-8-1
#ne inved, qid do - s'alr done on page, 2 vrns
#A 2.9
#vocabs: key , val
employee_base = {'0@8O 8:8B8=0': '+79033923029'}
employee_base = {
    '0@8O 8:8B8=0': '+79033923029',
    '3>@ !028G52': '+78125849204',
}
#A-2, 2.9, 1
#A-2, 2.9, 2
#A-2, 2.10, 1
# easy, ma do at home!
#A-2, 2.11, 1
draw_dict = {
' >AA8O': 'A',
'>@BC30;8O': 'B',
'$@0=F8O': 'C',
'0=8O': 'C',
'38?5B': 'A'
}
#draw_dict = {
# 'Russia': 'A',
# 'Portugal': 'B',
# 'France': 'C',
# 'Denmark': 'C',
# 'Egypet': 'A'
#}
#print('draw_dict = {')
#print('              Russia',':', 'A,')
#print('              Portugal',':', 'B,')
#print('              France',':', 'C,')
#print('              Denmark',':', 'C,')
#print('              Egypet',':', 'A')
#print('            }')
#
request=['B0;8O']
for CountryName in request:
    if CountryName in draw_dict:
        group=draw_dict[CountryName]
        #print("group of ",CountryName," is ",group)
    else:
        group='unknown'
        #print("group of ",CountryName," is ",group)
print(group)
#
request=[' >AA8O']
for CountryName in request:
    if CountryName in draw_dict:
        group=draw_dict[CountryName]
        #print("group of ",CountryName," is ",group)
    else:
        group='unknown'
        #print("group of ",CountryName," is ",group)
print(group)
#A-2.11-2
request=['B0;8O']
for CountryName in request:
    draw_dict.setdefault(CountryName,'unknown')
    group=draw_dict[CountryName]
    print("group of ",CountryName," is ",group)
print(group)
#
request=['Russia']
for CountryName in request:
    draw_dict.setdefault(CountryName,'unknown')
    group=draw_dict[CountryName]
    print("group of ",CountryName," is ",group)
print(group)
#
draw_dict = {
' >AA8O': 'A',
'>@BC30;8O': 'B',
'$@0=F8O': 'C',
'0=8O': 'C',
'38?5B': 'A'
}
#draw_dict = {
# 'Russia': 'A',
# 'Portugal': 'B',
# 'France': 'C',
# 'Denmark': 'C',
# 'Egypet': 'A'
#}
#print('draw_dict = {')
#print('              Russia',':', 'A,')
#print('              Portugal',':', 'B,')
#print('              France',':', 'C,')
#print('              Denmark',':', 'C,')
#print('              Egypet',':', 'A')
#print('            }')
#

developer_base=[]
employee_base = {'0@8O 8:8B8=0': '<5=5465@',
                '3>@ !028G52': '@07@01>BG8:',
                ';5:A0=4@ 0E><>2': '48709=5@',
                ';8=0 3>@>20': '@07@01>BG8:',
                ' CA;0= 0H0@>2': '25@AB0;LI8:'}
for employee in employee_base:
    if employee_base[employee] == '@07@01>BG8:':
        print(employee)
        developer_base[employee]=employee_base[employee]
print(developer_base)
new_dict =[]
for CountryName in draw_dict:
    if draw_dict[CountryName]=='A':
        new_dict[CountryName] =draw_dict[CountryName]
print(new_dict)
# ===========================================================
#
#2.14-1
#employee_base = {'0@8O 8:8B8=0': '<5=5465@',
#                '3>@ !028G52': '@07@01>BG8:',
#                ';5:A0=4@ 0E><>2': '48709=5@',
#                ';8=0 3>@>20': '@07@01>BG8:',
#                ' CA;0= 0H0@>2': '25@AB0;LI8:'}
#countDevers=0
#for employee in employee_base:
#    if employee_base[employee]=='@07@01>BG8:':
#       countDevers=countDevers+1
#print(countDevers)
#2 ('Quantity of developers: ', 2)
#A-2,15 1sngl
new_dict=[]
draw_dict = {
'Russia': 'A',
'Portugal': 'B',
'France': 'C',
'Denmark': 'C',
'Egypet': 'A'
}
for CountryName, Group in draw_dict.items():
    if Group=='A':
        new_dict[CountryName]=Group
print(new_dict)

# Traceback (most recent call last):
# File "D:/MyFilesCur/MyPrgs/pt/CurProbe.py", line 9, in <module>
#   for CountryName, Group in draw_dict:
# ValueError: too many values to unpack

# TTraceback (most recent call last):
#  File "D:/MyFilesCur/MyPrgs/pt/CurProbe.py", line 11, in <module>
#   new_dict[CountryName]=Group
# TypeError: list indices must be integers, not str

#check in JN!

#A-2,16
#N1
dict_expences=[]
dict_expences={
    '2019-04-01' : 2504,
    '2019-04-02' : 4994,
    '2019-04-03'  : 6343,
}
print(dict_expences)
#2 - python 2 so ne work't
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
# 2
#A-2,16 N2
sum=0
for date in dict_expences:
    sum=sum+dict_expences[date]
    print(sum)
print(sum)
print()
# 2 vrn
sum=0
for date, cost in dict_expences.items():
    sum=sum+cost
    print(sum)
print(sum)
#N3  - all vrns sat fit
phones = {
'>@485=:> 8:B>@8O': 5140,
'=8A8<>2 8@8;;': 5145,
'C7=5F>20 0@LO': 5142
}
if phones['C7=5F>20 0@LO'] == 5142:
print('><5@ 25@5=')
for name, phone in phones.items():
if name == 'C7=5F>20 0@LO' and phone == 5142:
print('><5@ 25@5=')
for record in phones:
if record == 'C7=5F>20 0@LO' and phones[record] == 5142:
print('><5@ 25@5=')
# - all 3 vrns sat fit
#A 2.17
#N1sngl
csv_file = [
    ['100412', '>B8=:8 4;O 3>@=KE ;K6 ATOMIC Hawx Prime 100', 9],
    ['100728', '!:59B1>@4 Jdbug RT03', 32],
    ['100732', ' >;;5@A5@D Razor RipStik Bright', 11],
    ['100803', '>B8=:8 4;O A=>C1>@40 DC Tucknee', 20],
    ['100898', '(03><5@ Omron HJA-306', 2],
    ['100934', 'C;LA><5B@ Beurer PM62', 17],
]
pulsometer_id=csv_file[6-1][1-1]
print(pulsometer_id)
#A 2.18
#N1sngl
csv_file_filtered=[]
for record in csv_file:
    if record[2-1] >10:
        csv_file_filtered.append(record)
print(csv_file_filtered)
#A 2.19
#N1 sngl
csv_dict = [
    {'id': '100412', 'position': '>B8=:8 4;O 3>@=KE ;K6 ATOMIC Hawx Prime 100', 'count': 9},
    {'id': '100728', 'position': '!:59B1>@4 Jdbug RT03', 'count': 32},
    {'id': '100732', 'position': ' >;;5@A5@D Razor RipStik Bright', 'count': 11},
    {'id': '100803', 'position': '>B8=:8 4;O A=>C1>@40 DC Tucknee', 'count': 20},
    {'id': '100898', 'position': '(03><5@ Omron HJA-306', 'count': 2},
    {'id': '100934', 'position': 'C;LA><5B@ Beurer PM62', 'count': 17},
]
csv_dict_boots=[]
RequiredWord=">B8=:8"
csv_dict_boots=[]
RequiredWord="=">B8=:8"
for item in csv_dict:
    if RequiredWord in item['position'].split(' '):
        csv_dict_boots.append(item)
print(csv_dict_boots) 
#A 2-20
#N1
contacts = {
    '>@8A:8= ;048<8@': {
        'tel': '5387',
        'position': '<5=5465@'
    },
    '!><>20 0B0;LO': {
        'tel': '5443',
        'position': '@07@01>BG8:'
    },
}
#
print(contacts['!><>20 0B0;LO']['position'])
#A 2-20
 #N2      
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
#print('habemus data:',results)
#print(' Task: find min cost')
#print('1) min(own alg)=',minimum)
#vrn 2:
#costs=[x['cost'] for x in results]
#print('2) min(costs)=',min(costs))
#vrn 3:
#print('3) min(costs)(single)=',min([x['cost'] for x in results]))
print('min(costs)(single)=',min([x['cost'] for x in results]))
#A 2-20
#N3
defect_stats = [
{'step number': 1, 'damage': 0.98},
{'step number': 2, 'damage': 0.99},
{'step number': 3, 'damage': 0.99},
{'step number': 4, 'damage': 0.96},
{'step number': 5, 'damage': 0.97},
{'step number': 6, 'damage': 0.97},
]
curStats=1
countSteps=0
while(curStats>0.9):
    countSteps=countSteps+1
    curStats=curStats*defect_stats[countSteps-1]['damage']
    print(countSteps,') curStats=', curStats)
else:
    print('Finally: ',countSteps,': curStats=', curStats)
#A 2-20
#N4
cources=[]
for index, data in currency.items():
    cource=data['Nominal']/data['Value']
    cources.append(cource)
print('min cource=',min(cources))
#A2.20
#5
bodycount = {
'@>:;OB85 '5@=>9 65<GC68=K': {
'G5;>25:': 17
},

'!C=4C: <5@B25F0': {
'G5;>25:': 56,
'@0:>2->BH5;L=8:>2': 1
},

'0 :@0N A25B0': {
'G5;>25:': 88
},

'0 AB@0==KE 15@530E': {
'G5;>25:': 56,
'@CA0;>:': 2,
'O4>28BKE 601': 3,
'?8@0B>2 7><18': 2
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
# answer:
# 225
#
# summing-up test of module
#
#N1
#1 - yes
#2 - yes (see 2.10 )
#3 - abl if do eiid, so final anw s' no
#N2
#ddict.keys() 
#N3
#2
#N4
#arrivals['8AA01>=']['AB0BCA']
#N5
#2: len(arrivals['5:8=']['@59A'])
#A-2, 2-27
#6tasks Habemus hin no .json-file=> so do ce at home
#
#A3-3.2
#          0123456789012345678901234567899012345678990123456789012345
#          8765432109876543210987654321098765432109876543210987654321
proverb = '@>3@0<<8ABK - MB> CAB@>9AB20, ?@5>1@07CNI85 :>D58= 2 :>4.'
print('    print('    8765432109876543210987654321098765432109876543210987654321')
print('    @>3@0<<8ABK - MB> CAB@>9AB20, ?@5>1@07CNI85 :>D58= 2 :>4.')
#proverb = 'programmisty - are ustrojstva, redoinnnnnnnn kofein v cod.'
print(proverb[0:len('@>3@0<<8ABK')])
#@>3@0<<8ABK+
#print('0...18',proverb[0:18])
#
#:>D5-
#print('-10...14',proverb[-10:-14])
#
#print('-14...-10',proverb[-14:-10])
#
#print('-15...-10',proverb[-15:-10])
#
#print('-14...-11',proverb[-14:-11])
#
#@>3@0<<8ABK+
print('0...18',proverb[0:18])
#@>3@0<<8ABK
#:>D5-
print('-10...-14')
print(proverb[-10:-14])
#noid or anid rand'l
print('-14...-10')
print(proverb[-14:-10])
# :>D
print('-15...-10')
print(proverb[-15:-10])
#5 :>D
print('-14...-11')
print(proverb[-14:-11])
# :>
print('-13...-9')
print(proverb[-13:-9])
#:>D5
#3
result = proverb[19:28]+'>'
print(result)
#CAB@>9AB2>
result = proverb[19:28],'>'
print(result)
#'CAB@>9AB2','>'
#result = proverb.split(',')[3][:-2]+'>'
#print(result)
#<error>
result = proverb.split()[3][:-2]+'>'
print(result)
#CAB@>9AB2>
#result = proverb[19:29].split()+'>'
#print(result)
#<error>
#N1
proverb[0:12]
#@>3@0<<8ABK
#N2
proverb[-13:-9]
#:>D5
#N3
proverb[19:28]+'>'
proverb.split()[3][:-2]+'>'
#N4
#          0123456789012345678901234567899012345678990123456789012345
#          8765432109876543210987654321098765432109876543210987654321
proverb = '@>3@0<<8ABK - MB> CAB@>9AB20, ?@5>1@07CNI85 :>D58= 2 :>4.'
print('    print('    8765432109876543210987654321098765432109876543210987654321')
print('    @>3@0<<8ABK - MB> CAB@>9AB20, ?@5>1@07CNI85 :>D58= 2 :>4.')
proverb = 'programmisty - are devicessic, preobrasuyzie kofein v cod.'
N=-1
#ini_proverb=[]
#for letter in proverb:
#    ini_proverb.append(letter)
#print(ini_proverb)
new_proverb=[]
PrevLetter="666"
for letter in proverb:
    N=N+1
    if N==0:
        PrevLetter=letter
    else:
        new_proverb.append(letter)
        new_proverb.append(PrevLetter)
print(new_proverb)
#
#N=-1
#ini_proverb=[]
#PrevLetter="666"
#for letter in new_proverb:
#    N=N+1
#    if N==0:
#        PrevLetter=letter
#    else:
#        ini_proverb.append(letter)
#        ini_proverb.append(PrevLetter)
#print(ini_proverb)
#N5
basic_word='?@>3@0<<8@>20=85'
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
    #else:
        #print(str1,'==',str2)
print(inverted_word)
if CountNonFitting==0:
    print('!;>2> '+'"'+basic_word+'"'+' O2;O5BAO ?0;8=4@><><')
else:
    print('!;>2> '+'"'+basic_word+'"'+' MB> =5 ?0;8=4@><')
#
 #A3, 3.3
 #N1
 #1
 #2
 #
 #N3
 domain=email[email.find('@')+1:]
 #N4*
number=56.257
str_frac=str(number)[str(number).find('.')+1:]
print('frac part=',str_frac)
_sum=0;
for i in range(1, len(str_frac)+1):
    digit=int(str_frac[i-1:i-1+1])
    _sum=_sum+digit
    #print(digit,_sum)
#print('sum=',_sum)
print(_sum)
#5**
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
#
for i in range(1,6): print(i*2) # works gut, so in single line
#
#A-3, 3.4
#N1
#seems #'(
#N2
if food.lower() == '>2AO=:0': print('0 K 3C@<0=!')
#N3
string = string.replace(string[0], string[0].upper())
#N4
string = '"O6Q;0O 8=B5@=5B-7028A8<>ABL - MB> :>340 BK 2KE>48HL 87 8=B5@=5B0, 0 >= 87 B51O =5B.'
string = '@825B, =4@59!'
string1=string.replace(':',':)')
string2=string1.replace(';',':)')
string3=string2.replace('-',':)')
string4=string3.replace('.',':)')
string5=string4.replace(',',':)')
string6=string5.replace('?',':)')
new_string=string6.replace('!',':)')
#print(string)
print(new_string)
#N5*
name = '!520AB80='
wovels=['0','8','5','Q','>','C','K','M','N','O']
for i in range(1, len(name)+1):
    letter=name[i-1:i-1+1]
    if letter.lower() in wovels: print(letter,' - 3;0A=0O')
    elif letter.lower() in consonants: print(letter,' - A>3;0A=0O')
    else: print('=5 3;0A=0O 8 =5 A>3;0A=0O')
#name = 'Syebastian'
#wovels=['a','e','i','o','u','y']
#for i in range(1, len(name)+1):
#    letter=name[i-1:i-1+1]
#    if letter.lower() in wovels: print(letter,' - wovel')
#    elif letter.lower() in consonants: print(letter,' - consonant')
#    else: print(letter,' - not a latin letter')
#
#A3, 3.5
#N1
#seems \d\d\d, ne [0-9] ob ne 1, ma 3 chars
#N2
#seem all xpt #2
#N3
#seem 3 erst ob s'req'd bigL, micL et anid else
#4
#seem erst ob asic contain " ", ic s' ne regular exveds