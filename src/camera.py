import copy
import numpy as np
import glfw
from PIL import Image
import cv2
import face_recognition
from time import sleep
import subprocess
import re

from transform import normalized


# https://learnopengl.com/Getting-started/Camera
class Camera:
	def __init__(self):
		# Camera position
		self.cameraPos = np.array((131.0, 162.0, 110.0))
		# Camera direction
		self.cameraTarget = np.array((0.0, 0.0, 0.0))
		self.cameraDirection = normalized((self.cameraPos - self.cameraTarget))
		# Right axis
		self.up = np.array((0.0, 1.0, 0.0))
		self.cameraRight = normalized(np.cross(self.up, self.cameraDirection))
		# Up axis
		self.cameraUp = np.cross(self.cameraDirection, self.cameraRight)
		
		# Walk Around
		self.cameraFront = np.array((0.0, 0.0, 0.1))
		
		self.sensitivity = 0.01
	
	def processInput(self, viewer, window, deltaTime, x):
		y_extreme = 162
		x_extreme = 131
		if len(x) > 0:
			x = int(x)

			if x == 0 and self.cameraPos[1] - 2.0 >= -y_extreme:
				self.cameraPos[1] -= 2.0
				print("moving DOWN")

			elif x == 1 and self.cameraPos[1] + 2.0 <= y_extreme:
				self.cameraPos[1] += 2.0
				print("moving UP")

			elif x == 2:
				if (self.cameraPos[0] + 1.5) >= x_extreme:
					self.cameraPos[0] = x_extreme
				else:
					self.cameraPos[0] += 1.5
				print("left")

			elif x == 3:
				if (self.cameraPos[0] - 1.5) <= -x_extreme:
					self.cameraPos[0] = -x_extreme
				else:
					self.cameraPos[0] -= 1.5
				print("right")

			else:
				print("")
	
		if glfw.get_key(window=window, key=glfw.KEY_UP) and self.cameraPos[1] + 2.0 <= y_extreme:
			self.cameraPos[1] += 2.0
			print("moving UP")
		if glfw.get_key(window=window, key=glfw.KEY_RIGHT):
			if (self.cameraPos[0] - 1.5) <= -x_extreme:
					self.cameraPos[0] = -x_extreme
			else:
				self.cameraPos[0] -= 1.5
			print("right")
		if glfw.get_key(window=window, key=glfw.KEY_LEFT):
			if (self.cameraPos[0] + 1.5) >= x_extreme:
					self.cameraPos[0] = x_extreme
			else:
				self.cameraPos[0] += 1.5
			print("left")
		if glfw.get_key(window=window, key=glfw.KEY_DOWN) and self.cameraPos[1] - 2.0 >= -y_extreme:
			self.cameraPos[1] -= 2.0
			print("moving DOWN")

		# if glfw.get_key(window=window, key=glfw.GLFW_KEY_R):
		# 	self.cameraPos[1] -= 2.0
		# 	print("moving DOWN")
		print(self.cameraPos)

	
	def cameraPositionXZ(self):
		return 0
	
	def get_cameraPos(self):
		return self.cameraPos
	
	def get_cameraFront(self):
		return self.cameraFront
	
	def get_cameraUp(self):
		return self.up
