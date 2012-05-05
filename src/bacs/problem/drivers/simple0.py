import os
from os.path import join, exists, splitext, basename
from ConfigParser import SafeConfigParser

from pyxb import BIND

from bacs.xsd.problem import (InfoType, ProblemNameType,
	SolutionTestingProfileType, ProfilesType)
from bacs.xsd.settings import TestGroupSettingsType, RlimitType
from bacs.xsd.testing import TestGroupType, WildcardQueryType

import bacs.problem.driver as driver
from bacs.problem.config import ENCODING


class Driver(driver.Driver):
	"""
		config.ini sections:

		[info]
		name="Problem name"
		authors="author1; author2"
		maintainers="maintainer1; maintainer2"
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

		[tests]
		in = "text"
		hint = "text"
	"""

	@staticmethod
	def _get_list(section, key):
		if key in section:
			return map(lambda s: s.strip(), section[key].split(';'))
		else:
			return []
	
	@staticmethod
	def _compress(dictionary):
		return dict(filter(lambda i, j: j is not None, dictionary.items()))

	def __init__(self, path):
		self._path = path
		self._config = SafeConfigParser()
		self._config.read(join(self._path, 'config.ini'), ENCODING)
		self._find_tests()

	def _find_tests(self):
		path = (self._path, 'tests')
		files = os.listdir(path)
		self._data_set = dict()
		self._test_set = set()
		tests = dict()
		for i in files:
			name, ext = splitext(basename(i))
			# we do not need period
			data = ext[1:]
			self._test_set.add(name)
			if data not in self._data_set:
				if 'tests' in self._config and data in self._config['tests']:
					format = self._config.get('tests', data).upper()
				else:
					format = 'TEXT'
				self._data_set[data] = format
			if name not in tests:
				tests[name] = set()
			tests[name].add(data)
		for name, datas in tests.items():
			assert datas==self._data_set

	def info(self):
		info_ = self._config['info']
		info = dict()
		info['names'] = BIND(ProblemNameType(info_['name'], lang='C'))
		authors = Driver._get_list(info_, 'authors')
		info['authors'] = BIND(*map(BIND, authors))
		maintainers = Driver._get_list(info, 'maintainers')
		info['maintainers'] = BIND(*map(BIND, maintainers))
		info['source'] = info_.get('source')
		info = InfoType(**Driver._compress(info))
		return info

	def tests(self, test_id, data_id):
		path = join(self._path, 'tests')

		class Tests(driver.Tests):

			def test_set(self):
				pass

			def data_set(self):
				pass

			def test(self, test_id, data_id):
				return join(path, test_id+'.'+data_id)

		return Tests()

	def statements(self):
		return driver.Statements()

	def profiles(self):
		settings = dict()
		if 'rlimits' in self._config:
			rlimits = [RlimitType(int(value), id=resource.toupper())
					for resource, value in self._config['rlimits']]
			settings['rlimits'] = BIND(*rlimits)
		if 'files' in self._config:
			pass
			#settings['files'] = None
		settings = TestGroupSettingsType(**settings)
		full_test_set = WildcardQueryType('*')
		test_group = TestGroupType(id='', settings=settings, test_set=BIND(full_test_set))
		profile = SolutionTestingProfileType(test_groups=BIND(test_group))
		return ProfilesType(testing_profiles=BIND(profile))

	def utilities(self):
		path = self._path

		class Utilities(driver.Utilities):

			def checker(self):
				return join(path, 'checker')

			def validator(self):
				vpath = join(path, 'validator')
				if exists(vpath):
					return vpath
				else:
					return None

		return Utilities()
