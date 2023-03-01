import csv

with open('data/mic/micnew.csv') as csvfile:
    r = csv.reader(csvfile, delimiter=',', quotechar='"')

    with open('data/mic/micnew2.csv', 'w', newline='') as ouf:
        w = csv.writer(ouf, delimiter=',', quotechar='"',quoting=csv.QUOTE_MINIMAL)
        for row in r:
            if(len(row)==13):
                w.writerow(map(lambda x:x.replace("\n",""), row))
                #print('"'+'","'.join(row)+'"')
                pass
            else:
                print("ERROR", len(row), row)
                pass
