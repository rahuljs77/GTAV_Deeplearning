# GTAV_Deeplearning
In this project I have used deep learning techniques to train a mulit-variant regression network to drive autonomously
in the popular game Grand Theft Auto V. The deep learning model used was based on Vgg-16 trained on imagenet data.
The final layer was chopped of and then followed by 4 fully connected layers with dropout layers in between. The model takes
(100 x 100 x 3) images a input and gives 2 values, the steering and the throttle as the output. This model used takes lower time to 
converge and lower trainable parameters compared to Nvidia's end to end architecture
