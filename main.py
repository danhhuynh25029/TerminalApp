import argparse
ap = argparse.ArgumentParser()
ap.add_argument("-u",action="store_const",help="CPU usage",const="y")
ap.add_argument("-t",action="store_const",help="Datetime",const="y")
args = vars(ap.parse_args())
if args["u"] == "y":
    print("CPU usage")
elif args["t"] == "y":
    print("Datetime")
