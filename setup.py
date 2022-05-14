from setuptools import setup, find_packages

setup(
    name='pyqt-checkbox-file-list-widget',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt QListWidget for files and supporting the checkbox',
    url='https://github.com/yjg30737/pyqt-checkbox-file-list-widget.git',
    install_requires=[
        'PyQt5>=5.8',
        'pyqt-checkbox-list-widget>=0.0.1',
        'pyqt-file-list-widget>=0.0.1'
    ]
)