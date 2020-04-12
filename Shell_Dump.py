#/usr/bin/python

import readline
import re
import os
import time 
import shutil 

class Shell_Dump:
      def __init__(self):
       
        self.Banner()     
        self.Create_file()
        self.file_path()
        self.replace()
        
      def Banner(self):
         self.Banner = """   
              _____ _          _ _ _____                        
             /   __| |        | | |  __ \                       
            | (___ | |__   ___| | | |  | |_   _ _ __ ___  _ __  
             \___ \| '_ \ / _ \ | | |  | | | | | '_ ` _ \| '_ \ 
             ____) | | | |  __/ | | |__| | |_| | | | | | | |_) |
            |_____/|_| |_|\___|_|_|_____/ \__,_|_| |_| |_| .__/ 
                                                         | |    
                                                         |_|   
                      """ 
         print self.Banner
  
      def Create_file(self):
         try: 
             try:    
                 self.dir_1= "Shell_Dump"
                 path = os.getcwd()   
                 create= os.path.join(path,self.dir_1)
                 os.mkdir(create)
                 time.sleep(2) 
                 os.chdir(self.dir_1)
                 print "\n[+]Create file Shell_Dump in [*]",os.getcwd()       
                 
             except OSError:
                 time.sleep(2)
                 os.chdir(self.dir_1)
                 print "\n[*]File is Ready Exits [*]",os.getcwd()
                 time.sleep(2)
         except KeyboardInterrupt:
              print self.Banner
              exit() 
              
      def file_path(self):
          try:
            try:   
                destntion = os.getcwd()
                print"\n[$]Please Copy the Output objdump.o To 'Plan.txt' "
                time.sleep(2)
                self.file_cname= str(raw_input("\n[X]Enter The File Name Of The 'Plan.txt': ")).strip()
                time.sleep(2)
                self.path_copy = str(raw_input("\n[E]Please Enter The File Path Of :")).strip()
                self.fpath=shutil.copy(self.path_copy+self.file_cname,"./")
                time.sleep(2)
                print "\n[%]Please Enter File Name To Save The ShellCode Resulet[$] "
                time.sleep(2)
                self.file_name= str(raw_input("\n[E]Please Enter The File Name :")).strip()
            except IOError :
                 time.sleep(2)
                 print"\n{O}SOMETHING IS WROING PLSEASE CHECK YOU FILE PATH{O}"
                 time.sleep(2)
                 self.file_path()        
          except KeyboardInterrupt:
              print self.Banner
              exit()           
      def replace(self):
          try:
              with open(self.file_cname,"r") as file:
                        read = file.read()  
              findall= str(re.findall(":....................\D",read))
           
              Header = findall.replace(":","")
              Header = Header.replace("   ",'')
              Header = Header.replace("\\s","") 
              Header = Header.replace("\\t","")
              Header = Header.replace(",","")
              Header = Header.replace("' '","") 
              Header = Header.replace(" ","")
              Header = Header.replace("[","")
              Header = Header.replace("]","")
              Header = Header.replace("'","")
             
              Header= "".join("\\x%s"%Header[i:i+2] for i in range(0, len(Header), 2))
              Header= "".join('\n"%s"'%Header[i:i+56] for i in range(0, len(Header),56))
              
              with open(self.file_name,'wb')as file: 
                     file.write(Header)  
              with open (self.file_name,'rb')as test:
                      test= test.read()
                      time.sleep(2)
                      print "\t\t\t\t\t\t{%}THE SHELLCODE{%}"
                      print "\t\t\t\t\t[@]++++++++++++++++++++++++++[@]\n"
                      time.sleep(2)
                      print test
                      print "\n\t\t\t\t\t[@]++++++++++++++++++++++++++[@]\n"
                      time.sleep(2)
              print self.Banner
              exit
          except KeyboardInterrupt:
              print self.Banner            
              exit()                    
if __name__=="__main__":
         Shell_Dump()     
