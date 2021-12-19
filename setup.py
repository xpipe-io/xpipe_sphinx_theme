from setuptools import setup

setup(
    name='xpipe_sphinx_theme',
    version='1.1.11',
    url='https://github.com/xpipe-io/xpipe_sphinx_theme',
    license='MIT',
    author='Christopher Schnick',
    author_email='crschnick@xpipe.io',
    description='Sphinx theme which is used for the XPipe docs website.',
    packages=['xpipe_sphinx_theme'],
    package_data={'xpipe_sphinx_theme': [
        'theme.conf',
        '*.html',
        'static/**/*'
    ]},
    install_requires=['sphinx >= 1.3.1']
)
