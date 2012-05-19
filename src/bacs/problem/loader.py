from os.path import join


class Loader(object):

    def __init__(self, config):
        """
            config is dictionary that contains
            the following options:
            TODO
        """
        self._config = config

    def get_format(self, path):
        """
            Retrieves format name.
        """
        with open(join(path, "format")) as fmt:
            return fmt.read().strip()

    def load(self, path):
        """
            Loads problem,
            returns bacs.problem.Driver instance
            implementing problem format.
        """
        format = self.get_format(path)
        bacs = __import__('bacs.problem.drivers.{}'.format(format))
        driver_module = getattr(bacs.problem.drivers, format)
        return driver_module.Driver(path)


__all__ = ['Loader']
