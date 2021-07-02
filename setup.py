from setuptools import setup


with open('README.rst', encoding='utf-8') as fh:
    description = fh.read().strip()

setup(
    name='httpie-snapdsocket',
    description='Snapd socket transport plugin for HTTPie.',
    long_description=description,
    version='1.0.0',
    author='Mickaël Schoentgen',
    author_email='mickael@apible.io',
    license='BSD',
    url='https://github.com/httpie/httpie-snapdsocket',
    py_modules=['httpie_snapdsocket'],
    zip_safe=False,
    entry_points={
        'httpie.plugins.transport.v1': [
            'httpie_snapdsocket = httpie_snapdsocket:SnapdSocketTransportPlugin'
        ]
    },
    install_requires=[
        'httpie',
        'requests_unixsocket'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Environment :: Plugins',
        'License :: OSI Approved :: BSD License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Utilities'
    ],
)
