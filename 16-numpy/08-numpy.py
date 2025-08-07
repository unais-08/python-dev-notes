import numpy as np

# 🎲 Ensure reproducibility (important for testing or tutorials)
np.random.seed(42)

# 1️⃣ Generate random exam scores for 100 students between 0 and 100
scores = np.random.randint(0, 101, size=100)  # inclusive of 0, exclusive of 101
print("Sample Scores:", scores[:10])  # show first 10

# 2️⃣ Simulate pass/fail: pass if score >= 50
pass_mask = scores >= 50
print("Number of Students Passed:", pass_mask.sum())
print("Number of Students Failed:", (~pass_mask).sum())

# 3️⃣ Shuffle the scores (to simulate random order)
np.random.shuffle(scores)
print("Shuffled Scores:", scores[:10])

# 4️⃣ Generate normal-distributed scores (mean=70, std=10) — more realistic than uniform
normal_scores = np.random.normal(loc=70, scale=10, size=100)
print("\nNormal Distributed Scores (first 5):", normal_scores[:5])

rounded_scores = np.round(normal_scores).astype(int)
print("Rounded Normal Scores (first 5):", rounded_scores[:5])


# 5️⃣ Choose random students for bonus (e.g., 5 lucky winners)
student_ids = np.arange(1, 101)  # student IDs 1 to 100
bonus_winners = np.random.choice(student_ids, size=5, replace=False)
print("🎁 Bonus Winners (IDs):", bonus_winners)
