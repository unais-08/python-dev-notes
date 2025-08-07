import numpy as np

# Useful NumPy Functions

import numpy as np

# 🎓 Exam scores from two different tests
test1_scores = np.array([75, 88, 92, 88, 67, 75, 91])
test2_scores = np.array([81, 79, 85, 90, 67, 75, 91])

# 1️⃣ Remove duplicates (e.g., same student got the same score multiple times)
unique_scores_test1 = np.unique(test1_scores)
print("Unique Test 1 Scores:", unique_scores_test1)

# 2️⃣ Sort the scores (e.g., leaderboard)
sorted_scores_test2 = np.sort(test2_scores)
print("Sorted Test 2 Scores:", sorted_scores_test2)

# 3️⃣ Combine both test scores (e.g., to calculate averages)
combined_scores = np.concatenate([test1_scores, test2_scores])
print("Combined Scores:", np.sort(combined_scores))

# 4️⃣ View combined scores in table form (2D) using stacking
# - Each row = a student
# - Column 0 = Test 1, Column 1 = Test 2
score_table = np.vstack((test1_scores, test2_scores)).T
print("\nStudent Score Table (Test1, Test2):\n", score_table)

# 5️⃣ Horizontally stack to see all test1 and test2 in the same row
side_by_side = np.hstack((test1_scores.reshape(1, -1), test2_scores.reshape(1, -1)))
print("\nSide-by-Side Test Scores (1 row):\n", side_by_side)
