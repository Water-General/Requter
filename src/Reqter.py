#!/Library/Frameworks/Python.framework/Versions/3.10/bin/python3

import requests
import sys

G = '\033[92m'  # green
Y = '\033[93m'  # yellow
B = '\033[94m'  # blue
R = '\033[91m'  # red
W = '\033[0m'  # white
L = '\033[90m'  # black

print("""                                  _                        
             _ __ ___  __ _ _   _| |_ ___ _ __             
            | '__/ _ \/ _` | | | | __/ _ \ '__|            
            | | |  __/ (_| | |_| | ||  __/ |               
            |_|  \___|\__, |\__,_|\__\___|_|               
                         |_|                v0.0.1@punkmemorie        
            Use "requter -h, --help" for more information about a command.                                               
______________________________________________________________________""")


def requter_url(url):
    Surl = url

    if Surl.find("http://") == -1:
        Surl = "http://" + Surl

    try:
        response = requests.get(Surl, timeout=1)

        if not response.text == '':
            print(" >> Method           : %s" % response)
            print(" >> URL              : %s" % response.status_code)
            print(" >> Content-Type     : %s" % response.headers['Content-Type'])
            print(" >> Timeout          : 1")
            print("___________________________________________________________")
            print("\033[1;32;1m%s" % response.text)
        else:
            print("\033[1;31;1mPLEASE CHECK YOUR URL\nStatus: %s" % response.status_code)
    except:
        print("\033[1;31;1mPLEASE CHECK YOUR URL : %s" % Surl)
    sys.exit()

def requter_fuzz(url, wordfile):
    print('%s----Attack from FUZZING----' % G)

    try:
        with open(wordfile, 'r') as file:
            # reading the file
            name = file.read()

            # using spilitlines() function storing the list
            # of splitted strings
            fuzz_data = name.splitlines()
    except:
        print(f'Please your Wordlist file link : {wordfile}')

    if url.find("http://") == -1:
        url = "http://" + url

    for f in fuzz_data:
        try:
            Surl = url.replace('FUZZ', f)

            # using try catch block to avoid crash of the
            # program

            # sending get request to the url
            response = requests.get(Surl)
            status = response.status_code
            # print(type(status))
            # print(type(status_blind))
            # if after putting subdomain one by one url
            # is valid then printing the url

            print(f'%s[+] {Surl} STATUS : {status}' % B)

        # if url is invalid then pass it
        except:
            print(f'%s[-] %s STATUS : ERROR' % (R, f))
            pass

    print('%s----FUZZING is Completed----' % G)
    sys.exit()

def requter_blind(url, wordfile, status_blind):
    print('%s----Attack from FUZZING----' % G)
    try:
        status_blind = status_blind.split(',')
    except:
        pass
    # print(status_blind)
    try:
        with open(wordfile, 'r') as file:
            # reading the file
            name = file.read()

            # using spilitlines() function storing the list
            # of splitted strings
            fuzz_data = name.splitlines()
    except:
        print(f'Please your Wordlist file link : {wordfile}')

    if url.find("http://") == -1:
        url = "http://" + url

    for f in fuzz_data:
        try:
            Surl = url.replace('FUZZ', f)

            # using try catch block to avoid crash of the
            # program

            # sending get request to the url
            response = requests.get(Surl)
            status = response.status_code
            # print(type(status))
            # print(type(status_blind))
            # if after putti, eng subdomain one by one url
            # is valid then printing the url

            if str(status) not in status_blind:
                print(f'%s[+] {Surl} STATUS : {status}' % B)

            # if url is invalid then pass it
        except:
            pass

    print('%s----FUZZING is Completed----' % G)
    sys.exit()

def parse_args():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--domain', help="Domain name to enumerate it's domains")
    parser.add_argument('-f', '--fuzz', help="Fuzz input to enumerate it's bruteforce")
    parser.add_argument('-w', '--wordlist', help="Input the your text file link")
    parser.add_argument('-b', '--blind', help='Blind the status module')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    # print(args.domain)
    # print(args.wordlist)
    # print(args.fuzz)
    # print(args.blind)
    # print(args.domain == -1)
    if args.fuzz:
        if args.blind:
            requter_blind(args.fuzz, args.wordlist, args.blind)
        else:
            requter_fuzz(args.fuzz, args.wordlist)
    if args.domain:
        requter_url(args.domain)
