import os
import sys
from datetime import datetime
from bson import json_util
import json

import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)

from test.blockchaintest import *
from test.bloquesIgualesTest import *
from test.bloquetest import *
from test.singletontest import *
from test.bloques100test import *