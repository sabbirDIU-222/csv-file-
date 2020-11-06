'''
so we finally work with data and wish that we can do anything with this data

at first we need to download any csv file it is very useful to use but we can make also
do it by downloading the file using python requests module but it will more time costly
so when my client give me his data i download the data in my project folder
we no need to import any module
'''

data_file = open('CHRIS-MGEX_IH1.csv')
for row in data_file:
    print(row.split(','))

