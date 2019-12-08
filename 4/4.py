def test_one(i):
    word = str(i)
    word_set = set(word)
    for a in word_set:
        if word.count(a) == 2:
            return True
    return False

def test_two(i):
    word = str(i)
    for a in range(0,len(word) - 1):
        x = int(word[a])
        y = int(word[a+1])
        if y < x :
            return False
    return True 

def test_input(i):
    return test_one(i) and test_two(i)

if __name__ == "__main__":
    min = 284639
    max = 748759
    count = 0
    for i in range(min,max):
        if test_input(i):
            count += 1
            print(i)


    print(count)
