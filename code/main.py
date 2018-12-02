import sensors, time, os, file_functions, graphs

def date():
    return time.strftime("%d-%m-%Y")

times = []
temperature = []
air_qual = []
pressure = []
humidity = []
wind_speed = []
rain = []
wind_direction = []

while True:
    if(os.path.isdir("../data/" + date()) == False):
        os.mkdir("../data/" + date())
        os.mkdir("../data/" + date() + "/csv")
        os.mkdir("../data/" + date() + "/graphs")
        times = []
        temperature = []
        air_qual = []
        pressure = []
        humidity = []
        wind_speed = []
        rain = []

    reading = sensors.measure.all()

    temperature.append(reading["temperature"])
    air_qual.append(reading["air_qual"])
    pressure.append(reading["pressure"])
    humidity.append(reading["humidity"])
    wind_speed.append(reading["wind_speed"])
    rain.append(reading["rain"])
    wind_direction.append(reading["wind_direction"])
    times.append(reading["time"])

    file_functions.write(round(int(temperature[-1]), 2), "../data/Current/temperature.csv")
    file_functions.write(round(int(air_qual[-1]), 2), "../data/Current/air_qual.csv")
    file_functions.write(round(int(pressure[-1]), 2), "../data/Current/pressure.csv")
    file_functions.write(round(int(humidity[-1]), 2), "../data/Current/humidity.csv")
    file_functions.write(round(int(wind_speed[-1]), 2), "../data/Current/wind_speed.csv")
    file_functions.write(round(int(rain[-1]), 2), "../data/Current/rain.csv")
    file_functions.write(round(int(wind_direction[-1]), 2), "../data/Current/wind_direction.csv")

    file_functions.write(temperature, "../data/" + date() + "/csv/temperature.csv")
    file_functions.write(air_qual, "../data/" + date() + "/csv/air_qual.csv")
    file_functions.write(pressure, "../data/" + date() + "/csv/pressure.csv")
    file_functions.write(humidity, "../data/" + date() + "/csv/humidity.csv")
    file_functions.write(wind_speed, "../data/" + date() + "/csv/wind_speed.csv")
    file_functions.write(rain, "../data/" + date() + "/csv/rain.csv")
    file_functions.write(wind_direction, "../data/" + date() + "/csv/wind_direction.csv")
    file_functions.write(times, "../data/" + date() + "/csv/time.csv")

    graphs.create_graph(times, temperature, "Temperature on " + date(), "Time", "Temperature", "../data/" + date() + "/graphs/temperature.png")
    graphs.create_graph(times, air_qual, "Air Quality on " + date(), "Time", "Air Quality", "../data/" + date() + "/graphs/air_qual.png")
    graphs.create_graph(times, pressure, "Pressure on " + date(), "Time", "Pressure", "../data/" + date() + "/graphs/pressure.png")
    graphs.create_graph(times, humidity, "Humidity on " + date(), "Time", "Humidity", "../data/" + date() + "/graphs/humidity.png")
    graphs.create_graph(times, rain, "Rain on " + date(), "Time", "Rain", "../data/" + date() + "/graphs/rain.png")
    graphs.create_graph(times, wind_speed, "Wind Speed on " + date(), "Time", "Wind Speed", "../data/" + date() + "/graphs/wind_speed.png")
    graphs.create_graph(times, wind_direction, "Wind Direction on " + date(), "Time", "Wind Direction", "../data/" + date() + "/graphs/wind_direction.png")

    os.system("sudo cp -r ../data/" + date() + " /var/www/html/data/")
    os.system("sudo cp -r ../data/Current" + " /var/www/html/data/")
    print(time.strftime("%H:%M:%S : Done"))
    #time.sleep(1800)
