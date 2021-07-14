import argparse
import os
def getWeather():
    pass
def getMemory():
    cpu = os.popen("free -t -m").readlines()[-1]
    a = list(map(int,cpu.split()[1:]))
    print("Memory usage : ",round(a[1]/a[0],2)*100,"%")
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-u","--usage",action="store_true",help="Memory usage")
    ap.add_argument("-t","--time",action="store_true",help="Datetime")
    ap.add_argument("-w","--weather",action="store_true",help="Weather")
    args = vars(ap.parse_args())
    #print(args)
    if args["usage"] == True:
        #print("CPU usage")
        getMemory()
    elif args["time"] == True:
        s = os.popen("date").readline()[:-1]
        print("Datetime now : ",s)
if __name__ == "__main__":
    main()
