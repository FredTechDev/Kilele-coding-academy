"""
=============================================================================
Kilele Python Learning Pack — Core Concepts
File: lists.py
Description: Ordered, mutable collections of items and list operations
=============================================================================

Learning Objectives:
1. Understand lists as ordered, mutable containers.
2. Access and modify elements using indexing and slicing.
3. Master list modification methods: .append(), .insert(), .pop(), .remove().
4. Use built-in functions: len(), min(), max(), sum(), sorted().
5. Iterate through lists with indexes using enumerate().
"""

print("==================================================")
print("              LESSON 11: LISTS                    ")
print("==================================================")

# ==========================================
# 1. CREATING AND ACCESSING LISTS
# ==========================================
# Lists are created with square brackets [].
# They can hold any data type, and items can be repeated.
languages = ["Python", "JavaScript", "C++", "Rust"]

print("\n--- 1. List Indexing ---")
print("Full list:    ", languages)
print("First item [0]:", languages[0])
print("Last item [-1]:", languages[-1])
print("List length:  ", len(languages))


# ==========================================
# 2. LISTS ARE MUTABLE (CAN BE MODIFIED)
# ==========================================
print("\n--- 2. Modifying Lists ---")
# Changing an existing item:
languages[1] = "TypeScript"
print("After replacing index 1:", languages)

# Adding items to the end (.append()):
languages.append("Go")
print("After .append('Go'):    ", languages)

# Inserting at a specific index (.insert()):
languages.insert(1, "HTML/CSS")
print("After .insert(1, ...):  ", languages)

# Removing an item by value (.remove()):
languages.remove("C++")
print("After .remove('C++'):   ", languages)

# Popping the last item off (.pop()):
removed_item = languages.pop()
print(f"After .pop() (removed '{removed_item}'):", languages)


# ==========================================
# 3. LIST MATHEMATICS & UTILITIES
# ==========================================
print("\n--- 3. Numerical Operations on Lists ---")
test_marks = [78, 92, 85, 64, 99, 88]

print("Scores:       ", test_marks)
print("Lowest score: ", min(test_marks))
print("Highest score:", max(test_marks))
print("Total sum:    ", sum(test_marks))
print(f"Class average: {sum(test_marks) / len(test_marks):.1f}")

# Sorting:
sorted_copy = sorted(test_marks)  # Leaves original unchanged
print("Sorted copy:  ", sorted_copy)


# ==========================================
# 4. ITERATING WITH enumerate()
# ==========================================
# enumerate() gives you both the index (position) and the value!
print("\n--- 4. Looping with enumerate() ---")
podium = ["Lightning", "Thunder", "Shadow"]

for rank, horse in enumerate(podium, start=1):
    print(f"Rank #{rank}: {horse}")


# ==========================================
# 5. MEMBERSHIP CHECK (in)
# ==========================================
print("\n--- 5. Checking Membership ---")
search_term = "Python"
if search_term in languages:
    print(f"Yes! '{search_term}' is currently in our curriculum.")
else:
    print(f"'{search_term}' is not found.")
