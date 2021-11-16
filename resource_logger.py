import time
import psutil

NET_INTERFACE = "wlo1"
NET_LIMIT = 1000000 #1GB
netio = psutil.net_io_counters(pernic=True)
net_usage = netio[NET_INTERFACE].bytes_sent + netio[NET_INTERFACE].bytes_recv
prev_usage = net_usage

print("time,%cpu,%mem,net_usage_bytes")

while(True):
    time_var = time.time()
    cpu_var = psutil.cpu_percent(3)
    mem_var = psutil.virtual_memory()[2]
    
    netio = psutil.net_io_counters(pernic=True)
    net_usage = netio[NET_INTERFACE].bytes_sent + netio[NET_INTERFACE].bytes_recv

    print("{},{},{},{}".format(time_var,cpu_var,mem_var,net_usage-prev_usage))
    prev_usage = net_usage



