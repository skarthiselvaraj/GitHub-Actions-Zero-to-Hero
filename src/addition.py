# app.py
# This is a test commit
#this is a second test commit
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0

#Substract value
def subtract(a, b):
    return a - b
    
def test_subtract():
    assert subtract(5, 99) == -94  # Corrected expected value
    assert subtract(99, 6) == 93   # Corrected expected value
