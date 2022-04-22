def merge(a, b):
    sorted = []
    prev_s = None
    for f, s in zip(a.copy(), b.copy()):
        if (f == prev_s):
            sorted.append(prev_s)
            b.pop(0)
        if (f < s):
            sorted.append(f)
            a.pop(0)  
        prev_s = s
        
    if not a:
        [sorted.append(e) for e in b]
    if not b:
        [sorted.append(e) for e in a]
        
    return sorted


if __name__ == '__main__':
    print(merge([1,2,3], [2,5,5]))