"""
//  soundfx.py
//  
//
//  Created by Pete Colasacco on 1/2/26.
//

"""
from pyo import *

# 1. Boot and start the audio server
s = Server().boot()
s.start()

# 2. Create a white noise source with an amplitude (mul) of 0.3
noise = Noise(mul=0.3)

# 3. Apply a Butterworth low-pass filter to the noise
# freq parameter determines the filter cutoff frequency
filter = ButLP(noise, freq=1000).out()

# 4. Keep the script running until the user presses Enter
input("Press Enter to stop the noise effect...")

# 5. Stop the server when done
s.stop()
