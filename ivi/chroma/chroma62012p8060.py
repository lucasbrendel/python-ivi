"""

Python Interchangeable Virtual Instrument Library

Copyright (c) 2013-2017 Alex Forencich

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

from chroma62000p import *


class chroma62012p8060(chroma62000p):
    "Chroma ATE 62012P-80-60 series IVI DC power supply driver"

    def __init__(self, *args, **kwargs):
        self.__dict__.setdefault("_instrument_id", "62012P-80-60")

        super(chroma62012p8060, self).__init__(*args, **kwargs)

        self._output_count = 1

        self._output_spec = [
            {
                "range": {"P80V": (80.0, 60.0)},
                "ovp_max": 88.0,  # 1.1 x max voltage
                "ocp_max": 63.0,  # 1.05 x max current
                "voltage_max": 80.0,
                "current_max": 60.0,
            }
        ]
