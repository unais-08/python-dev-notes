# --- dictionary in Python--> Treat something like objects in JavaScript---
# 📘 Creating a dictionary

person = {"name": "Alice", "age": 30, "city": "New York"}
print("📌 Initial dictionary:", person)

# 🔍 Accessing values
print("👤 Name:", person["name"])

# ➕ Adding a new key-value pair
person["email"] = "alice@example.com"
print("📬 After adding email:", person)

# 🔁 Updating a value
person["age"] = 31
print("🎂 After updating age:", person)

# 🔁 Updating using update()
person.update({"email": "dummy@gmail.com"})
print("✏️ After updating email with update():", person)

# ❌ Removing a key-value pair
del person["city"]
print("🗑️ After removing city:", person)

# 📋 Copying the dictionary
person_copy = person.copy()
print("📄 Copied dictionary:", person_copy)

# 🗝️ Getting all keys
keys = list(person.keys())
print("🔑 All keys:", keys)

# 📦 Getting all values
values = list(person.values())
print("📦 All values:", values)

# 🔢 Getting number of items
print("🔢 Number of items:", len(person))

# 🔁 Iterating over keys
print("🔁 Keys:")
for key in person:
    print("  -", key)

# 🔁 Iterating over values
print("🔁 Values:")
for value in person.values():
    print("  -", value)

# 🔁 Iterating over key-value pairs
print("🔁 Key-Value pairs:")
for key, value in person.items():
    print(f"  - {key}: {value}")

# ✅ Checking if a key exists
if "email" in person:
    print("✅ Email exists:", person["email"])

# ❓ Getting a value with a default
phone = person.get("phone", "Not available")
print("📞 Phone:", phone)


print(person.items())
