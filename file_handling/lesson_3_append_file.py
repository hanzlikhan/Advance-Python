# =====================================================================
# LESSON 3: HOW TO ADD MORE TEXT (APPEND MODE "a")
# Level: Grade 5 friendly!
# =====================================================================

# What is the difference between "w" (Write) and "a" (Append)?
#
# [!] "w" (Write):
#     Imagine drawing on a whiteboard and erasing everything before drawing again!
#     If you open with "w", your old notes will be deleted!
#
# [*] "a" (Append):
#     Imagine adding a new sticker or writing a new sentence at the BOTTOM of your page!
#     Your old words stay safe, and the new words get added at the end.

print("==================================================")
print("Welcome to Lesson 3: Adding Text (Append Mode)")
print("==================================================")

# -------------------------------------------------------------
# STEP 1: OPEN IN APPEND MODE ("a")
# -------------------------------------------------------------
my_notebook = open("my_second_file.txt", "a")
print("[Step 1] File opened in APPEND ('a') mode!")

# -------------------------------------------------------------
# STEP 2: WRITE NEW EXTRA LINES
# -------------------------------------------------------------
# Notice: \n ensures text goes onto a new line!
my_notebook.write("Line added in Lesson 3: I like playing games and coding.\n")
my_notebook.write("Line added in Lesson 3: Appending is super useful!\n")
print("[Step 2] New lines attached to the bottom!")

# -------------------------------------------------------------
# STEP 3: CLOSE THE FILE
# -------------------------------------------------------------
my_notebook.close()
print("[Step 3] File saved and closed!")

# -------------------------------------------------------------
# STEP 4: LET'S READ IT TO VERIFY!
# -------------------------------------------------------------
print("\nNow let's open and check the file to see the old + new lines:")

read_file = open("my_first_file.txt", "r")
all_text = read_file.read()
read_file.close()

print("\n" + "="*50)
print(all_text, end="")
print("="*50)
print("Notice that your old lines from Lesson 1 are STILL there!")
