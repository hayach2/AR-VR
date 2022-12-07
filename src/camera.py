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
		self.cameraPos = np.array((132, 159, 110.0))
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
		y_extreme = 162
		x_extreme = 132
		y_second_page = 29
		y_third_page = -103

		# top_left = [132, 162, 110]
		# bottom_left = [132, -162, 110]
		# second_page = [132, 29, 110]
		# third_page = [132, -103, 110]

		# top_right = [-132, 162, 110]
		# extreme_bottom = [-132, -162, 110]
		# second_page = [-132, 29, 110]
		# third_page = [-132, -103, 110]
		# print(self.cameraPos[1])
		if len(x) > 0:
			x = int(x)
			if x == 1 and self.cameraPos[1] < y_extreme:
				# x, y, z
				self.cameraPos += np.array((0.0, 1.0, 0.0))
				print("moving UP")
			elif x == 0 and self.cameraPos[1] > -y_extreme:
				self.cameraPos -= np.array((0.0, 1.0, 0.0))
				print("moving DOWN")
			elif x == 2:
				# left
				
				if (self.cameraPos[1] + 45) > y_extreme:
					self.cameraPos[1] = y_extreme
				else:
					self.cameraPos[1] += 45

				# if - y_extreme < self.cameraPos[1] < y_second_page:
				# 	self.cameraPos[1] = y_second_page
				# elif y_second_page < self.cameraPos[1] < y_third_page:
				# 	self.cameraPos[1] = y_third_page
				# elif y_third_page < self.cameraPos[1]:
				# 	self.cameraPos[1] = -y_extreme
				# elif self.cameraPos[1] == - y_extreme:
				# 	self.cameraPos[1] = y_second_page
				# elif self.cameraPos[1] == y_second_page:
				# 	self.cameraPos[1] = y_third_page
				# elif self.cameraPos[1] == y_extreme:
				# 	self.cameraPos[1] = - y_extreme
				# sleep(2)
				print("skipping section up")
			elif x == 3:
				# right

				if (self.cameraPos[1] - 45) < - y_extreme:
					self.cameraPos[1] = - y_extreme
				else:
					self.cameraPos[1] -= 45
				
				
				# if - y_extreme < self.cameraPos[1] < y_second_page:
				# 	self.cameraPos[1] = - y_extreme
				# elif y_second_page < self.cameraPos[1] < y_third_page:
				# 	self.cameraPos[1] = y_second_page
				# elif y_third_page < self.cameraPos[1]:
				# 	self.cameraPos[1] = y_third_page
				# elif self.cameraPos[1] == - y_extreme:
				# 	self.cameraPos[1] = y_third_page
				# elif self.cameraPos[1] == y_second_page:
				# 	self.cameraPos[1] = - y_extreme
				# elif self.cameraPos[1] == y_extreme:
				# 	self.cameraPos[1] = y_second_page
				# sleep(2)
				print("skipping section down")
			elif x == 5:
				# tilt right
				self.cameraPos[0] = - x_extreme
			elif x == 4:
				# tilt left
				self.cameraPos[0] = x_extreme
			else:
				print("")
	
		if glfw.get_key(window=window, key=glfw.KEY_UP):
			self.cameraPos += np.array((0.0, 1, 0.0))
		if glfw.get_key(window=window, key=glfw.KEY_RIGHT):
			self.cameraPos += np.array((1.0, 0, 0.0))
		if glfw.get_key(window=window, key=glfw.KEY_LEFT):
			self.cameraPos -= np.array((1.0, 0, 0.0))
		if glfw.get_key(window=window, key=glfw.KEY_DOWN):
			self.cameraPos -= np.array((0.0, 1, 0.0))
		# print(self.cameraPos)
	
	def cameraPositionXZ(self):
		return 0
	
	def get_cameraPos(self):
		return self.cameraPos
	
	def get_cameraFront(self):
		return self.cameraFront
	
	def get_cameraUp(self):
		return self.up
