from setuptools import setup

setup(
    name="my_hello_library",
    version="0.2.0",
    description="A simple Python library that provides a hello_world function.",
    author="Your Name",
    author_email="your@email.com",
    license='MIT',
   # py_modules=["my_hello_library"],  # Use py_modules for a single module
    url='https://github.com/luketych/my_hello_library',
    packages=['my_hello_library'],
    # scripts=['bin/test.py'],
    zip_safe=False
)
