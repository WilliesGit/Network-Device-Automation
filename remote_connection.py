from netmiko import ConnectHandler 
from difflib import HtmlDiff #For comparing differences
import ipaddress  #To check valid IP address
import re 
from getpass import getpass



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
                print("===============================================\n")
                print(f"{green}This is an unsecured connection using Telnet{reset}")

                ip_addr = input("Please enter Host IP address: ")
                username = input("Please enter Host Username: ")
                password = getpass("Please enter Host Password: ")
                secret = getpass("Please enter the privilege enabled password: ")


            elif option == '2':
                print("\n===============================================\n")
                print(f"{green}This is a Secured connection using SSH{reset}")

                ip_addr = (input("Please enter Host IP address: "))
                username = input("Please enter Host Username: ")
                password = getpass("Please enter Host Password: ")
                secret = getpass("Please enter the privilege enabled password: ")
            
            elif option == '3' or option == 'q':
                print("Goodbye")
                break

            else:
                print(f"{red}Please enter a valid option{reset}")
        
    except (RuntimeError, TypeError, NameError,  KeyboardInterrupt) as e:
        print(f"{e}")


if __name__ == "__main__":
   main()


