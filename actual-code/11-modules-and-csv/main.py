import utils # alias using 'as'
from utils import add as a

# import numpy as np
# import pandas as pd

from datetime import datetime

utils.printer("This is a specific printer.")
print(utils.MAX)
print(utils.add(1,2))

print(a(4,5))

print(datetime.now())