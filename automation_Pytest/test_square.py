import math

# In Selenium, Asserts are validations or checkpoints for an application
# Asserts in Selenium validate the automated test cases that help testers understand,
# if tests have passed or failed.

def test_sqrt():
   num = 25
   assert math.sqrt(num) == 5

def testsquare():
   num = 7
   assert 7*7 == 40

def testequality():
   assert 10 == 11