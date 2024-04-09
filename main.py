# Get the file path of a class in Python

from another import Employee

import inspect
import os


# ✅ get the absolute file path of class

# 👇️ /home/borislav/Desktop/bobbyhadz_python/another.py
print(inspect.getfile(Employee))

emp1 = Employee()

# 👇️ /home/borislav/Desktop/bobbyhadz_python/another.py
print(inspect.getfile(emp1.__class__))

# -----------------------------------------------

# ✅ get the relative file path of class

# 👇️ another.py
print(os.path.relpath(inspect.getfile(Employee)))