from hw10_caesar_cipher import *
from hw10_image_converter import *

from inspect import getframeinfo, stack

def unittest(did_pass):
    """
    Print the result of a unit test.
    :param did_pass: a boolean representing the test
    :return: None
    """

    caller = getframeinfo(stack()[1][0])
    linenum = caller.lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def CaesarCipher_test_suite():
    """
    A test suite for testing the encrypt and decrypt methods of the class

    NOTE:
    Typically, a test suite for a Class would be written into a second class entirely.
    However, to keep the complexity low, I chose to incorporate the test suite in a familiar way.
    In the future, we will explore how to properly write a test suite as a separate class.
    """

    # Tests encrypting a normal string
    caesar = CaesarCipher("encrypt")
    caesar.key = 3
    caesar.message = "A test string"
    caesar.encrypt()
    unittest(caesar.cipher == "D WHVW VWULQJ")

    # Tests encrypting a string with punctuation
    caesar.key = 13
    caesar.message = "It's a so-so kind of day!"
    caesar.encrypt()
    unittest(caesar.cipher == "VG'F N FB-FB XVAQ BS QNL!")

    # Tests decrypting a normal string
    caesar.key = 3
    caesar.cipher = "D WHVW VWULQJ"
    caesar.crypt_type = "decrypt"
    caesar.decrypt()
    unittest(caesar.message == "A TEST STRING")

    # Tests decrypting a string with punctuation
    caesar.key = 6
    caesar.cipher = "OZ'Y G YU-YU QOTJ UL JGE!"
    caesar.decrypt()
    unittest(caesar.message == "IT'S A SO-SO KIND OF DAY!")

    img_1, img_2 = ImageConverter("images/map_2.png"), ImageConverter("images/RF9152_2.png")
    unittest(img_r_diff(img_1, img_2) == 221)

CaesarCipher_test_suite()
