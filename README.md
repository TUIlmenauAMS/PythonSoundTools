
# Python Sound Tools Library
## The sound library

The file sound.py is a collection of a few practical tools for sound processing in Python.
Use it in Python with: import sound

It has the following functions:

* sound(audio, samplingRate):

    funtion to play back an audio signal, in array "audio", can be mono or stereo. 
    If stereo, each column of "audio" is one channel.
    usage: sound.sound(snd,  Fs)
    audio: array containing the audio wave
    sampligRate: The sampling rate for playback
    
* record(time, Fs, CHANNELS):

Records sound from a microphone to an array snd, for "time" seconds and with sampling rate of Fs samples/sec, also for stereo. E.g. with time= 5s, mono, and Fs= 32000 Hz: import sound; snd=sound.record(5,32000,1),
   for Stereo: snd=sound.record(5,32000,2)
    
For reading and writing sound files it uses scipy.io.wavfile :

* wavread(sndfile):

   This function implements a wavread function, similar to Octave or Matlab, to read a wav sound file into a vector snd and sampling rate info 'Fs' at its return. It supports multi-channel audio. Use it with: import sound; [snd,Fs]=sound.wavread('sound.wav'); or snd,Fs= sound.wavread('sound.wav')
   
* wavwrite(snd,Fs,sndfile):

   This function implements the wawwrite function, similar to Octave or Matlab, to write a wav sound file from a vector snd with sampling rate Fs. It also supports mnulti-channel. With: 
   import sound; 
   sound.wavwrite(snd,Fs,'sound.wav');

## pyrecplay_samplingblock.py
let it run with Python3. It records from the sound card, multiplies the sound with a unit pulse train, and play it back to the sound card. A demonstration of sampling with keeping the zeros in it, and for the sound of aliasing components. 

## pyrecspecwaterfallsampling.py
Let it run with Python3. It display a color waterfall spectrogram of the sound from the soundcard, optionally samples and low pass filters it, and plays it back to the sound card.

Decsribed in this lecture video:
https://youtu.be/qNtj-vCRqGY

##gsaudiocompressor.py
This program does an audio range compression. It applies a logarithmic curve of adjustable strength to the magnitudes of the audio samples. In this way it amlifies weak signals. It needs OpenCV (cv2) for display and control. Start this program with:

python3 gsaudiocompressor.py

##gsaudiocompressor_lcddothat.py
This is basically the same as "gsaudiocompressor.py", bit instead of using cv2 and a monitor, it uses Pimoroni's dothat.lcd for display and control, such that no external keyboard and monitor is needed. The 2 arrow touch buttons on the left of the LCD display are used to increase/decrease the compression level, and the white LED chain on the right of the display indicate the audio level. This is useful for a small, standalone box.
For the display see:

https://shop.pimoroni.com/products/display-o-tron-hat

Start it with 
python gsaudiocompressor_lcddothat.py 


