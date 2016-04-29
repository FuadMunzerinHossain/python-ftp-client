"""
Author: Fuad Munzerin Hossain
Other Contributors:
Github: FuadMunzerinHossain
Website: individual.utoronto.ca/Fuad
"""

import ftplib


def print_dir():
    """ function to print out files and directory names in current FTP server directory """
    try:
        print('File List:')
        files = ftp.dir()
        print(files)
    except Exception as e:
        print('Exception: ' + str(e))
    return


def change_dir(argument):
    """ function to change directory on FTP server"""
    try:
        ftp.cwd(argument)
    except Exception as e:
        print('Exception: ' + str(e))
        print('Error: Failed to change directory!')
    return


def download_file(name):
    """ function to download file onto local directory """
    try:
        f = open(name, 'wb')
        ftp.retrbinary('RETR ' + name, f.write)
        f.close()
        print(name + ' has been downloaded to local directory.')
    except Exception as e:
        print('Exception: ' + str(e))
        print('Error: File does not exist or could not be downloaded!')
    return


def mkdir(name):
    """ function to make new directory on FTP server """
    try:
        ftp.mkd(name)
        print('Directory ' + name + ' successfully created.')
    except Exception as e:
        print('Exception: ' + str(e))
        print('Directory ' + name + ' could not be created!')
    return


def rename(old_name, new_name):
    """ function to rename file/directory on FTP server """
    try:
        ftp.rename(old_name, new_name)
        print(old_name + ' successfully renamed to ' + new_name + '.')
    except Exception as e:
        print('Exception: ' + str(e))
        print('Could not rename ' + old_name + ' to ' + new_name + '!')
    return


def delete_file(name):
    """ function to delete file on FTP server """
    try:
        ftp.delete(name)
        print('Successfully deleted ' + name + '.')
    except Exception as e:
        print('Exception: ' + str(e))
        print('Could not delete ' + name + '!')
    return


def delete_directory(name):
    """ function to delete directory on FTP server """
    try:
        ftp.rmd(name)
        print('Successfully deleted ' + name + '.')
    except Exception as e:
        print('Exception: ' + str(e))
        print('Could not delete ' + name + '!')
    return


ftp = ftplib.FTP()  # initiate FTP object
""" default settings """
ip_address = '192.168.0.17'  # replace with default FTP IP Address
port = 3721  # replace with default FTP port (usually 21, but can be different)
username = 'Fuad123'  # replace with default FTP username
password = 'voldemort'  # replace with default FTP password

cmd = input('Use default settings? (y/n) (select n if you did not change source file): ')
if cmd == 'n' or cmd == 'N':
    ip_address = input('Enter IP Address: ')
    port = int(input('Enter port: '))
    username = input('Enter username: ')
    password = input('Enter password: ')

ftp.connect(ip_address, port)
ftp.login(username, password)

print(ftp.getwelcome())

while True:
    # cmd = input('-> ')
    cmd = input('root' + ftp.pwd() + '> ')
    cmd_list = cmd.split()
    cmd = cmd_list.pop(0).lower()
    cmd_args = " ".join(cmd_list)

    if cmd == 'dir' or cmd == 'ls':
        print_dir()

    elif cmd == 'cwd' or cmd == 'cd':
        change_dir(cmd_args)

    elif cmd == 'download' or cmd == 'retr':
        download_file(cmd_args)

    elif cmd == 'mkd' or cmd == 'mkdir':
        mkdir(cmd_args)

    elif cmd == 'rename' or cmd == 'mv':
        try:
            old_name = cmd_list.pop(0)
            new_name = cmd_list.pop(0)
            prompt = input('Do you want to change ' + old_name + ' to ' + new_name + '? (y,n,m)\n' +
                           'Select m to type the names separately if the names have spaces: ').lower()
            if prompt == 'y':
                rename(old_name, new_name)
            elif prompt == 'm':
                old_name = input('Which file/directory do you want to rename?')
                new_name = input('What do you want to rename ' + old_name + ' to?')
                rename(old_name, new_name)
        except Exception as e:
            print('Exception: ' + str(e))
            print('Invalid arguments')

    elif cmd == 'rm':
        confirm = input('Are you sure you want to delete file ' + cmd_args + '?(y/n): ').lower()
        if confirm == 'y':
            delete_file(cmd_args)
        else:
            print('Not deleting ' + cmd_args + ".")

    elif cmd == 'rmd':
        confirm = input('Are you sure you want to delete directory ' + cmd_args + '?(y/n): ').lower()
        if confirm == 'y':
            delete_directory(cmd_args)
        else:
            print('Not deleting ' + cmd_args + ".")

    elif cmd == 'quit':
        break








