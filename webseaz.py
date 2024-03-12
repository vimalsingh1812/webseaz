#!/usr/bin/env python

#NOTE coded by X-Byt3 don't try to copy my code build your own


import socket
import argparse
import colorama
import subprocess
import time

from colorama import init, Fore
from threading import Thread, Lock
from queue import Queue





que = Queue()

locking_of_thread = Lock()


init()
GREEN = Fore.GREEN
RESET = Fore.RESET
GREY = Fore.LIGHTBLACK_EX
YELLOW = Fore.YELLOW
CYAN = Fore.CYAN
RED = Fore.RED
BLUE = Fore.BLUE

banner = '''
╭╮╭╮╭╮╱╱╭╮╱╭━━━╮
┃┃┃┃┃┃╱╱┃┃╱┃╭━╮┃
┃┃┃┃┃┣━━┫╰━┫╰━━┳━━┳━━┳━━━╮
┃╰╯╰╯┃┃━┫╭╮┣━━╮┃┃━┫╭╮┣━━┃┃
╰╮╭╮╭┫┃━┫╰╯┃╰━╯┃┃━┫╭╮┃┃━━┫
╱╰╯╰╯╰━━┻━━┻━━━┻━━┻╯╰┻━━━╯'''

banner1 = '''✩░▒▓▆▅▃▂▁Open Ports▁▂▃▅▆▓▒░✩'''
banner2 = CYAN + '''webseaz port scan 	

                     .ed"""" """$$$$be.
                   -"           ^""**$$$e.
                 ."                   '$$$c
                /                      "4$$b
               d  3                      $$$$
               $  *                   .$$$$$$
              .$  ^c           $$$$$e$$$$$$$$.
              d$L  4.         4$$$$$$$$$$$$$$b
              $$$$b ^ceeeee.  4$$ECL.F*$$$$$$$
  e$""=.      $$$$P d$$$$F $ $$$$$$$$$- $$$$$$
 z$$b. ^c     3$$$F "$$$$b   $"$$$$$$$  $$$$*"      .=""$c             '''+YELLOW+'''             ╭╮╭╮╭╮╱╱╭╮╱╭━━━╮'''+CYAN+ '''
4$$$$L        $$P"  "$$b   .$ $$$$$...e$$        .=  e$$$.             '''+YELLOW+'''             ┃┃┃┃┃┃╱╱┃┃╱┃╭━╮┃'''+CYAN+ '''
^*$$$$$c  %..   *c    ..    $$ 3$$$$$$$$$$eF     zP  d$$$$$            '''+YELLOW+'''             ┃┃┃┃┃┣━━┫╰━┫╰━━┳━━┳━━┳━━━╮'''+CYAN+ '''
  "**$$$ec   "   *ce""    $$$  $$$$$$$$$$*    .r" =$$$$P""             '''+YELLOW+'''             ┃╰╯╰╯┃┃━┫╭╮┣━━╮┃┃━┫╭╮┣━━┃┃'''+CYAN+ '''
        "*$b.  "c  *$e.    *** d$$$$$"L$$    .d"  e$$***"              '''+YELLOW+'''             ╰╮╭╮╭┫┃━┫╰╯┃╰━╯┃┃━┫╭╮┃┃━━┫'''+CYAN+ '''
          ^*$$c ^$c $$$      4J$$$$$% $$$ .e*".eeP"                    '''+YELLOW+'''             ╱╰╯╰╯╰━━┻━━┻━━━┻━━┻╯╰┻━━━╯'''+CYAN+ '''
             "$$$$$$"'$=e....$*$$**$cz$$" "..d$*"                       
               "*$$$  *=%4.$ L L$ P3$$$F $$$P"                         '''+RED+'''              █▓▒▒░░░coded by X-Byt3░░░▒▒▓█ '''+CYAN+'''
                  "$   "**ebJLzb$e$$$$$b $P"                           '''+RED+'''                        version 1.0            '''+CYAN+'''
                    %..      4$$$$$$$$$$ "
                     $$$e   z$$$$$$$$$$%
                      "*$c  "$$$$$$$P"
                       ."""*$$$$$$$$bc
                    .-"    .$***$$$"""*e.
                 .-"    .e$"     "*$c  ^*b.
          .=*""""    .e$*"          "*bc  "*$e..
        .$"        .z*"               ^*$e.   "*****e.
        $$ee$c   .d"                     "*$.        3.
        ^*$E")$..$"                         *   .ee==d%
           $.d$$$*                           *  J$$$e*
            """""                              "$$$"

'''







#port scanning function
def port_scan(port):
    """
    Scan a port on the global variable `host`
    """
    try:
        s = socket.socket()
        s.settimeout(timeOut)
        s.connect((host, port))
    except:
        with locking_of_thread:
            print(f"{YELLOW}          {GREY}{host:15}\t\t{port:5} {YELLOW}  {RESET}", end="\r")
    else:
        with locking_of_thread:
            print(f"{YELLOW}🄾          {GREEN}{host:15}\t\t{port:5} {YELLOW}        🄾  {RESET}")
            print(Fore.BLUE + "✴.·´¯`·.·★  🎀---------------------------🎀  ★·.·`¯´·.✴")
    finally:
        s.close()





# controlling of thread
def cpu_of_threading():
    global que
    while True:
        worker = que.get()
        port_scan(worker)
        que.task_done()




#threading or worker function
def main(host, ports, No_of_thread):
    global que
    for t in range(No_of_thread):
        t = Thread(target=cpu_of_threading)
        t.daemon = True
        t.start()
    for worker in ports:
        que.put(worker)
    que.join()







#arg from user function
def arg():
    parser = argparse.ArgumentParser(description="Blazing Fast Port Scanner")
    parser.add_argument("--host", "-H", dest="host", help="Target to scan.")
    parser.add_argument("--ports", "-p", dest="port_range", default="1-65535", help="Port range to scan, defaults are b/w 1-65535")
    parser.add_argument("--time", "-t", dest="time", default="4", help="Enter the Timeout, default 4 sec")
    parser.add_argument("--worker", "-w", dest="worker", default="350" ,help="Amount of Worker or Thread")
    options = parser.parse_args()
    if not options.host:
        parser.error("Specify a Target Host, or use --help for more info")
    else:
        return options



#argument parser
options = arg()
host, port_range = options.host, options.port_range
start_port, end_port = port_range.split("-")
start_port, end_port = int(start_port), int(end_port)
ports = [ p for p in range(start_port, end_port)]


#thread
workersz = int(options.worker)

#timeout
timeOut = int(options.time)


subprocess.call(["clear"])
filenames = ["frame1.txt","frame2.txt"]
frames = []

for name in filenames:
    with open(name, "r", encoding="utf8") as f:
        frames.append(f.readlines())
for i in range(6):
    for frame in frames:
        print(BLUE + "".join(frame))
        time.sleep(0.2)
        subprocess.call(["clear"])


print(banner2)
print(Fore.BLUE + "\n\n\n"+"              " + banner1)
print(Fore.YELLOW+"\n\n\n=========================================================")
print(Fore.YELLOW+"IP\t\t\tPORT\n█▓▒▒░░░🄾🄾🄾🄾🄾🄾🄾🄾🄾🄾🄾🄾🄾🄾🄾🄾🄾🄾🄾🄾🄾🄾🄾🄾🄾🄾🄾🄾🄾🄾🄾🄾🄾🄾🄾🄾🄾🄾🄾🄾🄾🄾🄾🄾🄾🄾🄾░░░▒▒▓█")
#scanning
main(host, ports, workersz)
print(Fore.RED + "\n        ∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼ⊖⊖⊖⊖ⒹⓄⓃⒺ⊖⊖⊖⊖ᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫▫·∙∙")
print(Fore.WHITE + "\n\n     ▌║█║▌│║▌│║▌║▌█║H4ck Th3 Pl4n3T ▌│║▌║▌│║║▌█║▌║█")
