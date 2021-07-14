import argparse
import os
import requests
from prettytable import PrettyTable
def Print():
    pass
def getCovid(country):
    data = requests.get("https://api.covid19api.com/summary")
    json = data.json()
    l = json["Countries"]
    tb = PrettyTable(["Country","TotalConfirmed","TotalDeaths"])
    choose = 0
    if country  == "all":
        choose = 1
    for i in l:
        if choose == 0:
            if i["CountryCode"] == country:
                #print("Country\tTotalConfirmed\tTotalDeaths")
                tb.add_row([i["Country"],i["TotalConfirmed"],i["TotalDeaths"]])
                print(tb)
                #print("{}\t{}\t{}".format(i["Country"],i["TotalConfirmed"],i["TotalDeaths"]))
                break
        else: 
            tb.add_row([i["Country"],i["TotalConfirmed"],i["TotalDeaths"]])
            print(tb)
def getWeather():
    myKey = "e90072222e60645e2f9ed2949daec557"
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Tra%20Vinh&appid="+myKey)
    json = data.json()
    weather = json["weather"]
    #print(weather[0]["description"])
    temp = json["main"]
    tb = PrettyTable(["city","description","temp"])
    tb.add_row([json["name"],weather[0]["description"],str(round(temp["temp"]/10,2))+u"\N{DEGREE SIGN}"+"C"])
    print(tb)
    #print("City\tdescription\ttemp")
    #print("{}\t{}\t{}".format(json["name"],weather[0]["description"],str(round(temp["temp"]/10,2))+u"\N{DEGREE SIGN}"+"C"))
def getMemory():
    memory = os.popen("free -t -m").readlines()
    for i in memory:
        print(i[:-1])
    memoryUsage = memory[-1]
    a = list(map(int,memoryUsage.split()[1:]))
    print("Memory usage : ",round(a[1]/a[0],2)*100,"%")
def main():
    ap = argparse.ArgumentParser(description="Terminal app")
    ap.add_argument("x",help="choose country information covid19 (name/all)")
    ap.add_argument("-m","--memory",action="store_true",help="Memory usage")
    ap.add_argument("-t","--time",action="store_true",help="Datetime")
    ap.add_argument("-w","--weather",action="store_true",help="Weather")
    ap.add_argument("-c","--covid",action="store_true",help="Information covid")
    args = vars(ap.parse_args())
    #print(args)
    if args["memory"] == True:
        #print("CPU usage")
        getMemory()
    elif args["time"] == True:
        s = os.popen("date").readline()[:-1]
        print("Datetime now : ",s)
    elif args["weather"] == True:
        getWeather()
    elif args["covid"] == True:
        getCovid(args["x"])
if __name__ == "__main__":
    main()
