from pyxb import BIND

from bacs.xsd.problem import (
    ProblemType,
    TestsInfoType,
    StatementType,
    StatementVersionType,
    UtilitiesType)


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
        data_mapper = lambda t: BIND(id=t[0], format=t[1])
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


class StatementVersion(object):

    def lang(self):
        """
            Returns statement version language
        """
        raise NotImplementedError()

    def format(self):
        """
            Returns statement version format
        """
        raise NotImplementedError()

    def package(self):
        """
            Returns statement version package
        """
        raise NotImplementedError()

    def to_xsd(self):
        return StatementVersionType(lang=self.lang(),
                                    format=self.format(),
                                    package=self.package())


class Statement(object):

    def versions(self):
        """
            Returns all statement versions available
        """

    def to_xsd(self):
        """
            Returns bacs.xsd.problem.StatementType instance.
        """
        versions = map(StatementVersion.to_xsd, self.versions())
        return StatementType(*versions)


class Utilities(object):

    def to_xsd(self):
        """
            Returns bacs.xsd.problem.UtilitiesType instance.
        """
        # TODO
        utilities = dict()
        utilities['checker'] = ''
        return UtilitiesType(**utilities)

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
        problem['statement'] = self.statement().to_xsd()
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

    def statement(self):
        """
            Returns Statement instance.
        """
        raise NotImplementedError()

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

__all__ = ['Tests', 'Statement', 'Utilities', 'Driver']
