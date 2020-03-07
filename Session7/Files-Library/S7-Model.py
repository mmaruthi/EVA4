from torchsummary import summary 
import torch 
import torch.nn as nn
import torch.nn.functional as F 

## Writing a model as per requirement of assignment 7## 
##  Architecture C1 / C2 / C3 /C4 
##  Total RF must be more than 44 
##  One of the layers must use Depthwise separable convolution 
##  one of the layers must use Dilated convolution 
##  Use GAP compulsory - Add FC after GAP to target no. of classes 
##  Total params to be less than 1M.

class Net(nn.module):
     def __init__(self):
        super(Net, self).__init__()
        
        ## C1 ## 
        Self.convblock1  = nn.sequential(
            nn.conv2d(in_channels = 3, out_channels = 16 , kernel_size =(3,3), padding = 1 , bias = False)
            nn.ReLU(),
            nn.BatchNorm2d(16),
            nn.Dropout(dropout_value)    
        
        # Input - 32*32 , Output - 32*32 , RF = 3 
        
        self.convblock2  = nn.sequential(
            nn.conv2d(in_channels = 16, out_channels = 32 , kernel_size = (3,3), padding = 1 , bias = False)
            nn.ReLU(),
            nn.BatchNorm2d(32),
            nn.Dropout(droupout_value) 
          
         # Input - 32 * 32 , Output - 32 * 32 , RF = 5 
         
         self.convblock3 = nn.sequential(
             nn.conv2d(in_channels = 32 , out_channels = 32 , kernel_size = (3,3), padding =1 , bias = False)
             nn.ReLU(),
             nn.BacthNorm2d(32),
             nn.Dropout(dropout_value)
             
         # Input - 32*32 , output - 32*32 , RF = 7
         
         ## First Max pool block## 
         self.pool1   = nn.Maxpool2d(2,2)
         # Input - 32*32 , Output 16*16 , RF = 8 
         
         ## C2 ##  -- Used a dilated kernel 
         self.convblock4 = nn.sequential(
             nn.conv2d(in_channels = 32 , out_channels = 32 , kernel_size = (3,3), padding =1 , dilation = 2 ,bias = False)
             nn.ReLU(),
             nn.BacthNorm2d(32),
             nn.Dropout(dropout_value)
         # Input - 16*16 , output - 14*14 , RF = 16 
             
         ## Second Max pool Block ## 
         self.pool2   = nn.Maxpool2d(2,2)
         # Input - 14*14 , Output - 7*7 , RF = 18 
         
         ## C3 ##  -- Use Depth wise seperable 
         self.convblock5 = nn.sequential(
             nn.conv2d(in_channels = 32 , out_channels = 32 , kernel_size = (3,3), padding =1 ,bias = False)
             nn.ReLU(),
             nn.BacthNorm2d(32),
             nn.Dropout(dropout_value)
         # Input - 16*16 , output - 14*14 , RF = 16 
         
         
            
      
