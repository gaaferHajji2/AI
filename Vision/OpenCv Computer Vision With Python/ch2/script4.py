import cv2;

#this work without opening the camera, the capturing saved in memory then writing to desk.
cameraCapture = cv2.VideoCapture(0);

fps=30 # an assumption
# For Me as test: fps = 15

size= ( int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)), 
	int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)));

videoWriter = cv2.VideoWriter('IT_Gaafer.avi', cv2.VideoWriter_fourcc('I', '4', '2', '0'), fps, size);

sucess, frame = cameraCapture.read();

#Here we Record video for 10-seconds.
#each 30-frame take one second
numFramesRemaining = 10 * fps - 1;

while sucess and numFramesRemaining > 0:
	videoWriter.write(frame)
	success, frame = cameraCapture.read();
	numFramesRemaining -=1;
	#print("Num Of Frames Remaing is: ", numFramesRemaining);#For Debuag and Check if the program work ok.

print ("Finished!!!!");
