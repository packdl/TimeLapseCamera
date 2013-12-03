import os
import time
import sys
import argparse
import re
import subprocess

PATH = 'timelapsecamera'
T_PATTERN = '[0-9]{2}:[0-9]{2}:[0-9]{2}'

parser = argparse.ArgumentParser(description = 'Time lapse video program')
parser.add_argument('-t', default = '01:00:00', help = 'Time in the format hh:mm:ss. Default is 1 hour.')
parser.add_argument('-f', default=0.10, help = 'Frame rate. Format as a float. Default is 0.10.')



def validate_input():
    time_match = re.match(T_PATTERN, t)
    

def create_dir(path):
    try:
        os.mkdir(path)
    except OSError:
        pass
    os.chdir(path)
    DIR = str(int(time.time()))   #Creates a dir based on the current time
    try:
        os.mkdir(DIR)
    except OSError:
        pass
    os.chdir(DIR)
    pass

def my_arguments():
    
    ns = parser.parse_args()
    if not re.match(T_PATTERN, ns.t):
        ns.t = '01:00:00'
    try:
        fps = float(ns.f)
        if fps <= 0.0:
            ns.f = '0.10'
    except ValueError:
        ns.f = '0.10'
    return ns
    
def main():
    create_dir(PATH)
    ns = my_arguments()
    
    subprocess.call(["streamer", "-t", ns.t, "-r", ns.f, "-j", "99","-q", "-s", "1900x1425", "-o", "picTest0000.jpeg"])
    subprocess.call(["avconv", "-r", "30", "-i", "picTest%04d.jpeg", "-y", "output.avi"])
    pass

if __name__ == "__main__":
    main()



