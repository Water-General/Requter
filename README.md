Requter 
=============


The Simple Web Fuzzer and Request
-----------
Requter is (macOS Monterey M1, 2020) simple Fuzzing and Request 

Installation
-----------
```
git clone https://github.com/punkmemorie/Requter
```
How to PATH, Set up
-----------
```
chmod +x requter

vi ~/.zprofile

PATH="/Users/[USER]/Requter/requter:${PATH}"
export PATH
```

How to Use Requter
=============
```
usage: Reqter.py [-h] [-d DOMAIN] [-f FUZZ] [-w WORDLIST] [-b BLIND]

options:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        Domain name to enumerate it's domains
  -f FUZZ, --fuzz FUZZ  Fuzz input to enumerate it's bruteforce
  -w WORDLIST, --wordlist WORDLIST
                        Input the your text file link
  -b BLIND, --blind BLIND
                        Blind the status module "200,300,400,500"
```

Respon Domain
-----------
```
requter -d google.com
                                  _                        
             _ __ ___  __ _ _   _| |_ ___ _ __             
            | '__/ _ \/ _` | | | | __/ _ \ '__|            
            | | |  __/ (_| | |_| | ||  __/ |               
            |_|  \___|\__, |\__,_|\__\___|_|               
                         |_|                v0.0.1         
            Use "requter -h, --help" for more information about a command.                                               
______________________________________________________________________
 >> Method           : <Response [200]>
 >> URL              : 200
 >> Content-Type     : text/html; charset=ISO-8859-1
 >> Timeout          : 1
___________________________________________________________
<!doctype html><html itemscope="" itemtype=...........


requter -f google.com/FUZZ -w raft-large-directories-lowercase.txt -b 404
                                  _                        
             _ __ ___  __ _ _   _| |_ ___ _ __             
            | '__/ _ \/ _` | | | | __/ _ \ '__|            
            | | |  __/ (_| | |_| | ||  __/ |               
            |_|  \___|\__, |\__,_|\__\___|_|               
                         |_|                v0.0.1         
            Use "requter -h, --help" for more information about a command.                                               
______________________________________________________________________
----Attack from FUZZING----
[+] http://google.com/images STATUS : 200
[+] http://google.com/search STATUS : 200
[+] http://google.com/contact STATUS : 200
....
----FUZZING is Completed----

```




