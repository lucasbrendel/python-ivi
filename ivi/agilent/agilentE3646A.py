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

from agilentE3600A import *


class agilentE3646A(agilentE3600A):
    "Agilent E3646A IVI DC power supply driver"

    def __init__(self, *args, **kwargs):
        self.__dict__.setdefault("_instrument_id", "E3646A")

        super(agilentE3646A, self).__init__(*args, **kwargs)

        self._output_count = 2

        self._output_spec = [
            {
                "range": {"P8V": (8.24, 3.09), "P20V": (20.6, 1.545)},
                "ovp_max": 22.0,
                "voltage_max": 8.24,
                "current_max": 3.09,
            },
            {
                "range": {"P8V": (8.24, 3.09), "P20V": (20.6, 1.545)},
                "ovp_max": 22.0,
                "voltage_max": 8.24,
                "current_max": 3.09,
            },
        ]

        self._memory_size = 5

        self._init_outputs()
