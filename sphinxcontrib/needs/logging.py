import sphinx
from pkg_resources import parse_version

sphinx_version = sphinx.__version__
if parse_version(sphinx_version) >= parse_version("1.6"):
    from sphinx.util import logging
else:
    import logging  # type: ignore

    logging.basicConfig()  # type: ignore


def get_logger(name):
    return logging.getLogger(name)
