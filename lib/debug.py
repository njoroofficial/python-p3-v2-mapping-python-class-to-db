#!/usr/bin/env python3
#lib/testing/debug.py

from __init__ import CONN, CURSOR
from department import Department

import ipdb

Department.drop_table()
Department.create_table()

payroll = Department("Payroll", "Building A, 5th Floor")
print(payroll)

payroll.save()  # Persist to db, assign object id attribute
print(payroll)

hr = Department("Human Resources", "Building C, East Wing")
print(hr)  

hr.save()  # Persist to db, assign object id attribute
print(hr)

ipdb.set_trace()
