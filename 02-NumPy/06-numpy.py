import numpy as np

# 🏫 NumPy: Boolean Masking/Filtering Example

# 🎓 Final exam scores of students in a class
scores = np.array([55, 72, 67, 49, 90, 85])

# ✅ Define passing criteria: students who scored 50 or above
passed_mask = scores >= 50  # Boolean mask: [True, True, True, False, True, True]

# 🧾 See which students passed (True) or failed (False)
print("Pass/Fail Mask:", passed_mask)

# 🟩 Filter scores to show only those who passed
passed_scores = scores[passed_mask]
print("Passed Scores:", passed_scores)

# ❌ Filter scores of students who failed
failed_scores = scores[~passed_mask]  # ~ inverts the boolean array
print("Failed Scores:", failed_scores)

# 📊 Count how many passed and failed
print("Number of Passed Students:", passed_mask.sum())  # sum of True values
print("Number of Failed Students:", (~passed_mask).sum())

students = np.array(["Ali", "Zara", "Rohan", "Sara", "John", "Fatima"])

# Print only names of students who passed
print("Passed Students:", students[passed_mask])
