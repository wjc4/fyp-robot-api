import os
import logging
import sys
from flask import Flask
application = Flask(__name__)

from .motion_control import *
motion_control = MotionControl()

import robot.routes.command
