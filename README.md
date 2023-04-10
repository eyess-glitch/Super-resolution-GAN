# 1. Overview
SRGAN is a neural network architecure firstly introduced in the following [paper](https://arxiv.org/pdf/1609.04802.pdf) for upscaling images.

# 2. Training process
This repository contains the source code for the implementation of the SRGAN discussed in the following paper [link](https://arxiv.org/pdf/1609.04802.pdf).
The model was trained in the following way : firstly, the generator is trained with a non GAN approach by minimizing the MSE loss function between the upscaled
image and reconstructed image for roughy 40.000 iteration of 32 batches each on a Google Colab notebook (free-tier); next, both discriminator and generator are
trained with a GAN approach for approximately 20.000 iterations on Google Colab (Pro version).

# 3. Dataset used for training
The dataset (available at the following kaggle [link](https://www.kaggle.com/datasets/scribbless/another-anime-face-dataset)) on which the model was trained is organized in the following way : a folder containing various subfolders, each associated with an id, containing the original image and the downsampled image. The downsampled image was obtained by executing the scripting downsampling.py, which applies a 4x downsampling factor to a specific image. The organization of the folders in different subfolders was realized through a bash script. 

# 4. Model's weights
The model's weights are available [here](https://drive.google.com/drive/folders/19cR8VSN6P2UcbtXPvNtt5GZuDMdFJ_QL?usp=sharing).
