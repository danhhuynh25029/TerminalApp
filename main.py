import argparse
import os
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-u",action="store_const",help="CPU usage",const="y")
    ap.add_argument("-t",action="store_const",help="Datetime",const="y")
    args = vars(ap.parse_args())
    if args["u"] == "y":
        print("CPU usage")
    elif args["t"] == "y":
        s = os.popen("date").readline()[:-1]
        print("Datetime now : ",s)
if __name__ == "__main__":
    main()
