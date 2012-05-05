class Tests(object):

	def test_set(self):
		"""
			Returns set of test ids.
		"""
		raise NotImplementedError()

	def data_set(self):
		"""
			Returns dictionary mapping data id
			to file format (TEXT or BINARY).
		"""
		raise NotImplementedError()

	def test(self, test_id, data_id):
		"""
			Returns path to the test data file.
		"""
		raise NotImplementedError()


class Statements(object):
	pass


class Utilities(object):

	def checker(self):
		"""
			Returns path to the checker folder.
		"""
		raise NotImplementedError()

	def validator(self):
		"""
			Returns path to the validator folder.
			Returns None if no validator is provided.
		"""
		raise NotImplementedError()


class Driver(object):
	"""
		Problem driver.
		Implements format-independent access
		to problem internals.
	"""

	def convert(self, destination):
		"""
			Converts problem into internal format.
		"""
		raise NotImplementedError()

	def problem(self):
		"""
			Returns bacs.xsd.problem.ProblemType instance.
		"""
		raise NotImplementedError()

	def info(self):
		"""
			Returns bacs.xsd.problem.InfoType instance.
		"""
		raise NotImplementedError()

	def tests(self):
		"""
			Returns Tests instance.
		"""
		raise NotImplementedError()

	def statements(self):
		"""
			Returns Statements instance.
		"""

	def profiles(self):
		"""
			Returns bacs.xsd.problem.ProfilesType instance.
		"""
		raise NotImplementedError()

	def utilities(self):
		"""
			Returns Utilities instance.
		"""
		raise NotImplementedError()
