from pyxb import BIND

from bacs.xsd.problem import ProblemType, TestsInfoType


class Tests(object):

	def to_xsd(self):
		"""
			Returns bacs.xsd.problem.TestsInfoType instance.
		"""
		tests = dict()
		# test set
		test_mapper = lambda id: BIND(id=id)
		test_set = map(test_mapper, self.test_set())
		tests['test_set'] = BIND(*test_set)
		# data set
		data_mapper = lambda id, format: BIND(id=id, format=format)
		data_set = map(data_mapper, self.data_set().items())
		tests['data_set'] = BIND(*data_set)
		return TestsInfoType(**tests)

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

	def to_xsd(self):
		"""
			Returns bacs.xsd.problem.StatementsType instance.
		"""
		raise NotImplementedError()


class Utilities(object):

	def to_xsd(self):
		"""
			Returns bacs.xsd.problem.UtilitiesType instance.
		"""
		raise NotImplementedError()

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
		problem = dict()
		problem['info'] = self.info()
		problem['tests'] = self.tests().to_xsd()
		problem['statements'] = self.statements().to_xsd()
		problem['profiles'] = self.profiles()
		problem['utilities'] = self.utilities().to_xsd()
		return ProblemType(**problem)

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

__all__ = ['Tests', 'Statements', 'Utilities', 'Driver']
