# fyp-robot-api

Simple flask app which controls a dc motor controller via GPIO output. crontab is used with launcher.sh to run this application on boot automatically

To use crontab run,
`sudo crontab -e`
Add the following to the end of the editor and save.
`@reboot sh /home/pi/robot-api/launcher.sh`