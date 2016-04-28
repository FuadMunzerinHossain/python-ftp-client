"""
Author: Fuad Munzerin Hossain
Other Contributors:
Github: FuadMunzerinHossain
Website: individual.utoronto.ca/Fuad
"""

import ftplib


def print_dir():
    """ function to print out files and directory names in current FTP server directory """
    print('File List:')
    files = ftp.dir()
    print(files)
    return


def change_dir(argument):
    """ function to change directory on FTP server"""
    try:
        ftp.cwd(argument)
        print_dir()
    except:
        print('Error: Failed to change directory!')
    return


def download_file(name):
    """ function to download file onto local directory """
    try:
        f = open(name, 'wb')
        ftp.retrbinary('RETR ' + name, f.write)
        f.close()
        print(name + ' has been downloaded to local directory.')
    except:
        print('Error: File does not exist or could not be downloaded!')

def mkdir(name):
    """ function to make new directory on FTP server """
    try:
        ftp.mkd(name)
        print('Directory ' + name + ' successfully created.')
    except ftplib.error_perm as e:
        print(e)
        print('Directory ' + name + ' could not be created!')

ftp = ftplib.FTP()  # initiate FTP object
# default settings
ip_address = '192.168.0.17'  # replace with default FTP IP Address
port = 3721  # replace with default FTP port (usually 21, but can be different)
username = 'Fuad123'  # replace with default FTP username
password = 'voldemort'  # replace with default FTP password

cmd = input('Use default settings? (y/n): ')
if cmd == 'n' or cmd == 'N':
    ip_address = input('Enter IP Address: ')
    port = int(input('Enter port: '))
    username = input('Enter username: ')
    password = input('Enter password: ')

ftp.connect(ip_address, port)
ftp.login(username, password)

print(ftp.getwelcome())

while True:
    cmd = input('-> ')
    cmd_list = cmd.split()
    cmd = cmd_list.pop(0)
    cmd_args = " ".join(cmd_list)

    if cmd == 'dir' or cmd == 'ls':
        print_dir()

    elif cmd == 'cwd' or cmd == 'cd':
        change_dir(cmd_args)

    elif cmd == 'download' or cmd == 'retr' or cmd == 'RETR':
        download_file(cmd_args)

    elif cmd == 'mkd' or cmd == 'mkdir':
        mkdir(cmd_args)






