import MCP342X, wind_direction, HTU21D, bmp085, tgs2600, ds18b20_therm, wind_speed, rainfall, wind_direction
from time import strftime

pressure = bmp085.BMP085()
temp_probe = ds18b20_therm.DS18B20()
air_qual = tgs2600.TGS2600(adc_channel = 0)
humidity = HTU21D.HTU21D()

class measure:
	def temperature():
		return temp_probe.read_temp()
	def wind_direction():
		return wind_direction.test()
	def air_qual():
		return air_qual.get_value()
	def pressure():
		return pressure.get_pressure()
	def humidity():
		return humidity.read_humidity()
	def wind_speed():
		return wind_speed.measure()
	def rain():
		return rainfall.measure()
	def all():
		return {
		  "temperature": measure.temperature(),
		  "wind_direction": measure.wind_direction(),
		  "air_qual": measure.air_qual(),
		  "pressure": measure.pressure(),
		  "humidity": measure.humidity(),
		  "wind_speed": measure.wind_speed(),
		  "rain": measure.rain(),
		  "time": strftime("%H:%M:%S")
		}
