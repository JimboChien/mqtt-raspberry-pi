import Adafruit_DHT
import time

while True:
  h, t = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 14)
  if h is not None and t is not None:
    print(f"Temp: {t:3>} °C / {t*1.8+32:3>} °F")
    print(f"Humidity: {h:3>} %\n")
  else:
    print("Failed to get reading. Try again!")
  time.sleep(1)
