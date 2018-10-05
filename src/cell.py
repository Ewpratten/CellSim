from enum import Enum

Stage = Enum("Stage", "Interphase Mitosis")

# class DNA(object):


class Cell(object):
	
	def __init__(self, cell_id, non_mitosis_len, no_food):
		self.is_mitosis = False
		self.cell_id = int(cell_id)
		self.mitosis_countdown = int(non_mitosis_len)
		self.mitosis_countdown_legnth = self.mitosis_countdown
		self.no_food_alive = int(no_food)
		self.no_food_alive_backup = self.no_food_alive
		
		self.alive = True
	
	def __resetNFA(self):
		self.no_food_alive = self.no_food_alive_backup
	
	def progress(self, tick, food):
		# print("Cell: " + str(self.cell_id) + " Simulated progression on tick " + str(tick) + " with food "+ str(food))
		
		food_required = 2
		food_gen = 0.1
		
		if food - food_required >=0:
			if self.mitosis_countdown < 1:
				self.__resetNFA()
				self.mitosis_countdown = self.mitosis_countdown_legnth
				return [food - food_required, self.alive, True]
			else:
				# print(self.mitosis_countdown_legnth)
				self.mitosis_countdown = self.mitosis_countdown - 1
				return [food + food_gen, self.alive, False]
		
		else:
			if self.no_food_alive < 0:
				self.alive = False
			else:
				self.no_food_alive -= 1
			
			return [food, self.alive, False]
		