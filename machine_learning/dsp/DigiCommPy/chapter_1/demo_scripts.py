def sine_wave_demo():
# Simulate a sinusoidal signal with given sampling rate
   import numpy as np
import numpy as np
import matplotlib.pyplot as plt # library for plotting
from signalgen1 import sine_wave # import the function
f = 100 #frequency = 100 Hz
overSampRate = 250 #oversammpling rate
phase = 0 #1/4*np.pi #phase shift in radians
nCyl = 10 # desired number of cycles of the sine wave
(t,g) = sine_wave(f,overSampRate,phase,nCyl) #function call
plt.plot(t,g) # plot using pyplot library from matplotlib package
plt.title('Sine wave f='+str(f)+' Hz') # plot title
plt.xlabel('Time (s)') # x-axis label
plt.ylabel('Amplitude') # y-axis label
plt.show() # display the figure