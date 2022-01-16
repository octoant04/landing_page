#coding= ANSI

import unittest
import sys, urllib
from selenium import webdriver
import subprocess
import sys
import os.path

ROOT = 'http://localhost:8000'
path = "C:/Users/Mememe/Desktop/web-page/landing_page/web2py/web2py_no_console.exe"

class FunctionalTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.web2py = start_web2py_server()
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(1)

    @classmethod    
    def tearDownClass(self):
        self.browser.close()
        self.web2py.kill()

    def get_response_code(self, url):
        """Returns the response code of the given url

        url     the url to check for 
        return  the response code of the given url
        """
        handler = urllib.urlopen(url)
        return handler.getcode()


def start_web2py_server():
    #noreload ensures single process
    print (os.path.curdir)  
    return subprocess.Popen([
             path, "runserver", '-a "passwd"', '-p 8001'
    ])

    #unit test

def run_functional_tests(pattern=None):
    print ('running tests')
    if pattern is None:
        tests = unittest.defaultTestLoader.discover('.')
    else:
        pattern_with_globs = '*%s*' % (pattern,)
        tests = unittest.defaultTestLoader.discover('test_package', pattern=pattern_with_globs)

    runner = unittest.TextTestRunner()
    runner.run(tests)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        run_functional_tests()
    else:
        run_functional_tests(pattern=sys.argv[1])