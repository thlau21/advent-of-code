#Day 1 part 1
with open('puzzle.txt','r') as f:
    lines = f.readlines()
    lines = [int(i) for i in lines]
    bigger = 0
    threshold = lines[0]
    for x in lines[1:]:
        if x > threshold:
            bigger += 1
        threshold = x
    print(bigger)

#Day 1 part 2
    windowSize = 3
    window = [
        sum(lines[j : j + windowSize]) 
        for j in range(len(lines) - windowSize + 1)
    ]
    threshold = window[0]
    bigger = 0
    for i in window[1:]:
        if i > threshold:
            bigger+=1
        threshold = i
    print(bigger)

