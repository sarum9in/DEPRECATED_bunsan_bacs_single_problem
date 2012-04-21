
class Driver(object):
	"""
		Problem driver.
		Implements format-independent access
		to problem internals.
	"""

	def problem(self):
		"""
			Returns bacs.xsd.problem.ProblemType.
		"""
		raise NotImplementedError()

