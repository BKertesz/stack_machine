import stack

stack_cpu = stack.Stack(15)
stack_cpu.queue("A")
stack_cpu.queue("B")
stack_cpu.queue("C")
stack_cpu.queue("D")
last = stack_cpu.dequeue()
print(stack_cpu.size())
print(stack_cpu.stack)
print(last)

def setup():
    pass

def main():
    pass

if __name__ == "__main__":
    main()