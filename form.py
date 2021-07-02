import datetime
birth_date =  str(input("plese insert your birthdate in this type (2014-02-15): "))
year,year_main,year2 = [],[],[]
for i in birth_date:
    year.append((i))
print(year)
year_main.append((year[0:4]))
print(year_main)
for i in year_main[0]:
    # year2.extend(int(i))
    print(i)
    year2.append(int(i))
print(year2)