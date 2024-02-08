import sys

def openstack():
    return "OpenStack"

def ceph():
    return "ceph"

def zabbix_server():
    return "Zabbix server"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <input_string>")
    else:
        input_str = sys.argv[1]
        function_name = input_str.lower().replace(" ", "_")  # Convert input to function name format
        if function_name == "openstack":
            print(openstack())
        elif function_name == "ceph":
            print(ceph())
        elif function_name == "zabbix_server":
            print(zabbix_server())
        else:
            print("No matching function found for input:", input_str)

