import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
def scipy_square_wave():
    import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
f = 10 # f = 10Hz
overSampRate = 30 # oversampling rate
nCyl = 5 # number of cycles to generate
fs = overSampRate*f # sampling frequency
t = np.arange(start=0,stop=nCyl*1/f,step=1/fs)# time base
g = signal.square(2 * np.pi * f * t, duty = 0.2)
plt.plot(t,g)
plt.show()