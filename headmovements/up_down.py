import cv2
import numpy as np
import face_recognition

if __name__ == '__main__':
	
	result = []
	
	Camera = cv2.VideoCapture(0)
	_, frame = Camera.read()
	
	frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	box = face_recognition.face_locations(frameRGB)
	
	cx_ = (box[0][3] + box[0][1]) / 2
	cy_ = (box[0][3] + box[0][1]) / 2
	cx = cx_
	cy = cy_
	
	MIN_MOVE = 5
	while True:
		_, frame = Camera.read()
		
		frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
		box = face_recognition.face_locations(frameRGB)
		
		if (box != []):
			cx = (box[0][3] + box[0][1]) / 2
			cy = (box[0][0] + box[0][2]) / 2
			cv2.rectangle(frame, (box[0][3], box[0][2]), (box[0][1], box[0][0]), (0, 0, 255), 2)
			
			# if person moves head to right or left: disable the navigation
			# if person doesn't go left and right for 1 second, then he's focused
			if abs(cx - cx_) < abs(cy - cy_):
				if cy - cy_ > MIN_MOVE:
					print('DOWN')
				elif cy - cy_ < -MIN_MOVE:
					print('UP')
		
		cv2.imshow("unlock Face", frame)
		key = cv2.waitKey(30)
		cx_ = cx
		cy_ = cy
		if key == 27:
			break
