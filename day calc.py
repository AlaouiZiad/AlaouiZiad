daysofweek=['saturday','sunday','monday','tuesday','wednesday','thursday','friday']
def codeofyear(year):
    return year // 4 + year // 400 - year // 100 + year
def codeofmonth(month):
    month-=1
    returned=5*month//2+3*month % 2
    if month>=2:
        returned-=2
    if month>=8:
        returned+=1
    return returned
def isitleap(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False 
    else:
        if year % 4 == 0:
            return True
        else:
            return False            
def prosses():
    x=input()
    if x=='day':
        day=int(input('day:'))
        month=int(input('month:'))
        year=int(input('year:'))
        def d(year,month,day):
            d=codeofyear(year)+codeofmonth(month)+day
            if isitleap(year) and month<=2:
                d-=1
            return d
        print(daysofweek[d(year,month,day) % 7])    
    if x=='day calc':
        day=int(input('day:'))
        month=int(input('month:'))
        year=int(input('year:'))
        day2=int(input('day2:'))
        month2=int(input('month2:'))
        year2=int(input('year2:'))
        e=364*(year2-year)+28*(month2-month)+day2-day+codeofyear(year2)-codeofyear(year)+codeofmonth(month2)-codeofmonth(month)
        if e<0:
            e=-e
        print(e)
    y=input()         
    if y=='':
        prosses()
prosses()









   