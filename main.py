import argparse
import os
import requests
def getCovid():
    data = requests.get("https://api.covid19api.com/summary")
    json = data.json()
    l = json["Countries"]
    for i in l:
        if i["CountryCode"] == "VN":
            print("Country\tTotalConfirmed\tTotalDeaths")
            print("{}\t{}\t{}".format(i["Country"],i["TotalConfirmed"],i["TotalDeaths"]))
            break
def getWeather():
    myKey = "e90072222e60645e2f9ed2949daec557"
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Tra%20Vinh&appid="+myKey)
    json = data.json()
    weather = json["weather"]
    temp = json["main"]
    print("City\tdescription\ttemp")
    print("{}\t{}\t{}".format(json["name"],weather[0]["description"],str(temp["temp"]/10)+u"\N{DEGREE SIGN}"+"C"))
def getMemory():
    cpu = os.popen("free -t -m").readlines()[-1]
    a = list(map(int,cpu.split()[1:]))
    print("Memory usage : ",round(a[1]/a[0],2)*100,"%")
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-u","--usage",action="store_true",help="Memory usage")
    ap.add_argument("-t","--time",action="store_true",help="Datetime")
    ap.add_argument("-w","--weather",action="store_true",help="Weather")
    ap.add_argument("-c","--covid",action="store_true",help="Information covid")
    args = vars(ap.parse_args())
    #print(args)
    if args["usage"] == True:
        #print("CPU usage")
        getMemory()
    elif args["time"] == True:
        s = os.popen("date").readline()[:-1]
        print("Datetime now : ",s)
    elif args["weather"] == True:
        getWeather()
    elif args["covid"] == True:
        getCovid()
if __name__ == "__main__":
    main()
