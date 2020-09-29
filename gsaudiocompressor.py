"""
Audio Compressor, dynamic compression of an ausio signal in real time, for amateur radio applications, with keyboard control to switch on/off the compression, and to set the compression level.
Gerald Schuller, April 2015
"""

import pyaudio
import struct
import math
#import array
import numpy as np
#import scipy
#import matplotlib.pyplot as plt
import cv2

CHUNK = 256 #Blocksize
WIDTH = 2 #2 bytes per sample
CHANNELS = 1 #2
RATE = 16000  #Sampling Rate in Hz



compression=True;
#Compression strengh default:
A=20;

def loglimit(x,A):
   #y=np.sign(x)*np.log(np.abs(x)+1)/np.log(32768)*32767;
   #u-Law
   #y=np.sign(x)*np.log(np.abs(255.0*x/32767.0)+1)/np.log(256.0)*32767.0;
   #general compression Factor A:
   #A=2.550
   y=np.sign(x)*np.log(np.abs(A*x/32767.0)+1)/np.log(A+1)*32767.0;
   #x=x-0.5*x*x;
   #x=16*x;
   #if abs(x)< 10000:
   #   y=x;
   #else: 
   #   y=scipy.sign(x)*10000;
   
   return y;


#f=plt.figure();
#werte=np.arange(-32767,32676);
#plt.plot(werte,loglimit(werte));
#plt.title('Compression Curve')
#f.show()

p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                #input_device_index=10,
                frames_per_buffer=CHUNK)
                

print("* recording")



#Loop for the blocks:
#for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
i=0
power=0.0
maxim=0.0
while(True):
    i=i+1
    #For bar graph: set to dark grey:
    bar=np.ones((100,500,3))*0.1
    
    #Reading from audio input stream into data with block length "CHUNK":
    data = stream.read(CHUNK)
    #Convert from stream of bytes to a list of short integers (2 bytes here) in "samples":
    #shorts = (struct.unpack( "128h", data ))
    shorts = (struct.unpack( 'h' * CHUNK, data ));
    #samples=list(shorts);
    samples=np.array(list(shorts),dtype=float);
    #Compression function:
    #(comment out for no compression)
    if compression:
       samples=loglimit(samples,A)
    samples=np.clip(samples,-32000,32000)

    #power=0.8*power+0.2*np.round(np.linalg.norm(samples)**2/CHUNK/512e6*500)
    #average power per sample (/np.sqrt(CHUNK), converted to a peak for a sinusoid (factor 1.414), normalized to range 500.
#If Average power appears high than the average peak, the wave form is becoming more similar to a rectangular wave:
    power=0.9*power+0.1*np.round(np.linalg.norm(samples)/np.sqrt(CHUNK)*1.414/32767.0*500)
    #print("power=",power)
    if(power>500):
       power=500
    maxim=0.9*maxim+0.1*np.max(np.abs(samples))/32767.0*500
    #print("samples=", samples[0:10])
    #print("maxim=",maxim)
    if(maxim>500):
       maxim=500
    #set green channel to power bar:
    bar[0:50,0:int(power),1]=np.ones((50,int(power))) 
    #set red channel for maximum bar:
    bar[50:100,0:int(maxim),2]=np.ones((50,int(maxim))) 
    #write bar every 4th block:
    if(np.mod(i,4)==0):
       bartext=np.zeros((100,500,3))
       cv2.putText(bartext,"Compression on/off: key c, compr. strength: +/- keys", (20,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,100,100))
       cv2.putText(bartext,"Quit: key q, Green: average power, Red: average peak", (20,40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,100,100))
       if compression == False:
          cv2.putText(bartext,"Compression off", (20,70), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,100,100))
       else:
          cv2.putText(bartext,"Compr. strength="+str(A), (20,70), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,100,100))
       cv2.imshow('Aussteuerung',bar+bartext)

    samples=samples.astype(int)
    #converting from short integers to a stream of bytes in data:
    data=struct.pack('h' * len(samples), *samples);
    #Writing data back to audio output stream: 
    stream.write(data, CHUNK)
    #Keep window open until key 'q' is pressed, toggle compression with key 'c':
    key=cv2.waitKey(1) & 0xFF
    if key == ord('c'):
       compression=not compression;
    if key == ord('+'):
       compression=True
       A=A+5;
       A=np.clip(A,1,255)
       #print("Compression strength= ",A);
    if key == ord('-'):
       compression=True
       A=A-5;
       A=np.clip(A,1,255)
       #print("Compression strength= ",A);
    if key == ord('q'):
        break
print("* done")

cv2.destroyAllWindows()
stream.stop_stream()
stream.close()

p.terminate()

