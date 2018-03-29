import paramiko
import sys
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('127.0.0.1' , port=22, username='', password='')
stdin, stdout, stderr = client.exec_command('ifconfig')
output = stdout.readlines()
type = (output)
