draw_dict = {
	'������': 'A',
	'����������': 'B',
	'�������': 'C',
	'�����': 'C',
	'������': 'A'
}
draw_dict = {
	'Russia': 'A',
	'Portugal': 'B',
	'France': 'C',
	'Denmark': 'C',
	'Egypet': 'A'
}
print('draw_dict = {')
print('              Russia',':', 'A,')
print('              Portugal',':', 'B,')
print('              France',':', 'C,')
print('              Denmark',':', 'C,')
print('              Egypet',':', 'A')
print('            }')
#

developer_base=[]

employee_base = {'����� ��������': '��������',
                 '���� �������': '�����������',
                 '��������� �������': '��������',
                 '����� �������': '�����������',
                 '������ �������': '�����������'}
for employee in employee_base:
    if employee_base[employee] == '�����������':
        print(employee)
        developer_base[employee]=employee_base[employee]
print(developer_base)
new_dict =[]
for CountryName in draw_dict:
    if draw_dict[CountryName]=='A':
        new_dict[CountryName] =draw_dict[CountryName]
print(new_dict)
request=['Italy']

