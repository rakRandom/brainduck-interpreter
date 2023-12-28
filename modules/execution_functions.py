class BrainDuckInterpreter:
    def __init__(self): ...
    def run(self, code, debug=False): ...
    def memory_usage(self): ...


def execute_shell(interpreter: BrainDuckInterpreter):
    code: list[str] | str = list()
    user_input: str

    print("Brainfuck interpreter")

    while True:
        user_input = input("> ")
        if user_input != "":
            code.append(user_input)
        else:
            break

    code = [cmd for cmd in "".join(code) if cmd in "><+-[],."]
    interpreter.run(code)


def execute_external_code(interpreter: BrainDuckInterpreter, path: str):
    with open(path, "r") as code:
        code = [cmd for cmd in code.read() if cmd in "><+-[],."]

    interpreter.run(code, debug=False)
    print(f"\nMemory used: {interpreter.memory_usage()} bytes")
