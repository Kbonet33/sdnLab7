import netmiko
from netmiko import ConnectHandler
from getpass import getpass
from netmiko.ssh_exception import AuthenticationException, SSHException, NetMikoTimeoutException

USERNAME = input("Please enter your SSH username: ")
PASS = getpass("Please enter your SSH password: ")

device = {
    'ip': '192.168.11.11',
    'username': USERNAME,
    'password': PASS,
    'device_type': 'cisco_ios'
}

try:
    c = ConnectHandler(**device)
    output = c.send_command('show run')
    f = open('backup.conf', 'x')
    f.write(output)
    f.close()
except (AuthenticationException):
    print("An Authentication error occured while connecting to: " + device['ip'])
except (SSHException):
    print("An error occured while connecting to device " + device['ip'] + "via ssh. Is SSH enabled?")
except (NetMikoTimeoutException):
    print("the device " + device['ip'] + " timed out when attempting to connect")
