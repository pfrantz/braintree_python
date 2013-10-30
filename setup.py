import distutils.core
import sys

# a hack to just get the version from without calling the package init 
# which is necessary as the import will fail on python > 3 due to the 
# 2to3 needing to be run as part of the install
sys.path.append("braintree")
from version import Version

# Importing setuptools adds some features like "setup.py develop", but
# it's optional so swallow the error if it's not there.
try:
    import setuptools
except ImportError:
    pass

major, minor = sys.version_info[:2]

kwargs = {}
if major >= 3:
    import setuptools  # setuptools is required for use_2to3
    kwargs["use_2to3"] = True

distutils.core.setup(
    name="braintree",
    version=Version,
    description="Braintree Python Library",
    author="Braintree",
    author_email="support@braintreepayments.com",
    url="https://www.braintreepayments.com/docs/python",
    packages=["braintree", "braintree.exceptions", "braintree.util", "braintree.test", "braintree.util.http_strategy"],
    package_data={"braintree": ["ssl/*"]},
    install_requires=["requests>=0.11.1,<3.0"],
    zip_safe=False,
    **kwargs
)
