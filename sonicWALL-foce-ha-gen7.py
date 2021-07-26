import paramiko
import time

# setting connections parameters
host = "test.rebex.net"
port = "22"
username = "demo"
password = "password"

# setting commands
config = "config\n"
ha = "high-availability\n"
force = "force-failover\n"
confirm = "yes\n"

# connecting to destination
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, port, username, password)
shell = client.invoke_shell()

# executing commands in the SSH
shell.send(config)
time.sleep(1)
shell.send(confirm)
shell.send(ha)
shell.send(force)
time.sleep(2)
shell.send(confirm)

print("end of script!")

# prevent terminal from closing
input()
