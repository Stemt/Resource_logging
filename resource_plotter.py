import matplotlib.pyplot as plt
import csv
import sys

f = sys.argv[1]

if ".csv" not in f:
    sys.exit(1)

with open(f) as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    times= []
    cpus = []
    mems = []
    nets = []
    i = 0
    for row in csv_reader:
        if i == 0:
            i+=1
            continue
        print("{} {} {} {}".format(row[0],row[1],row[2],row[3]))
        times.append(row[0])
        cpus.append(float(row[1]))
        mems.append(float(row[2]))
        nets.append(float(row[3])/(1000000000/8)*100)

    plt.plot(times,cpus,"r")
    plt.plot(times,mems,"g")
    plt.plot(times,nets,"b")
    print(len(times))
    plt.axis([times[0],times[-1],0,120])
    plt.show()
