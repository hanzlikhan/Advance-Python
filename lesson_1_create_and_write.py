# =====================================================================
# LESSON 1: HOW TO CREATE AND WRITE TO A FILE
# Level: Grade 5 friendly!
# =====================================================================

# Think of a file like a brand new notebook:
# 1. You open the notebook.
# 2. You take a pen and write your message.
# 3. You close the notebook and put the cap back on your pen!

print("==================================================")
print("Welcome to Lesson 1: Creating and Writing a File!")
print("==================================================")

# -------------------------------------------------------------
# STEP 1: OPEN (OR CREATE) THE FILE
# -------------------------------------------------------------
# The open() function takes two main things inside the brackets:
#   1. The filename: "my_first_file.txt"
#   2. The mode: "w" stands for "WRITE" mode.
#
# IMPORTANT RULE FOR "w" MODE:
# - If the file does NOT exist, Python creates it for you!
# - If the file already exists, "w" erases it clean so you can start fresh.
my_notebook = open("my_second_file.txt", "w")

print("[Step 1] Notebook opened and ready!")

# -------------------------------------------------------------
# STEP 2: WRITE SOMETHING INTO THE FILE
# -------------------------------------------------------------
# We use the .write() command to write words on the page.
# Note: "\n" means "hit Enter" to jump down to a new line!
my_notebook.write("Hello! This is my second computer file.\n")
my_notebook.write("I am learning Python file handling!\n")
my_notebook.write("Python is super fun and easy to learn.\n")

print("[Step 2] Message written inside the file!")

# -------------------------------------------------------------
# STEP 3: CLOSE THE FILE
# -------------------------------------------------------------
# Always close your file when you are finished!
# Why? Because closing saves all your changes safely to the computer's storage.
# It is just like closing your school bag so your books don't fall out.
my_notebook.close()

print("[Step 3] Notebook closed safely!")
print("\nGreat job! Look at the left side of your screen in VS Code.")
print("You will see a new file called 'my_first_file.txt' has appeared!")
