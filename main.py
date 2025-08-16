Reset = '\033[0m'
Red = '\033[31m'

count = 0

Stringer = input("Enter your essay/paragraph/sentence you want to check the word count for: ")

Stringer = Stringer.split()

count = len(Stringer)

print(f"The word count for your string is {Red} {count} {Reset}")