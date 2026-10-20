# =====================================================================
# LESSON 5: MINI PROJECT - "MY SECRET DIARY"
# Level: Grade 5 friendly!
# =====================================================================

# Now you know all 4 key skills:
# 1. Create a file
# 2. Write to a file
# 3. Read from a file
# 4. Close a file (or use 'with open')
#
# Let's put everything together into a fun interactive diary!

print("==================================================")
print("          WELCOME TO YOUR SECRET DIARY            ")
print("==================================================")

# 1. Ask the user for their name and secret thought
user_name = input("What is your name? ")
todays_date = input("What is today's date or day? (e.g., Monday): ")
secret_entry = input("Write a secret note or your goal for today:\n> ")

# 2. Open the diary in "a" (append) mode so old secrets are never lost!
# We use the superpower 'with open' so it closes automatically!
with open("my_secret_diary.txt", "a") as diary:
    diary.write(f"\n--- Entry by {user_name} on {todays_date} ---\n")
    diary.write(f"Note: {secret_entry}\n")
    diary.write("-" * 40 + "\n")

print("\n[Success] Your secret entry has been saved to 'my_secret_diary.txt'!\n")

# 3. Ask if they want to read the entire diary
see_diary = input("Would you like to read all entries in your diary right now? (yes/no): ")

if see_diary.lower() == "yes" or see_diary.lower() == "y":
    print("\n" + "="*50)
    print("READING YOUR SECRET DIARY:")
    print("="*50)
    
    with open("my_secret_diary.txt", "r") as diary:
        all_secrets = diary.read()
        print(all_secrets, end="")
        
    print("="*50)
    print("End of Diary!")
else:
    print("Understood! Your secrets are safe. Run this program anytime to add more!")
