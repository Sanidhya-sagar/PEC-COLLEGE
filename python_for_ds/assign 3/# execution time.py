import time
import csv

time_list = list()

start_time = time.time()

t_dict = {"Lines":"Lines", "Time": "Time"}
time_list.append(t_dict)

for i in range(500):
    out_path = "file500/f-upper{}.txt".format(i)
    in_path = "file500/f{}.txt".format(i)
    out_file = open(out_path, "w")
    in_file = open(in_path, "r")
    out_file.seek(0)
    out_file.write(in_file.read().upper())
    
    if i in range(0, 500, 100):
        t_dict = {"Lines":i, "Time": time.time() - start_time}
        time_list.append(t_dict)

_csv = open("time.csv", "w")
writer = csv.DictWriter(_csv, fieldnames=["Lines", "Time"])
writer.writerows(time_list)