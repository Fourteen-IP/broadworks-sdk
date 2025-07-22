"""
thor's hammer exceptions
"""

import attr


@attr.s(slots=True, frozen=True)
class THError(Exception):
    """Base Exception raised by Thor's Hammer.

    Attributes:
        message: Why something failed
        context: BWKS Type/ Command that failed
    """

    message: str = attr.ib()
    context = attr.ib(default=None)

    def __str__(self):
        return f"{self.__class__.__name__}({self.message})"


@attr.s(slots=True, frozen=True)
class THErrorResponse(THError):
    """
    Exception raised when an ErrorResponse is received and decoded.
    """

    pass


@attr.s(slots=True, frozen=True)
class THErrorTimeOut(THError):
    """
    Exception raised when nothing is head back from the server.
    """

    pass


@attr.s(slots=True, frozen=True)
class THErrorUnknown(THError):
    """
    Exception raised when life becomes too much for the software.
    """

    pass


@attr.s(slots=True, frozen=True)
class THErrorAPISetup(THError):
    """
    Exception raised when life becomes too much for the software.
    """

    pass


@attr.s(slots=True, frozen=True)
class THErrorAttributeMissing(THError):
    """
    Exception raised when a required attribute is missing.
    """

    pass


@attr.s(slots=True, frozen=True)
class THErrorUnexpectedAttribute(THError):
    """
    Exception raised when additional elements passed to __init__
    """

    pass


@attr.s(slots=True, frozen=True)
class THErrorSocketInitialisation(THError):
    """
    Exception raised when the TCP socket fails to initiate.
    """

    pass


@attr.s(slots=True, frozen=True)
class THErrorSocketTimeout(THError):
    """
    Exception raised when the TCP socket fails to initiate.
    """

    pass


@attr.s(slots=True, frozen=True)
class THErrorSendRequestFailed(THError):
    """
    Exception raised when the TCP socket fails to initiate.
    """

    pass
