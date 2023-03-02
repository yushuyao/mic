import csv

switcher = {
        0: "no",
        1: "neither",
        2: "yes",
}

with open('data/mic/micnew.csv') as csvfile:
    r = csv.reader(csvfile, delimiter=',', quotechar='"')

    next(r)
    
    with open('data/mic/micQARoT.csv', 'w', newline='') as ouf:
        w = csv.writer(ouf, delimiter=',', quotechar='"',quoting=csv.QUOTE_MINIMAL)
        w.writerow(("category","text"))

        for row in r:
            if(len(row)==13):
                newrow=(switcher[int(row[6])],"Q: "+row[1]+" A: "+row[2]+" RoT: "+row[3])
                w.writerow(newrow)
                pass
            else:
                print("ERROR", len(row), row)
                pass
