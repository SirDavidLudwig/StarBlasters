from . event_manager import *
from gui.scene.main_menu import *
from gui.scene.world import *
from gui.screen import *
import pygame

class Game():

	# Initialize pygame here
	def __init__(self):
		pygame.init()

		self.__event_manager = EventManager()
		self.__screen = Screen()
		self.__done = False
		self.__clock = pygame.time.Clock()

	# Main loop, returns exit code
	def run(self):
		dt = 0
		self.__screen.set_scene(World())
		# Main loop
		while not self.__done:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.__done = True
				elif event.type == pygame.KEYDOWN:
					for controller in self.__screen.get_scene().get_controllers():
						controller.key_press(event)
				elif event.type == pygame.KEYUP:
					for controller in self.__screen.get_scene().get_controllers():
						controller.key_release(event)
			for controller in self.__screen.get_scene().get_controllers():
				controller.update()
			self.__event_manager.dispatch()
			self.__screen.tick(dt)
			self.__screen.draw()

			dt = self.__clock.tick(60) / 1000.0
		return 0

	def exit(self):
		self.__done = True
