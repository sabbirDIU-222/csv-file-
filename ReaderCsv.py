'''
['2005-08-10', '305.0', '305.0', '305.0', '305.0', '0.0', '0.0\n']
we see that when we don't import any library the csv return the list as like with all code character
but we don't want that
we need clean data
so we import the library
'''
import csv

with open('CHRIS-MGEX_IH1.csv') as csv_file:
    data = csv.reader(csv_file)
    # line count
    count = 0
    for row in data:
        if count==0:
            print(f"is first column %s" %(','.join(row)))
            count+=1
        else:
            print("this row all %s" %(','.join(row)))
            #print(f"this is row  {row}")
            count+=1
    print(f"total line are in the csv file {count}")

# so this is the advantage of using library
'''
sometimes we have million of data that time we don't touch the raw line of data 
so then it comes an problem that many code character will be in the data 
so how to fix it
we can easily do it by this csv library reader method 
i saw reader take delimiter but in my code the reader don't take any delimeter and successfully print all the data 
so this the advantage of using library 
i saw many use panda and numpy but i still don't fimiller with panda and numpy 
so i decide to make last shot and make confidently work 
26 octebor 
'''