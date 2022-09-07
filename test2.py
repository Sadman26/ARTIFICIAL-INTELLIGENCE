unit=int(input('Enter unit: '))
if unit<=50:
    bill=unit*0.50
    print('Bill=',bill)
    x=bill*0.20
    print('Surcharge={}'.format(x))
elif unit>=51 and unit<=150:
    bill=25+(unit-50)*0.75
    print('Bill=',bill)
    x=bill*0.20
    print('Surcharge=',x)
elif unit>=151 and unit<=250:
    bill=100+(unit-150)*1.20
    print('Bill=',bill)
    x=bill*0.20
    print('Surcharge=',x)
elif unit>=251:
    bill=220+(unit-250)*1.50
    print('Bill=',bill)
    x=bill*0.20
    print('Surcharge=',x)