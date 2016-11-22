class Queue:
	def __init__(self, capacity):
		self.end = -1
		self.capacity = capacity
		self.line = [None] * self.capacity

	def is_empty(self):
		return True if self.end == -1 else False

	def enter(self, next):
		try:
			self.line[self.end + 1] = next
			self.end += 1
		except IndexError:
			#Fix this to have a changeable capacity!
			pass

	def leave(self):
		try:
			next_up = self.line[0]
			for i in range(self.capacity-1):
				self.line[i] = self.line[i+1]
			return next_up
		except IndexError:
			pass


new_queue = Queue(10)

for i in range(8):
	new_queue.enter(i)

print(new_queue.line)

for i in range(8):
	print(new_queue.leave())

