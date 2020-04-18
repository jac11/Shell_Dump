#/usr/bin/python

import readline
import re
import os
import time 
import shutil
import subprocess  
  
class Shell_Dump:
      def __init__(self):
        
        self.Banner()
        self.Create_file()
        self.file_path()
        self.IF_OPtion()
        self.LINKER_ASSEMBLY()
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
                 print "\n[*]File is Ready Exist[*]",os.getcwd()
                 time.sleep(2)
         except KeyboardInterrupt:
              print self.Banner
              exit() 
      def file_path(self):
          try:
            try:   
                destntion = os.getcwd()
                print
                self.file_cname = str(raw_input("\n[X]Enter The File Name Example.asm : ")).strip()
                time.sleep(2)
                self.path_copy = str(raw_input("\n[E]Please Enter The File Path Example.asm :")).strip()
                self.fpath = shutil.copy(self.path_copy+self.file_cname,"./")
                self.file1 = str(self.file_cname + "_obj")
                self.file2 = str(self.file_cname + "_dump")
                self.file3 = str(self.file_cname + "_shellcode")
                self.file4 = str(self.file_cname + "_Linker")
            except IOError :
                 time.sleep(2)
                 print"\n{O}SOMETHING IS WROING PLSEASE CHECK YOU FILE PATH{O}"
                 time.sleep(2)
                 self.file_path() 
            except Exception:
                 time.sleep(2)
                 print"\n{O}SOMETHING IS WROING PLSEASE CHECK YOU FILE PATH{O}"
                 time.sleep(2)
                 self.file_path()                             
          except KeyboardInterrupt:
              print self.Banner
              exit()   
      def IF_OPtion(self):
           try:              
                 opt_1 = "x86"
                 opt_2 = "x64"
                 time.sleep(2)
                 SELECT = str(raw_input("\n[@]Please Selcet x86 or x64 : "))
                 self.fpath = shutil.copy(self.path_copy+self.file_cname,"./") 
                 print
                 if SELECT == opt_1 and  len(SELECT) == 3 : 
                       code = subprocess.call(['nasm','-f','elf32',"{}".format(self.file_cname),'-o','{}'.format(self.file1)])
                       if code == 1 :
                           print
                           print " [!] Instruction Not Completed Not Supported in 86-bit Mode [!]"
                           print "\t\t\t\t\n [@] check the assembly code[#]"  
                           time.sleep(2)
                           return self.IF_OPtion()
                       else:
                          time.sleep(2)
                          print "\nThe Object File x86 is Generated  !! "         
                                                                                                         
                 elif SELECT == opt_2 and len(SELECT)==3:                  
                       code = subprocess.call(['nasm','-f','elf64',"{}".format(self.file_cname),'-o','{}'.format(self.file1)])                     
                       if code == 1 :
                           print
                           print " [!] Instruction Not Completed Not Supported in 64-bit Mode [!]"
                           time.sleep(2)
                           return self.IF_OPtion()
                       else:
                          print "\nThe Object File x64 is Generated !! " 
                          time.sleep(2)  
                 else :
                       print " [!] Instruction Not Completed Not Supported [!]"
                       time.sleep(2)
                       return self.IF_OPtion()     
                        
           except KeyboardInterrupt:
              print self.Banner
              exit()  
                         
      def LINKER_ASSEMBLY(self):
          try:
             time.sleep(2)        
             print "\n[W]The Linker Process Started [W]\n "
             time.sleep(2)
             subprocess.call(['ld','-n','-o','{}'.format(self.file4),'{}'.format(self.file1)])
             with open(self.file2,'w')as file:                 
                stdout =  subprocess.call(['objdump','-d','{}'.format(self.file1)], stdout=file, stderr=file)   
          except KeyboardInterrupt:
              print self.Banner            
              exit()                    
      def replace(self):
          try:
              with open(self.file2,"r") as file:
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
              
              with open(self.file3,'wb')as file: 
                     file.write(Header)  
              with open (self.file3,'rb')as test:
                      test= test.read()
                      time.sleep(2)
                      print
                      print "\t\t\t\t\t\t{%}THE SHELLCODE{%}"
                      print "\t\t\t\t\t[@]++++++++++++++++++++++++++[@]\n"
                      time.sleep(2)
                      print test
                      print "\n\t\t\t\t\t[@]++++++++++++++++++++++++++[@]\n"
                      time.sleep(2)
              print "\n[@] All Files will Found at ",os.getcwd() ,"{@}"
              time.sleep(2)       
              print self.Banner
              exit
          except KeyboardInterrupt:
              print self.Banner            
              exit()                  
               
if __name__=="__main__": 
       Shell_Dump()
        
