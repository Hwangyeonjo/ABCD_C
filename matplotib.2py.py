# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

y = [5, 3, 7, 10, 9, 5, 3.5, 8]
x = range(len(y))
plt.bar(x, y, width=0.7, color="blue")
plt.show()