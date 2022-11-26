import cv2
import face_recognition
from time import sleep

myfile = "test.txt"


def head_movements():
	Camera = cv2.VideoCapture(0)
	_, frame = Camera.read()
	
	frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	box = face_recognition.face_locations(frameRGB)
	
	if len(box) < 1 and len(box[0]) < 4:
		print(len(box[0]))
		head_movements()
	cx_ = (box[0][3] + box[0][1]) / 2
	cy_ = (box[0][3] + box[0][1]) / 2
	cx = cx_
	cy = cy_
	
	MIN_MOVE = 20
	
	print('here')
	
	while True:
		
		_, frame = Camera.read()
		
		frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
		box = face_recognition.face_locations(frameRGB)
		
		if (box != []):
			cx = (box[0][3] + box[0][1]) / 2
			cy = (box[0][0] + box[0][2]) / 2
			# cv2.rectangle(frame, (box[0][3], box[0][2]), (box[0][1], box[0][0]), (0, 0, 255), 2)
			
			# if person moves head to right or left: disable the navigation
			# if person doesn't go left and right for 1 second, then he's focused
			f = open("test.txt", "w")
			f.write("")
			if abs(cx - cx_) < abs(cy - cy_):
				if cy - cy_ > MIN_MOVE:
					f.write("0")
					print('DOWN')
				elif cy - cy_ < -MIN_MOVE:
					f.write("1")
					print('UP')
			else:
				if cy - cy_ > MIN_MOVE:
					f.write("2")
					print('LEFT')
				elif cy - cy_ < -MIN_MOVE:
					f.write("3")
					print('RIGHT')
			f.close()
			# sleep(1)
		
		
		cv2.imshow("unlock Face", frame)
		key = cv2.waitKey(30)
		cx_ = cx
		cy_ = cy
		if key == 27:
			break


head_movements()
