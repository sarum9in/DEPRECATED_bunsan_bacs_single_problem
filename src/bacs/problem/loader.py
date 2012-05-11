from os.path import join


def get_format(path):
    """
        Retrieves format name.
    """
    with open(join(path, "format")) as fmt:
        return fmt.read().strip()


def load(path):
    """
        Loads problem,
        returns bacs.problem.Driver instance
        implementing problem format.
    """
    format = get_format(path)
    bacs = __import__('bacs.problem.drivers.{}'.format(format))
    driver_module = getattr(bacs.problem.drivers, format)
    return driver_module.Driver(path)


__all__ = ['get_format', 'load']
