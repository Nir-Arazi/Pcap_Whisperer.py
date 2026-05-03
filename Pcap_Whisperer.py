import subprocess
import os
import argparse


def File_download():

    Home = os.getcwd()
    Rules_file = os.path.join(Home ,'local.rules')

    if not os.path.exists("local.rules"):   
        with open( Rules_file ,"w") as f:
         subprocess.run(["curl", "-s", "https://raw.githubusercontent.com/Nir-Arazi/Snort_Rules/main/network.rules"], stdout=f)

    return Rules_file
    


def scan_test ():

    arg = argparse.ArgumentParser()
    arg.add_argument("filename")
    Pcap_file = arg.parse_args()
    Pcap_test = Pcap_file.filename

    print()

    if not Pcap_test.endswith((".pcap", ".pcapng")): 
        print("\033[31mError: must be a .pcap or .pcapng file\033[0m")
        exit(1)
    
    else:

        Rules_file = File_download()

    result = subprocess.run(f'sudo snort -c /etc/snort/snort.lua -R {Rules_file} -r {Pcap_test} -A fast -q | awk \'{{$1=$2=$3=""; print "\\033[32m" $0 "\\033[0m"}}\' | sed \'s/:[0-9]*//g\' | sort -u | grep -v dtctedct', shell=True, capture_output=True, text=True)

    if not result.stdout.strip():
        print("\033[32mNo rules were triggered for this pcap file!\033[0m")

    else:
        print("\033[31mMalicious activity was detected.\033[0m")
        print("\033[31m-----------------------------------------------------------------------------------------------------------------------------------------------\033[0m")
        print ()
        print(result.stdout)
        print("\033[31m-----------------------------------------------------------------------------------------------------------------------------------------------\033[0m")


check=subprocess.run(["which","snort" ], capture_output=True, text=True)

if check.returncode == 0:
   
    scan_test ()

else:
    subprocess.run (["sudo", "apt-get", "install", "snort" , "-y"])

    scan_test ()
