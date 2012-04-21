import os
from os.path import join, splitext, basename
from ConfigParser import SafeConfigParser

from pyxb import BIND

from bacs.xsd.problem import (ProblemType, InfoType,
							ProblemNameType, SolutionTestingProfileType)
from bacs.xsd.settings import TestGroupSettingsType, RlimitType
from bacs.xsd.testing import TestGroupType, WildcardQueryType

import bacs.problem.driver
from bacs.problem.config import ENCODING


class Driver(bacs.problem.driver.Driver):
	"""
		config.ini sections:

		[info]
		name="Problem name"
		authors="author1, author2"
		maintainers="maintainer1, maintainer2"
		source=Problem source

		[rlimits]
		time=0
		memory=0
		cpu=0
		output=0

		[files]
		stdin="input.txt"
		stdout="output.txt"
		stderr="log.txt"
	"""

	def __init__(self, path):
		self._path = path
		self._parse()

	@staticmethod
	def _get_list(section, key):
		if key in section:
			return map(lambda s: s.strip(), section[key].split(','))
		else:
			return []
	
	@staticmethod
	def _compress(dictionary):
		return dict(filter(lambda i, j: j is not None, dictionary.items()))

	def _find_tests(self):
		path = (self._path, 'tests')
		files = os.listdir(path)
		self._data_set = set()
		self._test_set = set()
		tests = dict()
		for i in files:
			name, ext = splitext(basename(i))
			# we do not need period
			data = ext[1:]
			self._data_set.add(name)
			self._test_set.add(data)
			if name not in tests:
				tests[name] = set()
			tests[name].add(data)
		for name, datas in tests.items():
			assert datas==self._data_set

	def _parse(self):
		problem = dict()
		self._config = SafeConfigParser()
		self._config.read(join(self._path, 'config.ini'), ENCODING)
		# info section
		info_ = self._config['info']
		info = dict()
		info['names'] = BIND(ProblemNameType(info_['name'], lang='C'))
		authors = Driver._get_list(info_, 'authors')
		info['authors'] = BIND(*map(BIND, authors))
		maintainers = Driver._get_list(info, 'maintainers')
		info['maintainers'] = BIND(*map(BIND, maintainers))
		info['source'] = info_.get('source')
		info = InfoType(**Driver._compress(info))
		problem['info'] = info
		# tests section
		self._find_tests()
		test_set = BIND(*map(lambda t: BIND(id=t), self._test_set))
		data_set = BIND(*map(lambda d: BIND(id=d, format='TEXT'), self._data_set))
		problem['tests'] = BIND(data_set=data_set, test_set=test_set)
		# statements section
		problem['statements'] = BIND()
		# utilities section
		problem['utilities'] = BIND(checker=BIND())
		# profiles section
		settings = dict()
		if 'rlimits' in info_:
			rlimits = [RlimitType(int(value), id=resource.toupper())
					for resource, value in info_['rlimits']]
			settings['rlimits'] = BIND(*rlimits)
		if 'files' in info_:
			pass
			#settings['files'] = None
		settings = TestGroupSettingsType(**settings)
		full_test_set = WildcardQueryType('*')
		test_group = TestGroupType(id='', settings=settings, test_set=BIND(full_test_set))
		profile = SolutionTestingProfileType(test_groups=BIND(test_group))
		problem['profiles'] = BIND(testing_profiles=BIND(profile))
		# binding
		self._problem = ProblemType(**problem)

	def problem(self):
		return self._problem
