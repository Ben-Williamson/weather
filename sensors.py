import interrupt_client, MCP342X, wind_direction, HTU21D, bmp085, tgs2600, ds18b20_therm, json, wind_speed
from time import strftime

pressure = bmp085.BMP085()
temp_probe = ds18b20_therm.DS18B20()
air_qual = tgs2600.TGS2600(adc_channel = 0)
humidity = HTU21D.HTU21D()
#wind_dir = wind_direction.wind_direction(adc_channel = 0, config_file="wind_direction.json")
#interrupts = interrupt_client.interrupt_client(port = 49501)

class measure:
	def temperature():
		return temp_probe.read_temp()
	def wind_direction():
		return wind_dir.get_value(10)
	def air_qual():
		return air_qual.get_value()
	def pressure():
		return pressure.get_pressure()
	def humidity():
		return humidity.read_humidity()
	def wind_speed():
		return wind_speed.measure()
	def rain():
		return interrupts.get_rain()
	def all():
		return {
		  "temperature": measure.temperature(),
		  ##"wind_direction": measure.wind_direction(),
		  "air_qual": measure.air_qual(),
		  "pressure": measure.pressure(),
		  "humidity": measure.humidity(),
		  "wind_speed": measure.wind_speed(),
		  #"rain": measure.rain(),
		  "rain": 0,
		  "time": strftime("%H:%M:%S")
		}
