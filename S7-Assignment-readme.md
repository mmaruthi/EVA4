S7 - Assignment Solution 

Target :

change the code such that it uses GPU

change the architecture to C1C2C3C40 (basically 3 MPs)

total RF must be more than 44

one of the layers must use Depthwise Separable Convolution

one of the layers must use Dilated Convolution

use GAP (compulsory):- add FC after GAP to target #of classes (optional)

achieve 80% accuracy, as many epochs as you want. Total Params to be less than 1M. 


Approach used :

>Made the architecture in C1 / C2/C3 /c4 

>Used 3 Max Poolings 

>Used Padding 

>Used Dilated Kernels 

>Used Depth wise and Point wise Kernels 

>Used GAP and an FC after that 


Results :

>Ran the Network for 20 Epochs 

>No .of parameters is 70K 

>Overall Accuracy achieved is 79% 

>Dog class accuracy is less than 70% , Rest all performed well with more accuracy than 85%

>Probably more epochs will give better results - but its taking lot of time 

>Still working on the modular approach as it failed multiple times. So submitted in a single code for time being.




