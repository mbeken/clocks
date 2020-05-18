
# coding: utf-8

# In[16]:

from  app import func1
def test_1():
    """
        Testing at 3 hrs 0 mins - Angle = 90
        """
    hour = 3
    minute = 0
    angle1 = func1(hour,minute)
    try:
        angle1 = float(angle1.split(':')[1])
    except:
        None
    assert angle1 == 90.0
def test_2():
    """
        Testing at 12 hrs 50 mins - Angle = 85
        """
    hour = 12
    minute = 50
    angle1 = func1(hour,minute)
    try:
        angle1 = float(angle1.split(':')[1])
    except:
        None
    assert angle1 == 85.0
def test_3():
    """
        Testing at 23 hrs 50 mins - Angle = "Enter correct integer value(Hour=1 to 12, Minute=0 to 60)"
        """
    hour = 23
    minute = 50
    angle1 = func1(hour,minute)
    try:
        angle1 = float(angle1.split(':')[1])
    except:
        None
    assert angle1 == "Enter correct integer value(Hour=1 to 12, Minute=0 to 60)"
def test_4():
    """
        Testing at empty string - Angle = "Enter correct integer value(Hour=1 to 12, Minute=0 to 60)"
        """
    hour = ""
    minute = ""
    angle1 = func1(hour,minute)
    try:
        angle1 = float(angle1.split(':')[1])
    except:
        None
    assert angle1 == "Enter correct integer value(Hour=1 to 12, Minute=0 to 60)"
