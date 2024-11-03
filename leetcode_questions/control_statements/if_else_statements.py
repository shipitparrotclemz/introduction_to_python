"""
Given a blood pressure variable, set answer: str to be equal to the following:

1. blood_pressure: int = 80

If blood pressure is below 120, set answer to "Normal"

If blood_pressure is more or equal to 120, set answer = "High Blood Pressure"

If blood pressure is more or equal to 140, set answer to "Very High Blood Pressure"

If blood pressure is more or equal to 160, set answer to "Can someone please call an ambulance"
"""

blood_pressure: int = 80

# Test Case 1: 80 -> "Normal"
# Test Case 2: 119 -> "Normal"
# Test Case 3: 125 -> "High Blood Pressure"
# Test Case 4: 145 -> "Very High Blood Pressure"
# Test Case 5: 165 -> "Can someone please call an ambulance"
