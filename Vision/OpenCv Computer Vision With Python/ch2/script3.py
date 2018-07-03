import cv2;

videoCapture = cv2.VideoCapture('small.avi');
fps= videoCapture.get(cv2.CAP_PROP_FPS);
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)), 
	int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)));
	
print("The FBS is : ", fps)
print("The Size is: ", size);

videoWriter=cv2.VideoWriter('smallOut.avi', cv2.VideoWriter_fourcc('I', '4', '2', '0'), fps, size);
success, frame = videoCapture.read();

while success:
	videoWriter.write(frame);
	success, frame=videoCapture.read();
