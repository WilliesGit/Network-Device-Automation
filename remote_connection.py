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


