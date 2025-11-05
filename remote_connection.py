from netmiko import ConnectHandler 



#Function for Telnet Connection
def telnetLogin(ip_addr, username, password, secret):
  try:
      device_ConfigTelnet = {
      'device_type': 'cisco_ios_telnet',
      'host': ip_addr,
      'username': username, 
      'password': password, 
      'secret' : secret
      } 

      connection = ConnectHandler(**device_ConfigTelnet)

  except:
    pass


def sshLogin(ip_addr, username, password, secret):
  try:
      device_ConfigSSh = {
      'device_type': 'cisco_ios',
      'host': ip_addr,
      'username': username, 
      'password': password, 
      'secret' : secret
      } 

      connection = ConnectHandler(**device_ConfigSSh)
  except:
    pass

def main():
    print("\n")
    print("***WELCOME TO THE NETWORK REMOTE CONNECTION***")
    print("\n===============================================")
    try:
        while True:
            print("\n")
            print("1. Telnet Remote Connection")
            print("2. SSH Remote Connection")
            print("3. Quit")

            option = input("\nPlease enter an option to connect to a device:  ")

            if option == "1":
               pass
            
            elif option == '3' or option == 'q':
              pass

            else:
               pass
    except:
      pass


if __name__ == "__main__":
   main()


