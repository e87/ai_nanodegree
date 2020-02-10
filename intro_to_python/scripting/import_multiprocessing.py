
import os

cpu_count = os.cpu_count()
os_name = os.name
os_pgid = os.getpid()

os_uid = os.getuid()

print(cpu_count)
print(os_name)
print(os_pgid)
print(os_uid)