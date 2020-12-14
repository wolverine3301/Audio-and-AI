# Audio-and-AI
A documentation of my experience using AI applied to audio 

## Introduction
  over the past few months I've decided to research AI applications with audio, things such as text-to-speech , speech-to-text (speech recognition), music generation, ect.
  I'll be trying to make organised as cronological as possible, and assuming very little prior knowledge to digital signal processing.
  
# Data and preprocessing

First things ,the data. below is an example of an audio wave form. Common file types that contain these are **.mp3** , **.mid**, **.aiff** and **.wav**.
There are many others but for this I will be mostly sticking to **.wav** , This is because wav files are uncompressed ,and have the most support for libraries.
Whatever file format you use, I would reccomend making sure they are raw and uncompressed. MP3 for example uses a compression on raw wav files so they take up less space, however when running analysis on a large number of files, your computer will have to reverse this compression for every file.

  <img src="https://github.com/wolverine3301/Audio-and-AI/blob/main/pics/waveform_post.png" width="516" height="138">
  
 The important things to know about raw audio are as follows:
 
  * **Sample rate** - this is how many data points per second make up the wave form. CD quality sample rate is common which is 44100 Hz, so for one second of audio that's 44100 points of data. This can be and maybe should be, down sampled depending on what your working with.
  * **Channels** - so we all know what a stereo is? left and right channels recorded using 2 microphones , or just 2 of the same wave. If you graphed these you would have 2 sperated waves like the one above. Because these 2 wav forms are often very similar and litterally double the data to process, they are converted to a single MONO chennel by averageing, or other method.
  * **Duration** - simply how long in time the wave is
  
  ## preprocessing raw audio
  
 while you can use raw aduio data for AI projects ,its often not because there are methods to extract more useful data from them.
 
 **FFT** - fast fourier transform this algorithm takes a time frame of a wave and returns the frquencies that compose the wave and their power. 
 **STFT** - short term fourier transform. This opperates an fft on a short time frame then shift the frame over slightly and does it again. this works like a video for audio basically. This will be used ALOT as a starting point for preprocessing audio.
### STFT main Parameters 
this works alot like a camera, so to avoid getting into the specifics ill explain it like that.
  **n_fft** - the number off points to calculate an FFT, this basically how big the picture is. NOTE: must be a power of 2, commonly used: 2048,1024,512
  **hop length** - how many fft points to shift the frame over. This is like the shutter speed and frames per second. 
 
 
