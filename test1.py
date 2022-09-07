#HRA=House Rent Allowance
#Dearness Allowance
salary=int(input('Enter Salary: '))
if salary<=10000:
    HRA=salary*0.2
    DA=salary*0.8
    gross=salary+HRA+DA
    print('Gross Salary={}'.format(gross))
elif salary>=10001 and salary<=20000:
    HRA=salary*0.25
    DA=salary*0.9
    gross=salary+HRA+DA
    print('Gross Salary={}'.format(gross))
elif salary>=20001:
    HRA=salary*0.3
    DA=salary*0.95
    gross=salary+HRA+DA
    print('Gross Salary={}'.format(gross))
