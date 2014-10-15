WindyBrew
=========

Python code to control a maplin type RF controlled plug sockect with live wind turbine data.

Hook this up on a Raspberry Pi with the code and circuit from https://github.com/dmcg/raspberry-strogonanoff 

Connect the socket to your kettle, and when you think you need a brew turn the kettle on. If the turbine is producing power then you can have your brew, otherwise windy brew makes you wait until your brew is powered by the wind.

Our turbine uses pusher to share its live output data (so you need their library), once a threshold is reached windybrew turns on the socket and off when the turbine output drops again.

Recommended you can auto-start this script by adding to crontab:

crontab -e

and then add in:

@reboot sudo python /path/to/windybrew.py