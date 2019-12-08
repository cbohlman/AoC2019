class test:
    def __init__(self):
        self.test = 1

    def run_test(self):
        x = self.test
        x = 2
        print(x)

test = test()
print(test.test)
test.run_test()
print(test.test)