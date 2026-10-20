# =====================================================================
# LESSON 2: HOW TO READ A FILE
# Level: Grade 5 friendly!
# =====================================================================

# Think of reading a file like opening your favorite storybook:
# 1. You open the book in READ mode ("r").
# 2. You read the words with your eyes (.read()).
# 3. You close the book when you are done (.close()).

# print("==================================================")
# print("Welcome to Lesson 2: Reading a File!")
# print("==================================================")

# -------------------------------------------------------------
# STEP 1: OPEN THE FILE IN READ MODE
# -------------------------------------------------------------
# We pass "r" which stands for "READ".
#
# IMPORTANT RULE FOR "r" MODE:
# The file MUST already exist!
# If you try to read a file that does not exist, Python will show an error.
# (Make sure you ran lesson_1 first so 'my_first_file.txt' exists!)
my_notebook = open("my_second_file.txt", "r")

# print("[Step 1] File opened in READ mode!")

# -------------------------------------------------------------
# STEP 2: READ THE CONTENTS
# -------------------------------------------------------------
# We use .read() to pull all the words out of the file and save
# them into a Python variable called 'file_contents'.
file_contents = my_notebook.read()

# print("[Step 2] Read all the text into memory!")

# -------------------------------------------------------------
# STEP 3: CLOSE THE FILE
# -------------------------------------------------------------
# Always close the file once you have finished reading it.
my_notebook.close()

# print("[Step 3] File closed safely!")

# -------------------------------------------------------------
# STEP 4: SHOW THE WORDS ON SCREEN!
# -------------------------------------------------------------
# Now we use print() so you can see what was inside the file!
# print("\n" + "="*50)
# print("HERE IS WHAT WAS INSIDE YOUR FILE:")
# print("="*50)
print(file_contents, end="")
# print("="*50)
# print("High five! You just read a file with Python!")
