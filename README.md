# GTA V Deep Learning
In this project I have used deep learning techniques to train a mulit-variant regression network to drive autonomously
in the popular game Grand Theft Auto V. The deep learning model used was based on Vgg-16 pre-trained on imagenet data.
The final layer was chopped off and 4 fully connected layers with dropout layers in between were added. The model takes
(100 x 100 x 3) images a input and gives 2 values, the steering and the throttle as the output. This model converges faster
and has lower trainable parameters compared to Nvidia's end to end [architecture.](https://images.nvidia.com/content/tegra/automotive/images/2016/solutions/pdf/end-to-end-dl-using-px.pdf)

## Training Data:
+ In order to collect the training data, the game was run in windowed mode in (800 x 600) resolution. Using python the screen and 
the corresponding input form the controller (left analogue stick placement for steering and right and left triggers for throttle) were recorded at 30fps
and the data is stored in the form of an .npy file. 

* The training data was collected only for a specific region on the map(as collecting data for the entire map takes lot of time and resources). 

* Over 200,000 images were collected for the training purposes.

## Data Augumentation:
* All the images were resized to (100 x 100), normalized and converted to HLS format. Majority of the raw data contained only forward throttle and
straight steering angle. Using the raw data for wouldn't yield optimal results as the model will only predict forward throttle and straight steering at every instance.

* In order to solve this issue, all the images with either high steering angle or negative throttle are duplicated with minor changes in the control (noise was added) 
and image data(brightened/darkened image). This resulted in more number of images corresponding to high steering angle and negative throttle. On the contrary the images with forward throttled and straight steering angle were randomly discarded. 

* The result was a balanced data with a similar number of images for different control inputs.

## Training:
* The model was built and trained using Tensorflow 2.1.0.

* 20% of the data was used as Validation data. It was trained for 12 epochs and for a batch size of 128.
Adam optimizer was the selected optimizer and mean squared error was used as loss.

* It was made sure that the validaton loss kept decreasing gradually along with the training loss, the opposite would mean that the model is overfitting, which is undesirable.

+ The model along with the trained weights is saved in a .h5 file.

## Deploying the model:
+ The following points include about how you can implement this model on your own machine.

+ #### Minimun System requirements:
  + Nvidia graphic card (gtx 960m or higher)
  + 4 core intel/Amd CPU
  + 16gb ram
  
+ #### Software/Programs:
  + A modded version of GTA V on steam. Click [here](https://www.youtube.com/watch?v=9zwLiurObSU) for GTA V moding tutorial.
  + Tensorflow-gpu version 2.1.0 and OpenCV. Click [here](https://www.youtube.com/watch?v=xQVOaTUm9lM) for tensorflow gpu installtion tutorial.
  + Python 3.6
  + Vjoy - Download [link](http://vjoystick.sourceforge.net/site/index.php/download-a-install/download)
  + X360ce - Download [link](https://www.x360ce.com/)
  + Anaconda3
+ #### Instructions:
  + Clone the repository into your C drive
  + Install the Vjoy drivers
  + Open X360ce and setup as shown.
  + Open GTA V in windowed mode at 800 X 600 resolution and place the window on top right corner of your screen
  + Open the GTA V mod menu by pressing 'F3' and make the following changes (navigate the menu using numpad)
    + options > godmode - enabled
    + Vehicle options > vehicle godmode - enabled
    + Time > noon, freeze time > enabled (very important as the model hasnt been trained for different times)
    + Weather > clear sunny, freeze weather > enabled (also equally important)
    + Vehicle spawning > open wheel vehicle > select the second option (to load the f1 car) make sure it's red.
   + Now head to this location in the map.
   + Open anaconda terminal and conda activate the package where tensorflow gpu is installed
   + In the terminal head to the directory where the repo has been cloned and run Test_2D.py, wait till you see the steering and throttle values are printed
   + Press P to pause and then click the GTA V window
   + Press P to unpause the model and see the neural network in action!
 + #### Debugging:
   + Incase of any issues run the screen_test.py and joystick_control_test.py to resolve screen recording/virtual controller issues
 
 




