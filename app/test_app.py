# test_app.py
import pytest
import time
from app import App

def test_add(): 
    calc = App()
    time.sleep(1)  
    assert calc.add(2, 4) == 6

def test_add2(): 
    calc = App()
    time.sleep(1)  
    assert calc.add(3, 4) == 7
    
def test_long_running_one():
    # Simulating a long process
    print("Test 1 is running, simulating a long process...")
    time.sleep(1)  # Sleep for 120 seconds (2 minutes)
    assert True  # Simulating a successful test
