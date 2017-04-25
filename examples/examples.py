#!/usr/bin/env Python3

import matches

"""
These are some simple examples
that show the naming conventions
for the library.

Note that the function name follows
the convention of:

match_value_with(key)

This allows the programmer to
understand what is being matched by reading
the function name and the first parameter.

For example:

match_size_with(shirt)
match_tires_with(car)
match_tax_with(income)
"""

def match_login_url_with(username, default="https://foo.bar/login"):
    """
    Match a given username with the corresponding
    login URL

    :param username: username of user. type str
    :returns URL: login URL for user. type str
    """
    return matches(
        {
            "yelluw": "https://yelluw.com/login",
            "Pablo": "https://pablojuan.com/login",
            },
        username,
        default=default
        )


def match_address_with(name, default="No addres for name"):
    """
    Match a given name with an address

    :param name: name if person. type str
    :returns address: address of person. type str
    """
    options = {
        "Pablo": "12345 Street Ave., The Moon",
        "Juan": "67890 Python Road, Guido's Basement"
        }

    return matches(options, name, default=default)


"""
Below are some more complex examples.
These show how to use types as keys
and functions as values.
"""

def match_postage_with(name_and_address, default=2.0):
    """
    Match a tuple of name and address
    with a postage rate

    :param name_and_address: name and address of person. typle tuple
    :returns postage: cost of postage. type float
    """
    options = {
        ("Pablo", "12345 Street Ave., The Moon"): 2.5,
        ("Juan", "67890 Python Road, Guido's Basement"): 3.0
    }
    return matches(options, name_and_address, default=default)


def florida_taxrate():
    """
    return a ficticious tax rate
    """
    return 15.0


def arizona_taxrate():
    """
    return a ficticious tax rate
    """
    return 18.0


def match_taxrate_with(income_and_state, default=20.0):
    """
    Match a tuple of income and state to taxrate.

    Taxrate is calculated by a separate function.

    :param: income and state of person to know taxrate. type tuple
    :returns tax rate: tax rate. type float
    """
    options = {
        (24000, "florida"): florida_taxrate(),
        (30000, "arizona"): arizona_taxrate()
    }
    return matches(options, income_and_state, default=default)
