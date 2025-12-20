import sys


print("=== Command Quest ===")
print("Program name:", sys.argv[0])
argc = len(sys.argv)
if argc == 1:
    print("No arguments provided!")
else:
    print("Arguments received:", argc - 1)
    i = 1
    while i < argc:
        print("Argument", i, ":", sys.argv[i])
        i += 1

print("Total arguments:", argc)
