from distutils.core import setup

setup(
  name = 'inform_me',
  packages = ['inform_me'],   
  version = '0.1.2',
  license='MIT',
  description = 'The aim of this library is to automatically notify the developer as soon as a time-consuming program execution gets completed.',
  author = 'Mohak Narang',
  author_email = 'mohak.nar@gmail.com',
  url = 'https://github.com/mohak1/inform_me',
  download_url = 'https://github.com/mohak1/inform_me/blob/master/dist/inform_me-0.1.1.tar.gz',
  keywords = ['Sound Alert', 'Notification', 'Timer', 'Code Execution Completion Alert', 'Popup Message'],
  install_requires=[''],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)
