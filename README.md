# Audio and AI
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
  
## Basic preprocessing raw audio
  
 while you can use raw aduio data for AI projects ,its often not because there are methods to extract more useful data from them.
 
 **FFT** - fast fourier transform this algorithm takes a time frame of a wave and returns the frquencies that compose the wave and their power. This is called a spectrogram.
 **STFT** - short term fourier transform. This opperates an fft on a short time frame then shift the frame over slightly and does it again. this works like a video for audio basically. This will be used ALOT as a starting point for preprocessing audio.
### STFT main Parameters 
this works alot like a camera, so to avoid getting into the specifics ill explain it like that.

  **n_fft** - the number off points to calculate an FFT, this basically how big the picture is. NOTE: must be a power of 2, commonly used: 2048,1024,512
  
  **hop length** - how many fft points to shift the frame over. This is like the shutter speed and frames per second. 
  
<img src="https://github.com/wolverine3301/Audio-and-AI/blob/main/pics/wav-spec.png?raw=true" width="625" height="400">

### Mel scale spectrogram
an fft can capture a wide range of frequencies, friquencies up to 1/2 of the sample rate. However human hearing, doesnt pick up many high frequencies and also scales more logrithmically, meaning it is more sensitive to low frequencies and typically noticeable changes are when the loudness (decibles, db) and frequencies are doubled.
Because of this the Mel Scale is typically used for music and speech data. There is no universal definition for this scale and so over-simplifying this, it particians the frequency bins(Hz) into new **n_mels** bins, a new scale HZ to Mels. it's basically the log transform of the FFT, kinda. There are 2 big pros to this. One, you get a spectrogram that better represents the data we care about. Second ,it reduces the amount of data the model will need to process.
### basic preprocessing summary
 * unless you have a reson not to, make sure to process audio as MONO channel
 * always use uncompressed file formats
 * depending on your needs adjust sample rate, hop length and fft points
 * Use mel spectrograms when dealing with human audio
 
## Feature extraction
  Along with the STFT and MEL spectrogram there are some other features that can be useful.
  * **zero crossing and zero crossing rate** - looking back at the raw wave, we can obtain the times and rate where the signal crosses 0. This typically has higher values for highly percussive sounds.
  * **Spectral Centroid** - This indicates where the "centre of mass" for a sound is located and is calculated as the weighted mean of the frequencies present in the sound. If the frequencies in music are same throughout then spectral centroid would be around a centre and if there are high frequencies at the end of sound then the centroid would be towards its end. 
  * **Spectral Rolloff** - Spectral rolloff is the frequency below which a specified percentage of the total spectral energy, ex. 50%, lies.
  * **Mel-Frequency Cepstral Coefficients (MFCC)** - this is sort of a "spectrum-of-a-spectrum".T hey are a small set of features , usually 20, that further compress the mel-spectrogram, but reveal higher view of its shape. https://en.wikipedia.org/wiki/Mel-frequency_cepstrum
  * **chroma frequencies** - This is a transofrm of the STFT into bins similar to the process of making the mel spectrogram, but this uses less bins, typically 12-48. These bins represent semitones / pitch in a musical octave
  
  
