# Shell_Dump
* Shell_Dump.py the python script write by python2.7
* the Shell_Dump heve to ojbdump assembly code Dedect the hex code from the objdump 
## how to use

* write assemble code "file.asm".
'''

;Hello world 

; assembly code

global _start

section .text

_start:

       mov eax,0x4  ;service foe syswrite
       mov ebx,0x1  ;service to sysexit
       mov ecx,char  ; load the staring 
       mov edx,char1
       int 0x80

       mov eax,0x1
       xor ebx,ebx
       int 0x80


section .data

     char: db "Hello world"
     char1 equ $ -char
'''
* Shell_Dump.py  will ask to Enter the name asm file 
* Shell_Dump.py  will ask to Enter the path of the file asm
* Shell_Dump.py  will ask to select x86 or x64 
* Shell_Dump.py  will do nsam -f elf32 0r elf64 and will create file .o
* Shell_Dump.py  will linker the assembly use 'ld -n - o 'and will create file have output
* Shell_Dump.py  will use objdump - d and will save output file.txt
* Shell_Dump.py  Will detect the shellcode from file.txt and save the shellcode in to file.txt and print the shellcode
* shell_Dump.py  will save all file in to folder Shell_Dump and will print location of this file 

##  Shell_Dump stpes

'''

              _____ _          _ _ _____                        
             /   __| |        | | |  __ \                       
            | (___ | |__   ___| | | |  | |_   _ _ __ ___  _ __  
             \___ \| '_ \ / _ \ | | |  | | | | | '_ ` _ \| '_ \ 
             ____) | | | |  __/ | | |__| | |_| | | | | | | |_) |
            |_____/|_| |_|\___|_|_|_____/ \__,_|_| |_| |_| .__/ 
                                                         | |    
                                                         |_|   
                      

[+]Create file Shell_Dump in [*] /root/Desktop/Shell_Dump/Shell_Dump


[X]Enter The File Name Example.asm : execve2.asm

[E]Please Enter The File Path Example.asm :/root/Desktop/test/

[@]Please Selcet x84 or x64 : x86


tThe Object File x86 is Generated  !! 

[W]The Linker Process Started [W]
 
ld: i386 architecture of input file `execve2.asm_obj' is incompatible with i386:x86-64 output

						{%}THE SHELLCODE{%}
					[@]++++++++++++++++++++++++++[@]


"\xeb\x1a\x5e\x31\xc0\x88\x46\x07\x8d\x1e\x89\x5e\x08\x89"
"\x46\x0c\xb0\x0b\x89\xf3\x8d\x4e\x08\x8d\x56\x0c\xcd\x80"
"\xe8\xe1\xff\xff\xff\x2f\x62\x69\x6e\x2f\x73\x68\x4a\x41\x41\x41\x41\x4b\x4b\x4b\x4b"

					[@]++++++++++++++++++++++++++[@]


[@] All Files will Found at  /root/Desktop/Shell_Dump/Shell_Dump {@}
   
              _____ _          _ _ _____                        
             /   __| |        | | |  __ \                       
            | (___ | |__   ___| | | |  | |_   _ _ __ ___  _ __  
             \___ \| '_ \ / _ \ | | |  | | | | | '_ ` _ \| '_ \ 
             ____) | | | |  __/ | | |__| | |_| | | | | | | |_) |
            |_____/|_| |_|\___|_|_|_____/ \__,_|_| |_| |_| .__/ 
                                                         | |    
                                                         |_| 
,,,							 
   
## Connect Me . 
* administrator@jacstory.tech

   
