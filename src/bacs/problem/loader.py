from os.path import join
import imp


def get_format(path):
	"""
		Retrieves format name.
	"""
	with open(join(path, "format")) as fmt:
		return fmt.read()


def load(path):
	"""
		Loads problem,
		returns bacs.problem.Driver instance
		implementing problem format.
	"""
	format = get_format(path)
	module_name = "bacs.problem.drivers.{}".format(format)
	find_ = imp.find_module(module_name)
	driver_module = imp.load_module(module_name, *find_)
	return driver_module.Driver(path)


__all__ = ['get_format', 'load']
