# import modules
import board
import time
import adafruit_dht
import pandas as pd
from datetime import datetime
from app import db
from index import Environment


# bring csv into dataframe (commenting out while we make transition to db)
# df = pd.read_csv('/home/pi/secondDashing/data/tempData.csv')

# assign readings to sensor from GPIO 23
dhtSensor = adafruit_dht.DHT11(board.D23)

# loop
while True:

	try:

		# add new value
		e = Environment(temperature=dhtSensor.temperature, humidity=dhtSensor.humidity, timestamp=datetime.utcnow())
		db.session.add(e)
		db.session.commit()

		# write the new dataframe to the csv
		# df.to_csv('/home/pi/secondDashing/data/tempData.csv', index=False)

		# take a reading every 5 minutes
		time.sleep(300)

	# address occasional runtime error
	except RuntimeError:

		continue
