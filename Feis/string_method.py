year, month , day = 2020,12,1

print(str(year)+"/"+str(month)+"/"+str(day).zfill(2))

print("%d/%d/%02d" % (year,month, day))

print('{0}/{1}/{2:02}'.format(year,month,day))

print('{}/{}/{:02d}'.format(year ,month,day ))

print('{year}/{month}/{day:02}'.format(year=year,month = month, day =day))

print(f'{year}/{month}/{day:02}')