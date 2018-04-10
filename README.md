
# Python Sound Tools Library

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

   



