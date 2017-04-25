#!/usr/bin/env python3

"""
.___  ___.      ___   .___________.  ______  __    __   _______     _______.
|   \/   |     /   \  |           | /      ||  |  |  | |   ____|   /       |
|  \  /  |    /  ^  \ `---|  |----`|  ,----'|  |__|  | |  |__     |   (----`
|  |\/|  |   /  /_\  \    |  |     |  |     |   __   | |   __|     \   \    
|  |  |  |  /  _____  \   |  |     |  `----.|  |  |  | |  |____.----)   |   
|__|  |__| /__/     \__\  |__|      \______||__|  |__| |_______|_______/    

"""

"""
MIT License

Copyright (c) 2017 Pablo Rivera

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

def matches(options, key, default=None):
    """
    Match a key with a dictionary key
    and return the dictionary value.
    Allows to pass custom default parameter
    to avoid returning None types.

    :param options: dictionary of possible key, values
    :param key: key that will tried to be matched with a options key
    :returns value: value that corresponds to given key or default if no matche
    """
    return options.get(key, default)
