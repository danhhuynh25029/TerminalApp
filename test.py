import requests
def showInfo():
    data = requests.get("https://api.covid19api.com/summary")
    json = data.json()
    l = json["Countries"]
    for i in l:
        if i["CountryCode"] == "VN":
            print("Country\tTotalConfirmed\tTotalDeaths")
            print("{}\t{}\t{}".format(i["Country"],i["TotalConfirmed"],i["TotalDeaths"]))
            break
if __name__ == "__main__":
    showInfo()
    degree_sign = u"\N{DEGREE SIGN}"
    print(degree_sign)
