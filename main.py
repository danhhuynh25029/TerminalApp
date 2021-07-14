import argparse
import os
def getWeather():
    pass
def getCPU():
    cpu = os.popen("free -t -m").readlines()[-1]
    print("CPU usage : ",cpu[:-1])
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-u","--usage",action="store_true",help="CPU usage")
    ap.add_argument("-t","--time",action="store_true",help="Datetime")
    ap.add_argument("-w","--weather",action="store_true",help="Weather")
    args = vars(ap.parse_args())
    #print(args)
    if args["usage"] == True:
        #print("CPU usage")
        getCPU()
    elif args["time"] == True:
        s = os.popen("date").readline()[:-1]
        print("Datetime now : ",s)
if __name__ == "__main__":
    main()
