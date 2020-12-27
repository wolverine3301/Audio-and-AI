# Music Classification and Information retrival
  In order to get to the more advanced projects, there needs to be a good understanding of the data, and features used. Since raw audio data doesn't usually yeild good results or is to large in most cases, and there is a large variety of features we can derive, I decided to run some experiments with this simple project. This will hopfully reveal some guidance and usful features for future projects.

## Prerequisits
* **Data Set** - I will be using the GTZAN data set, availible here http://marsyas.info/downloads/datasets.html . This data set contains 1000 ,30 second, song clips with 10 genres (blues,pop,ect), with 100 samples for each.
* **Libraries** - **Librosa**, **numpy**, **pandas**, **sklearn**, **tensorflow / keras** are the main ones

## Overview
  The goals for this project will be to refine preprocessing techniques, and determine the most useful features to include. In addition, I will try to determine the best and smallest number of fetures to try and obtain a goal of  80% accuracy. I will run one model with various fetures, **(zero crossing rate, mean root-mean-square of energy, mean spectral bandwidth, mean spectral rolloff, mean spectral flatness, mean spectral_centroid, mean spectral contrast)**. These values are calculated by frame so I will be useing the mean of each to represent the entire sample. This will act as a baseline if 80% is unattainable, and will also serve to see if these simpilar derived fetures are more significant than the ones going foward.For the first round of testing I will be using MFCC, chroma frequencies, mel frequencies, again take their averages for each frequency bin.
  
  With the STFT ,audio is basically turned into sets of images (or one long image). Unlike classifying images of cat or dog, audio has a time element where one frame's properties are influnced by its neighboring frames. Two models come to mind for deaaling with images, and time, which are convolutional and recurrent neural nets. However upon some research and my own experimentation they do not perfrom very well in this particular problem and dataset. This could be from a variety of things but is likely due to the short duration and number of samples. For this dataset I found using a simplier dense feed foward net worked very well.
  
 ## Experiment 1
  For the set up, we will be using the same network architecture with the only difference being between the input shape of the base line data(input = 6) and the rest (input = 12). The other 3 datasets will be using 12 fequency bins with their transforms along with a 2048 point fft and hop length of 512 points. The training data for these will be the averaged bin value from the frames of each sample. I am choosing a relativly small network size as a bottleneck, The idea being that the higher accuracy accived with limited recources, suggest the data is more informative
  
  Model: "sequential_1"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
dense_4 (Dense)              (None, 128)               768       
_________________________________________________________________
dense_5 (Dense)              (None, 64)                8256      
_________________________________________________________________
dense_6 (Dense)              (None, 32)                2080      
_________________________________________________________________
dense_7 (Dense)              (None, 10)                330       
=================================================================
Total params: 11,434
Trainable params: 11,434
Non-trainable params: 0
_________________________________________________________________
  
There are 3 fully connected hidden layers each with relu activation, and the output layer with a softmax activaton. I will be doing 3 rounds of test with 10, 15 and 20 epochs respectivly. The Training and validation will be set to 70:30 , so each will be trained on 700 examples and validated on 300. Each will be using "adam" as the optimizer function, and sparse categorical cross entropy as the loss/accuracy function. This is used because we are defining each example as only belonging to one genre/class.

## Results

  <img src="https://github.com/wolverine3301/Audio-and-AI/blob/main/Music_Classification_and_Information_Retrival/plots/music_genre_classification_Test1_accuracy_12.png?raw=true" width="1000" height="800">
