word="python"
i=0
print("character present at even index:")
while i<len(word):
    print(word[i])
    i=i+2
else:
    print("character prsent at odd index")
    i=1
    while i<len(word):
        print(word[i])
        i=i+2