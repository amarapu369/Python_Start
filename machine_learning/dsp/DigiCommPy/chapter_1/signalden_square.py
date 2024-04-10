import numpy as np 
def square_wave(f,overSampRate,nCyl):
  fs = overSampRate*f # sampling frequency
  t = np.arange(0,nCyl*1/f-1/fs,1/fs) # time base
  g = np.sign(np.sin(2*np.pi*f*t)) # replace with cos if a cosine wave is desired
  return (t,g) # return time base and signal g(t) as tuple
  
  """
   Generate square wave signal with the following parameters Parameters:
   f : frequency of square wave in Hertz overSampRate : oversampling rate (integer)
   nCyl : number of cycles of square wave to generate Returns:
   (t,g) : time base (t) and the signal g(t) as tuple
   Example:
   f=10; overSampRate=30;nCyl = 5;
   (t,g) = square_wave(f,overSampRate,nCyl)
   """
