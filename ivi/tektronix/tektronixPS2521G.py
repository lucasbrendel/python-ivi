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

from tektronixPS2520G import *


class tektronixPS2521G(tektronixPS2520G):
    "Tektronix PS2521G DC power supply driver"

    def __init__(self, *args, **kwargs):
        self.__dict__.setdefault("_instrument_id", "PS2521G")

        super(tektronixPS2521G, self).__init__(*args, **kwargs)

        self._output_count = 3

        self._output_spec = [
            {
                "range": {"P20V": (21.0, 2.5)},
                "ovp_max": 22.5,
                "voltage_max": 21.0,
                "current_max": 2.5,
            },
            {
                "range": {"P20V": (21.0, 2.5)},
                "ovp_max": 22.5,
                "voltage_max": 21.0,
                "current_max": 2.5,
            },
            {
                "range": {"P6V": (6.5, 5.0)},
                "ovp_max": 7.0,
                "voltage_max": 6.5,
                "current_max": 5.0,
            },
        ]

        self._init_outputs()
