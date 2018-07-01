import cv2;
import numpy;
import os;

"""
it is also possible to generate a random Numpy array directly (and more efficiently) using a statement such as numpy.random. 
randint(0, 256, 120000).reshape(300, 400). The only reason we are using os.urandom() is to help demonstrate conversion from raw bytes.
"""

# Make an array of 120.000 randomm bytes.
randomByteArray = bytearray(os.urandom(120000));

flatNumpyArray = numpy.array(randomByteArray);

# Convert the array to make a 400*300 grayscale image.
grayImage = flatNumpyArray.reshape(300, 400);

cv2.imwrite('RandomGray.png', grayImage);

# Convert the array to make a 400*100 color image
bgrImage = flatNumpyArray.reshape(100, 400, 3);

cv2.imwrite('RandomColor.png', bgrImage);

