import numpy as np

# Set a random seed for reproducibility
# This is a standard practice in data science to ensure that
# anyone running the same code gets the exact same "random" numbers.
np.random.seed(42)

# --- 1️⃣ Data Creation: Simulating Student Data ---
# Imagine this is a CSV file or database record we've loaded.
# We have a class of 10 students.
student_ids = np.arange(101, 111)
english_scores = np.random.randint(50, 100, size=10)  # Scores for English
math_scores = np.random.randint(40, 95, size=10)  # Scores for Math
science_scores = np.random.randint(60, 100, size=10)  # Scores for Science

print("Student IDs:", student_ids)
print("English Scores:", english_scores)
print("Math Scores:", math_scores)
print("Science Scores:", science_scores)

# --- 2️⃣ Data Aggregation: Combining Scores into a Single Dataset ---
# In a real-world scenario, you'd often combine different data points
# for a single entity (e.g., a student).
# We'll create a 2D array where each row is a student and each column is a subject.
# The 'T' (transpose) is used to switch rows and columns for a more intuitive layout.
all_scores = np.vstack([english_scores, math_scores, science_scores]).T

print("\n--- Combined Student Score Matrix ---")
# The final matrix represents:
# Rows: Students
# Columns: English, Math, Science
print(all_scores)

# --- 3️⃣ Data Exploration: Basic Statistics ---
# These are essential first steps in any data analysis task.
# We use the 'axis' parameter to perform calculations on a specific dimension.
# axis=0 means operate on each column (e.g., all English scores).
# axis=1 means operate on each row (e.g., one student's scores).
print("\n--- Performance Statistics ---")
print("Average score per subject (columns):", np.mean(all_scores, axis=0))
print("Highest score in each subject:", np.max(all_scores, axis=0))
print("Lowest score in each subject:", np.min(all_scores, axis=0))

# --- 4️⃣ Data Filtering: Identifying High Performers ---
# Boolean masking is a powerful tool for filtering data based on conditions.
# It's a cornerstone of data analysis in NumPy and Pandas.
passing_score = 70
high_performers_mask = all_scores[:, 0] > passing_score  # English score > 70
high_performers = all_scores[high_performers_mask]

print(f"\n--- Students with an English Score > {passing_score} ---")
# We're showing the full score record for these students.
print("Scores of high performers in English:\n", high_performers)

# We can find the IDs of these students too.
high_performer_ids = student_ids[high_performers_mask]
print("IDs of high performers:", high_performer_ids)

# --- 5️⃣ Data Transformation: Calculating Total Scores and Grades ---
# We can create new data from existing data, a common step in feature engineering.
# The `sum(axis=1)` calculates the total for each student (each row).
total_scores = np.sum(all_scores, axis=1)
print("\nTotal scores for each student:", total_scores)

# --- 6️⃣ Combining Arrays: Creating a Final Report ---
# We can use hstack to join different arrays side-by-side.
# The reshape(-1, 1) converts the 1D array into a 2D column vector,
# which is necessary for hstack to work correctly.
final_report = np.hstack(
    (student_ids.reshape(-1, 1), all_scores, total_scores.reshape(-1, 1))
)

print("\n--- Final Student Report (ID, English, Math, Science, Total) ---")
print(final_report)

# --- 7️⃣ Advanced Filtering: Identifying Students for Intervention ---
# We can combine multiple conditions using logical operators (`&` for AND, `|` for OR).
# Parentheses are crucial for correct operator precedence.
# We'll identify students who scored below 70 in both English and Math.
intervention_mask = (all_scores[:, 0] < 70) & (all_scores[:, 1] < 70)
students_for_intervention = student_ids[intervention_mask]

print("\n--- Students Needing Intervention ---")
print("Students who scored < 70 in both English and Math:", students_for_intervention)

# --- 8️⃣ Final Summary and Analysis ---
print("\n--- Final Class Summary ---")
print(f"Average English Score: {np.mean(english_scores):.2f}")
print(f"Highest Score in Class (any subject): {np.max(all_scores)}")
print(
    f"Student with highest total score is student ID {student_ids[np.argmax(total_scores)]}"
)

# argmax() gives the index of the highest value. We use this index
# to find the corresponding student ID.
# This is a very common and powerful pattern in data analysis.
