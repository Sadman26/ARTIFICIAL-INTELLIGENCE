#ID - 19201103123
#Intake-43
#Section-2
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
#psedocode for the above program
#1. input salary
#2. if salary<=10000
#3. HRA=salary*0.2
#4. DA=salary*0.8
#5. gross=salary+HRA+DA
#6. print gross
#7. elif salary>=10001 and salary<=20000
#8. HRA=salary*0.25
#9. DA=salary*0.9
#10. gross=salary+HRA+DA
#11. print gross
#12. elif salary>=20001
#13. HRA=salary*0.3
#14. DA=salary*0.95
#15. gross=salary+HRA+DA
#16. print gross

