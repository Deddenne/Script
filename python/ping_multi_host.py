import ipaddress
import platform    # For getting the operating system name
import subprocess  # For executing a shell command

# ---- ask for fist and last IP of the range
ip_first = input("Entrez la premiere IP de la plage d'IP : ")
ip_last = input("Entrez la derniere IP de la plage d'IP : ")

# ---- check fist and last IP of the range
def validate_ip_address(ip_string):
   try:
       ip_object = ipaddress.ip_address(ip_string)
        # print("The IP address {} is valid.".format(ip_object))

   except ValueError:
       print("The IP address {} is not valid".format(ip_string))

validate_ip_address(ip_first)
validate_ip_address(ip_last)


def ping(host):
    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    return subprocess.call(command) == 0

# ---- split and take the last octet of the first IP of the range
find_last_point_ip_first = ip_first.rfind('.')
find_last_point_ip_first += 1
last_octet_ip_first = ip_first[find_last_point_ip_first::]
last_octet_ip_first = int(last_octet_ip_first)
#print (last_octet_ip_first)


# ---- split and take the last octet of the first IP of the range
find_last_point_ip_last = ip_last.rfind('.')
find_last_point_ip_last += 1
last_octet_ip_last = ip_last[find_last_point_ip_last::]
last_octet_ip_last = int(last_octet_ip_last)
#print (last_octet_ip_last)

count = last_octet_ip_last - last_octet_ip_first + 2

# ---- check if fist ip is greater or smaller than last ip
if last_octet_ip_first > last_octet_ip_last :
    print ("OHLALA IP FIRST > IP LAST")
else :
    for count in range (last_octet_ip_first,last_octet_ip_last) : 
        ping(ip_first)
        last_point_ip_first = ip_first.rfind('.')
        ip_first = ip_first[0:last_point_ip_first]
        # last_octet_ip_first = int(last_octet_ip_first)
        last_point_ip_first += 1
        ip_first = "{}.{}".format(ip_first,last_octet_ip_first)


