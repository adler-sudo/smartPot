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
The application is still in early stages of development. The data is currently being pulled from a .csv file where data was collected at 5 minute intervals over the course of a week using dht sensors connected to a Raspberry Pi. Ultimately, this data will be collected to a database and will be served live to your smartPot application. As you can see, the html is pretty rough, too. I'm going to spend some time getting to know the javascript side of plotly to hopefully beef up my web development skills and put something together that provides for a better user experience.

Stay tuned and enjoy!