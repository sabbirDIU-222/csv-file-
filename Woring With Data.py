'''
now i have a data sate to practice myself
i got this data from kaggle and this data is like heart
1.we write into this data
2.we make a copy csv file
3.we put data

'''
import csv

with open('heart_copy.csv','w') as cdata:
    with open('heart.csv') as read:
        write_data = csv.writer(cdata)
        read_data = csv.reader(read)

        # make count the row
        m_count = 0
        for row in read_data:
            if m_count==0:
                row.append('need_CLC')
                write_data.writerow(row)
                m_count += 1

            else:

                write_data.writerow(row)
                m_count += 1


        print(f'total line in data {m_count}')

