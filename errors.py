class IndexOutOfList(Exception):
    def __init__(self, input: int, lenght: int):
        self.message = f"The length of the list is {lenght} but the entered value is {input}."
        super().__init__(self.message)