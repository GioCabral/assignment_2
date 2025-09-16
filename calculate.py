#!/usr/bin/env python3

import math
import os
from datetime import datetime

query_string = os.environ.get('QUERY_STRING', '')
params = {}
if query_string:
    try:
        params = dict(qc.split("=") for qc in query_string.split("&"))
    except ValueError:
        params = {}

try:
    a = float(params.get('a', '1.0'))
    b = float(params.get('b', '0.0'))
    c = float(params.get('c', '0.0'))
except (ValueError, TypeError):
    a, b, c = 1.0, 0.0, 0.0

if a == 0:
    a = 1.0

c_cubed = c ** 3
try:
    sqrt_c_cubed = math.sqrt(c_cubed)
except ValueError:
    sqrt_c_cubed = 0.0

division_result = sqrt_c_cubed / a
multiplication_result = division_result * 10
final_result = multiplication_result + b

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print("-----------------------------------------------------------------------<br>")
print(f"Giovanni Luca Cabral<br>")
print(f"Final Result: {final_result:.1f}<br>")
print(f"Step 1: c = {c:.1f} , c³ = {c_cubed:.1f}<br>")
print(f"Step 2: √(c³) = {sqrt_c_cubed:.1f}<br>")
print(f"Step 3: {sqrt_c_cubed:.1f} / {a:.1f} = {division_result:.1f}<br>")
print(f"Step 4: {division_result:.1f} * 10 = {multiplication_result:.1f}<br>")
print(f"Step 5: {multiplication_result:.1f} + {b:.1f} = {final_result:.1f}<br>")
print(f"<br>Calculation completed at {current_time}<br>")
print("-----------------------------------------------------------------------<br>")
