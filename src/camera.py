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
		self.cameraPos = np.array((0.0, 191, 180.0))
		# self.cameraPos = np.array((0, 0, -276.76675199))
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
		# self.cameraFront = np.array((-2.5, 2, -10))
		
		self.sensitivity = 0.01
	
	def processInput(self, window, deltaTime, x):
		if len(x) > 0:
			x = int(x)
			if x == 1 and self.cameraPos[1] < 191:
				self.cameraPos += np.array((0.0, 0.3, 0.0))
				print("moving UP")
			elif x == 0 and self.cameraPos[1] > -191:
				self.cameraPos -= np.array((0.0, 0.3, 0.0))
				print("moving DOWN")
			elif x == 2 and self.cameraPos[1] > -191:
				# left
				self.cameraPos[1] = -191
				print("moving >> DOWN")
			elif x == 3 and self.cameraPos[1] < 191:
				# right
				self.cameraPos[1] = 191
				print("moving >> UP")
			else:
				print("")
	
	# if glfw.get_key(window=window, key=glfw.KEY_UP) and self.cameraPos[1] < 191:
	# 	self.cameraPos += np.array((0.0, 1, 0.0))
	# if glfw.get_key(window=window, key=glfw.KEY_DOWN) and self.cameraPos[1] > -191:
	# 	self.cameraPos -= np.array((0.0, 1, 0.0))
	
	def cameraPositionXZ(self):
		return 0
	
	def get_cameraPos(self):
		return self.cameraPos
	
	def get_cameraFront(self):
		return self.cameraFront
	
	def get_cameraUp(self):
		return self.up
