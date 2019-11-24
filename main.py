import stack, memory
from guizero import App, TextBox, PushButton, Text

stack_cpu = stack.Stack(32)
cpu_memory = memory.Memory(64)

def do_nothing():
    pass

def setup():
    app = App(title="Stack Machine")
    address_label = Text(app, text="Address:")
    address_value = TextBox(app)

    data_label = Text(app, text="Data:")
    data_value = TextBox(app)

    load_button = PushButton(app, text="Load", command=do_nothing)
    save_button = PushButton(app, text="Save", command=do_nothing)
    run_button = PushButton(app, text="Run", command=do_nothing)

    app.display()

def main():
    pass

if __name__ == "__main__":
    setup()
    main()