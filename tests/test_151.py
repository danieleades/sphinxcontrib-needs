from sphinx.application import Sphinx
from sphinx_testing import with_app


@with_app(buildername='html', srcdir='doc_test/151-validate-color')
def test_151(app: Sphinx, status, warning):
    pass
