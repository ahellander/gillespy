from setuptools import setup

setup(name = "gillespy",
      version = "1.0.1",
      packages = ['gillespy'],
      description = 'Python interface to the Gillespie StochKit2 solvers',
      
      install_requires = ["numpy",
                          "matplotlib",
                          "scipy"],
      
      author = "John H. Abel, Brian Drawert, Andreas Hellander",
      author_email = ["jhabel01@gmail.com", "briandrawert@gmail.com", "andreas.hellander@gmail.com"],
      license = "GPL",
      keywords = "gillespy, gillespie algorithm, stochkit, stochastic simulation"

      #url = "http://www.pyurdme.org", # we don't yet have one

      #download_url = "https://github.com/pyurdme/pyurdme/tarball/master/v1.0.1"
      
      )
