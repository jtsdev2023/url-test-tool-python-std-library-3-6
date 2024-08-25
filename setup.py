# setup.py

from distutils.core import setup


setup(
    name='url-tool',
    version='1.0',
    description='URL test tool using only the Python standard library and backwards compatible with Python 3.6',
    author='JT. Sizemore',
    author_email='jtsdev2023@gmail.com',
    url='https://github.com/jtsdev2023/url-test-tool-python-std-library-3-6/tree/development',
    packages=['url_tool'],
    license='GPLv3',
    long_description=open('README.md', encoding='utf-8').read(),
    requires=['urllib3', 'requests']
)
