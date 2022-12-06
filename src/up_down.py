import cv2
import face_recognition
from time import sleep
import numpy as np

myfile = "test.txt"


def head_movements():
	Camera = cv2.VideoCapture(0)
	ret, frame = Camera.read()
	
	frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	box = face_recognition.face_locations(frameRGB)
	
	if len(box) < 1 and len(box[0]) < 4:
		print(len(box[0]))
		head_movements()
	cx_ = (box[0][3] + box[0][1]) / 2
	cy_ = (box[0][3] + box[0][1]) / 2
	cx = cx_
	cy = cy_
	
	# sensitivity
	MIN_MOVE = 20

	face_cascade = cv2.CascadeClassifier("../headmovements/haarcascade_frontalface_default.xml")
	eye_cascade = cv2.CascadeClassifier("../headmovements/haarcascade_eye.xml")

	while True:
		
		ret, frame = Camera.read()
		
		frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
		box = face_recognition.face_locations(frameRGB)

		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		faces = face_cascade.detectMultiScale(gray, 1.1, 5)
		x, y, w, h = 0, 0, 0, 0
		for (x, y, w, h) in faces:
			cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
			cv2.circle(frame, (x + int(w * 0.5), y +
							  int(h * 0.5)), 4, (0, 255, 0), -1)
		eyes = eye_cascade.detectMultiScale(gray[y:(y + h), x:(x + w)], 1.1, 4)
		index = 0
		eye_1 = [None, None, None, None]
		eye_2 = [None, None, None, None]
		for (ex, ey, ew, eh) in eyes:
			if index == 0:
				eye_1 = [ex, ey, ew, eh]
			elif index == 1:
				eye_2 = [ex, ey, ew, eh]
			cv2.rectangle(frame[y:(y + h), x:(x + w)], (ex, ey),
						 (ex + ew, ey + eh), (0, 0, 255), 2)
			index = index + 1
		if (eye_1[0] is not None) and (eye_2[0] is not None):
			if eye_1[0] < eye_2[0]:
				left_eye = eye_1
				right_eye = eye_2
			else:
				left_eye = eye_2
				right_eye = eye_1
			left_eye_center = (
				int(left_eye[0] + (left_eye[2] / 2)),
				int(left_eye[1] + (left_eye[3] / 2)))

			right_eye_center = (
				int(right_eye[0] + (right_eye[2] / 2)),
				int(right_eye[1] + (right_eye[3] / 2)))

			left_eye_x = left_eye_center[0]
			left_eye_y = left_eye_center[1]
			right_eye_x = right_eye_center[0]
			right_eye_y = right_eye_center[1]

			delta_x = right_eye_x - left_eye_x
			delta_y = right_eye_y - left_eye_y

			# Slope of line formula
			angle = np.arctan(delta_y / delta_x)

			# Converting radians to degrees
			angle = (angle * 180) / np.pi


		if (box != []):
				cx = (box[0][3] + box[0][1]) / 2
				cy = (box[0][0] + box[0][2]) / 2
				# cv2.rectangle(frame, (box[0][3], box[0][2]), (box[0][1], box[0][0]), (0, 0, 255), 2)

				# if person moves head to right or left: disable the navigation
				# if person doesn't go left and right for 1 second, then he's focused
				f = open("test.txt", "w")
				# possibility to stop navigating
				f.write("")
				if abs(cx - cx_) < abs(cy - cy_):
					if cy - cy_ > MIN_MOVE:
						f.write("0")
						print('DOWN')
					elif cy - cy_ < -MIN_MOVE:
						f.write("1")
						print('UP')
				elif abs(cx - cx_) > abs(cy - cy_):
					if cy - cy_ > MIN_MOVE:
						f.write("2")
						print('LEFT')
					elif cy - cy_ < -MIN_MOVE:
						f.write("3")
						print('RIGHT')
				# Provided a margin of error of 10 degrees
				# (i.e, if the face tilts more than 10 degrees
				# on either side the program will classify as right or left tilt)
				elif angle > 17:
					f.write("4")
					print('TILT RIGHT')
				elif angle < -17:
					f.write("5")
					print('TILT LEFT')
				f.close()
				# sleep(1)

		cv2.imshow("unlock Face", frame)
		key = cv2.waitKey(30)
		cx_ = cx
		cy_ = cy
		if key == 27:
			break


head_movements()
