
import matplotlib.pyplot as plt

from datetime import timedelta, date

# the list with dates are generated using code from:
# https://www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-50.php


fran = input("Ange datum du vill läsa från: yyyy-mm-dd ")
till = input("Ange datum du vill läsa till: yyyy-mm-dd ")
#fran = "1950-01-01" exempel
#till = "1950-12-31"
    
fran2 = fran.replace('-',' ')
till2 = till.replace('-',' ')
    
fran2 = fran2.split()
till2 = till2.split()
        
############ Skapar lista med alla datum mellan de önskade datumen. Används som x-axel i plotten
def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)
    
datList = []

start_dt = date(int(fran2[0]), int(fran2[1]), int(fran2[2]))
end_dt = date(int(till2[0]), int(till2[1]), int(till2[2]))
for dt in daterange(start_dt, end_dt):
    datList.append(dt.strftime("%Y-%m-%d"))
        
############
    
temper_list = []  # lista som temperaturerna läggs in i
    
def ladda_csv(filename):    # Skapar funktionen som hämtar temperaturen kl 15:00
    import csv
    
    with open(filename, 'r') as csvFile: # öppnar filen
        reader = csv.reader(csvFile)

        for row in reader:
            row_str = ''.join(row)
            current_row = row_str.split(';')
            if current_row[0] in datList and current_row[1] == '15:00:00':
                temper_list.append(current_row[2])
           
# csv-filen kommer härifrån: https://www.smhi.se/data/meteorologi/ladda-ner-meteorologiska-observationer/#param=airtemperatureInstant,stations=all
ladda_csv('smhi-opendata_1_117160_20210713_103431.csv') # Anropar ladda_csv- funktionen ovan
tempen = [float(i) for i in temper_list]

xx = range(len(datList))
xx = list(xx)
plt.plot(xx,tempen)
plt.xlabel("Dagar")        # lägger till info till plotten
plt.ylabel("Temperatur [C]") 
plt.title("Temperatur vid 15:00 mellan " + fran + " och " + till)
plt.grid()


plt.show()
