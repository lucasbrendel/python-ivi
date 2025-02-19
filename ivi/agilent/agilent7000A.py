"""

Python Interchangeable Virtual Instrument Library

Copyright (c) 2012-2017 Alex Forencich

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

"""

from agilent7000 import *


class agilent7000A(agilent7000):
    "Agilent InfiniiVision 7000A series IVI oscilloscope driver"

    def __init__(self, *args, **kwargs):
        self.__dict__.setdefault("_instrument_id", "")

        super(agilent7000A, self).__init__(*args, **kwargs)

        self._identity_description = (
            "Agilent InfiniiVision 7000A series IVI oscilloscope driver"
        )
        self._identity_supported_instrument_models = [
            "DSO7012A",
            "DSO7014A",
            "DSO7032A",
            "DSO7034A",
            "DSO7052A",
            "DSO7054A",
            "DSO7104A",
            "MSO7012A",
            "MSO7014A",
            "MSO7032A",
            "MSO7034A",
            "MSO7052A",
            "MSO7054A",
            "MSO7104A",
        ]
