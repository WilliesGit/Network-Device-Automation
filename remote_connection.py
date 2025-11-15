from netmiko import ConnectHandler 
from difflib import HtmlDiff #For comparing differences
import ipaddress  #To check valid IP address
import re 
from getpass import getpass


#Color codes
red = '\033[91m'
reset = '\033[0m'
green = '\033[92m'
blue = '\033[94m'


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

      #Validation for failed session
        if connection is None:
            print("Failed to establish SSH connection")

        #Enter Privilege enable mode if secret is provided
        if secret != "":
            connection.enable()
       
        #Calling the hostnameConfig() function
        hostnameConfig(connection)
  
        #Retrieving tranpsort input information
        trans_input_info = connection.remote_conn.sock 
        remote_ip, remote_port = trans_input_info.getpeername()
        print(f"Connection established through: {blue}{remote_ip}:{remote_port}{reset}")
        print("Telnet Session Closed!")
        print("===============================================")
       
        connection.disconnect()

        return connection

  except (RuntimeError, TypeError, NameError, OSError, netmiko.NetMikoTimeoutException) as e:
    print(f"{red}Error: {e}{reset}")


def sshLogin(ip_addr, username, password, secret):
  try:
      device_ConfigSSh = {
      'device_type': 'cisco_ios',
      'host': ip_addr,
      'username': username, 
      'password': password, 
      'secret' : secret
      } 

      #Calling the connection function
      connection = ConnectHandler(**device_ConfigSSh)

      #Validation for failed session
      if sessionSSH is None:
          print("Failed to establish SSH connection")

      #Enter Privilege enable mode if secret is provided
      if secret != "":
          sessionSSH.enable()

      #Retrieving tranpsort input information
      trans_input_info = sessionSSH.remote_conn.get_transport().sock 
      remote_ip, remote_port = trans_input_info.getpeername()

      print("\n===============================================")
      print(f"Connection established through: {blue}{remote_ip}:{remote_port}{reset}")
      print("SSH Session Closed!")
      print("===============================================")

      sessionSSH.disconnect()

      return sessionSSH
      
  except (RuntimeError, TypeError, NameError, OSError, netmiko.NetMikoTimeoutException) as e:
      print(f"{red}Error: {e}{reset}")


#To validate IP address      
def validateIP(ip_addr):
    try:
        ip = ipaddress.ip_address(ip_addr)
        return ip,ip.version

    except ValueError as e:
        print("\n")
        raise ValueError(f"{e}")


#Function to save configuration to file
def saveToFile(filename, config_type):
    try:

        with open(filename, 'w') as con_file:
            con_file.write(config_type) 
            
        return filename    

    except IOError as error:
        print("An error occured writing to file: ", error)
    

#Function to read configuration from file
def readFromFile(filename):
    try:
        with open(filename, 'r') as con_file:
           readFile = con_file.read().splitlines()   
        
        return readFile
    except IOError as error:
        print("An error occured reading from file: ", error)


#Function to Establish the connections
def connection(device_config):

  #Establishes a connection 
  connection = ConnectHandler(**device_config)

  #Sub-Menu Options for Other Configuration
  try:
      while True:
          print("\n")
          print("===============================================\n")
          print("1. Configure Hostname")
          print("2. Save Running Configuration")
          print("3. Save Startup Configuration")
          print("4. Compare Running and Startup Configuration")
          print("5. Compare Running Configuration and Cisco Device Hardening Advice")
          print("6. Quit")

          option = input("\nPlease enter an option :  ")

          if option == '1':
              hostnameConfig(connection)

          elif option == '2':
              runningConfig(connection)

          elif option == '3':
              startConfig(connection)

          elif option == '4':
              compareRunStart(connection)

          elif option == '5':
              compareRun_CiscoHard(connection)

          elif option == '6' or option == 'q':
              break

          else:
              print(f"{red}Please enter a valid option{reset}")

      return connection

  except netmiko.NetMikoTimeoutException as error: 
      print(f"{red}Connection timed out: {error}{reset}")
      return None


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
                print("===============================================\n")
                print(f"{green}This is an unsecured connection using Telnet{reset}")

                ip_addr = input("Please enter Host IP address: ")
                username = input("Please enter Host Username: ")
                password = getpass("Please enter Host Password: ")
                secret = getpass("Please enter the privilege enabled password: ")

                #Input validations
                if (ip_addr == "" or username == "" or password == "" ):
                    print(f"{red}Fields cannot be empty{reset}")
                    continue
                
                #Validating IP address version
                try:
                    ip, ip_version = validateIP(ip_addr)
                
                    #Calling the telnet function
                    telnetLogin(str(ip), username, password, secret)
                  
                except (RuntimeError, TypeError, NameError, ValueError, OSError) as e:
                    print(f"{red}Error: {e}{reset}")



            elif option == '2':
                print("\n===============================================\n")
                print(f"{green}This is a Secured connection using SSH{reset}")

                ip_addr = (input("Please enter Host IP address: "))
                username = input("Please enter Host Username: ")
                password = getpass("Please enter Host Password: ")
                secret = getpass("Please enter the privilege enabled password: ")

                #Input validations
                if (ip_addr == "" or username == "" or password == "" ):
                    print(f"{red}Fields cannot be empty{reset}")
                    continue

                #Validating IP address version
                try:
                    ip, ip_version = validateIP(ip_addr)
                   
                    #Calling the SSH function
                    sshLogin(str(ip), username, password, secret)
                  
                except (RuntimeError, TypeError, NameError, ValueError, OSError) as e:
                    print(f"{red}Error: {e}{reset}")

            
            elif option == '3' or option == 'q':
                print("Goodbye")
                break

            else:
                print(f"{red}Please enter a valid option{reset}")
        
    except (RuntimeError, TypeError, NameError,  KeyboardInterrupt) as e:
        print(f"{e}")


if __name__ == "__main__":
   main()


