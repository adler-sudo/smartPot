# smartPot
## smartPot is a comprehensive potted plant management application. The application is built using Plotly Dash.

### Description
The application utilizes sensors that monitor the environment of your potted plant, including temperature, humidity, and soil moisture. Triggered actions will include watering and sending alerts to the plant-parent. The end goal of the application is to build an application that collects and processes data, then, triggers actions based on the incoming data.


### Getting started:
To get started from the command line:
```ruby
git clone https://github.com/adler-sudo/smartPot.git
cd smartPot
pip install -r requirements.txt
python index.py
```

Then, point your web browser to the address returned in the command line. This is usually something like: 127.0.0.1:8050

### Current state and future plans:
The application has been updated to read to and pull from a sqlite db file. Readings are made from the dht11 sensory every 5 minutes. I have updated the application interface to a cleaner dash format and added dcc.Interval functionality to automatically update the data every 5 minutes from the database file. This provides a live interface to display temperature and humidity of your environment.

The next phase is going to be integration of the soil moisture sensor to the Raspberry Pi. We've purchased an explorer hat to integrate this sensor and, soon, the water pump to provide automatic watering functionality to the plant. We hope to have these new features ready to go here shortly.

Stay tuned and enjoy!
