class SampleClass:
    def __init__(self, value):
        self.__value = value

    def __method(self):
        print(self.__value)

>>> sample_instance = SampleClass("Hello!")
>>> vars(sample_instance)
{'_SampleClass__value': 'Hello!'}

>>> vars(SampleClass)
mappingproxy({
    ...
    '__init__': <function SampleClass.__init__ at 0x105dfd4e0>,
    '_SampleClass__method': <function SampleClass.__method at 0x105dfd760>,
    '__dict__': <attribute '__dict__' of 'SampleClass' objects>,
    ...
})

>>> sample_instance = SampleClass("Hello!")
>>> sample_instance.__value
Traceback (most recent call last):
    ...
AttributeError: 'SampleClass' object has no attribute '__value'

>>> sample_instance.__method()
Traceback (most recent call last):
    ...
AttributeError: 'SampleClass' object has no attribute '__method'

>>> sample_instance._SampleClass__value
'Hello!'

>>> sample_instance._SampleClass__method()
Hello!