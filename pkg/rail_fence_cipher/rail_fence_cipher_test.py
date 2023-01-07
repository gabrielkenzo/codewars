import pytest
from rail_fence_cipher import encode_rail_fence_cipher, decode_rail_fence_cipher


class TestCase:
    def __init__(self, decoded, n, encoded):
        self.decoded = decoded
        self.n = n
        self.encoded = encoded


def test_encode_rail_fence_cipher():
    # Arrange
    inputs = [
        TestCase("WEAREDISCOVEREDFLEEATONCE", 3, "WECRLTEERDSOEEFEAOCAIVDEN"),
        TestCase("Hello, World!", 3, "Hoo!el,Wrdl l"),
        TestCase("Hello, World!", 4, "H !e,Wdloollr"),
        TestCase("I'm a Riven OTP and a Raze OTP", 5, "Ivaz'ie naemRnPdR    T  OPaOaT"),
    ]
    # inputs = [
    #     ["WEAREDISCOVEREDFLEEATONCE", 3, "WECRLTEERDSOEEFEAOCAIVDEN"],
    #     ["Hello, World!", 3, "Hoo!el,Wrdl l"],
    #     ["Hello, World!", 4, "H !e,Wdloollr"],
    #     ["I'm a Riven OTP and a Raze OTP", 5, "Ivaz'ie naemRnPdR    T  OPaOaT"],
    # ]

    for test_case in inputs:
        # Act
        got = encode_rail_fence_cipher(test_case.decoded, test_case.n)

        # Assert
        assert got == test_case.encoded
