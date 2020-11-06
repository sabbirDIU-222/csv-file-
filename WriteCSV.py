'''
now we write into the csv file
before doing it we did the same things what we did before
1.import csv
2.open file
3.read file with csv reader
4. also line count
5. and all we do this making a new csv file
'''
import csv

with open('copydata.csv','w') as outcome_data:
    with open('CHRIS-MGEX_IH1.csv') as csv_file:
        write_data = csv.writer(outcome_data)
        read_data = csv.reader(csv_file)

        count = 0
        for row in read_data:
            if count==0:

                row.append('diffr')
                row.append('average')
                write_data.writerow(row)
                count += 1

            else:
                row.append(float(row[2]) - float(row[3]))
                row.append(( float(row[2]) + float(row[3]) )/2)
                write_data.writerow(row)
                count += 1
        print(f'the number of rows are in {count}')


