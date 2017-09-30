def int_to_time(seconds):
	time = Time()
	minutes, time.second = divmod(seconds, 60)
	time.hour, time.minute = divmod(minutes, 60)
	return time

class Time:

	def __radd__(self, other):
		return self.__add__(other)

	def __init__(self, hour=0, minute=0, second=0):
		self.hour = hour
		self.minute = minute
		self.second = second

	def __str__(self):
		return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

	def __add__(self, other):
		if isinstance(other, Time):
			return self.add_time(other)
		else:
			return self.increment(other)

	def time_to_int(self):
		second = (self.hour * 60 + self.minute) * 60 + self.second
		return second

	def add_time(self, other):
		seconds = self.time_to_int() + other.time_to_int()
		return int_to_time(seconds)

	def time_to_int(self):
		second = (self.hour * 60 + self.minute) * 60 + self.second
		return second

	def print_time(self):
		print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))

	def increment(self, seconds):
		seconds += self.time_to_int()
		return int_to_time(seconds)

	def is_after(self, other):
		return self.time_to_int() > other.time_to_int()


	#Represents the time of day.

	#attributes: hour, minute, second

duration = Time(1, 35)

time = Time(9, 45)

print(60 + time)

#x = time + duration

#print(time + duration)

#print(time + 60)