import psutil

print psutil.cpu_times()
print psutil.cpu_times().user

print psutil.cpu_count
print psutil.cpu_count(logical=False)

mem = psutil.virtual_memory()
print mem.total
print mem.free

print psutil.swap_memory()

