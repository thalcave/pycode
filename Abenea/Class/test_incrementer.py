class incrementer:
    def __init__(self, step=1):
        self.value = 0
        self.step = step

    def __call__(self):
        self.value += self.step
        return self.value

if __name__ == '__main__':


    a = incrementer()
    print a()
    print a()
    print a()

    b = incrementer(5)
    print b()
    print b()
    print b()

    
