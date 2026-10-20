# =====================================================================
# LESSON 4: THE SUPERPOWER WAY -> THE "with" STATEMENT!
# Level: Grade 5 friendly!
# =====================================================================

# QUESTION: What happens if you forget to write .close()?
# Your computer might keep the file locked or lose your changes!
#
# PYTHON'S SUPERPOWER: The "with" statement!
# Think of "with" like an automatic sliding door in a superhero base:
# - When you walk inside (indented lines), the door is open.
# - When you step outside (back to the left margin), the door closes AUTOMATICALLY!
# - You NEVER have to remember .close() ever again!

print("==================================================")
print("Welcome to Lesson 4: The 'with' Statement!")
print("==================================================")

# -------------------------------------------------------------
# EXAMPLE 1: WRITING WITH "with"
# -------------------------------------------------------------
print("\n--- Example 1: Creating a superhero file ---")

# Notice the syntax: with open(...) as variable_name:
with open("superhero_team.txt", "w") as my_file:
    # Everything inside this indented block is working with the file:
    my_file.write("Member 1: Iron Man\n")
    my_file.write("Member 2: Spider-Man\n")
    my_file.write("Member 3: Batman\n")
    print("  -> Inside the block: Writing heroes to the file...")

# As soon as we un-indent (go back to the left), Python ALREADY closed the file!
print("  -> Outside the block: File is automatically closed! No .close() needed!")


# -------------------------------------------------------------
# EXAMPLE 2: READING WITH "with"
# -------------------------------------------------------------
print("\n--- Example 2: Reading the superhero file ---")

with open("superhero_team.txt", "r") as my_file:
    heroes = my_file.read()
    print("  -> Inside the block: Reading heroes...")

# The file is closed automatically here too!
print("\n" + "="*50)
print("OUR SUPERHERO SQUAD:")
print("="*50)
print(heroes, end="")
print("="*50)

print("PRO TIP: Almost all professional Python coders use 'with open'!")
