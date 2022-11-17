import copy
import numpy as np
import glfw
from PIL import Image

from transform import normalized


# https://learnopengl.com/Getting-started/Camera
class Camera:
	def __init__(self):
		# Camera position
		self.cameraPos = np.array((0.0, -151.2, 100.0))
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
	
	def processInput(self, window, deltaTime):
		if glfw.get_key(window=window, key=glfw.KEY_UP):
			self.cameraPos += np.array((0.0, 10, 0.0))
		if glfw.get_key(window=window, key=glfw.KEY_DOWN):
			self.cameraPos -= np.array((0.0, 10, 0.0))
			
	def cameraPositionXZ(self):
		return 0

	def get_cameraPos(self):
		return self.cameraPos

	def get_cameraFront(self):
		return self.cameraFront

	def get_cameraUp(self):
		return self.up
