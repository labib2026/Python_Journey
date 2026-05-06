# --- Task 1: List Input (ভিডিও ৩০ এর সহজ ভার্সন) ---
# কতগুলো ইনপুট নিবে তা আগে ঠিক করা
n = int(input("How many subjects? : "))
subjects = []

for i in range(n):
    # বারবার ইনপুট নিয়ে লিস্টে ভরা
    val = input(f"Enter subject {i+1}: ")
    subjects.append(val)

print("Your Subject List:", subjects)


# --- Task 2: Matrix (ভিডিও ৩১ এর সহজ ভার্সন) ---
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

print("\nPrinting Matrix:")
for row in matrix:
    for col in row:
        print(col, end=" ") # end=" " দিলে সংখ্যাগুলো পাশাপাশি বসে
    print() # এক সারি শেষ হলে নতুন লাইনে যাবে


# --- Task 3: JP Dictionary (ভিডিও ৩২ এর সহজ ভার্সন) ---
jp_dict = {
    "neko": "Cat",
    "inu": "Dog",
    "gakusei": "Student"
}

word = input("\nEnter JP word: ").lower() # lower() দিলে ছোট হাতের বড় হাতের ঝামেলা হবে না

# .get() ব্যবহার করলে এরর আসে না, সুন্দর মেসেজ দেয়
result = jp_dict.get(word, "Word not found in N5 database")
print("Meaning:", result)
