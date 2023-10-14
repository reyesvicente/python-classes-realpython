class SampleClass:
    class_attr = 100

    def __init__(self, instance_attr) -> None:
        self.instance_attr = instance_attr

    def method(self):
        print(f"Class attribute: {self.class_attr}")
        print(f"Instance attribute: {self.instance_attr}")
