from distutils.core import setup

setup(
  name = 'SimpleNode',
  packages = ['SimpleNode'],
  version = '0.1',
  license='MIT',
  description = 'Package for working with Neural Networks for small projects',
  author = 'Artyom Yesayan',
  author_email = 'yesart8@gmail.com',
  url = 'https://github.com/user/reponame',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['NeuralNetwork', 'GradientDescent', 'AI'],
  install_requires=[            # I get to this in a second
          'validators',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.10',
  ],
)
