import sys

shift = int(sys.argv[1])%26

text = sys.stdin.read().upper()

result=""

for ch in text:
    if 'A' <= ch <= 'Z':
        result += chr((ord(ch) - ord('A') + shift) % 26 +ord('A'))

count = 0
blocks = 0

for ch in result:
    print(ch, end = "")
    count += 1

    if count ==5:
        print(" ", end="")
        count = 0
        blocks += 1

    if blocks == 10:
        print()
        blocks = 0

print()
