#
# Produces simple stats for each dataset.
#
import pandas as pd

airline_data = pd.read_csv("data/airline.csv")
airport_data = pd.read_csv("data/airport.csv")
lounge_data = pd.read_csv("data/lounge.csv")
seat_data = pd.read_csv("data/seat.csv")

data = [airline_data, airport_data, lounge_data, seat_data]
names = ["Airline", "Airport", "Lounge", "Seat"]
for i in range(0,len(data)):
    print "Dataset: %s\nNum. Samples: %d\n\nNum. Values per Column" % (names[i], len(data[i]))
    for c in data[i].columns:
        print "(%s) %s: %d" % (data[i][c].dtype, c, data[i][c].count())
    print "\n\n"