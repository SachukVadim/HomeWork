import  random
with open("randomNumber", "w") as f:
    for _ in range(0,10000):
        number = random.randint(1,10)
        f.write(str(number) + "\n")

with open("randomNumber", "r") as f:
    count = sum(int(line) for line in f)
    print(f"Sum of all numbers in the file: {count}")
