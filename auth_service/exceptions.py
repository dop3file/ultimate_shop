class UserException(Exception):
    ...


class UserNotFound(UserException):
    ...


class IncorrectPassword(UserException):
    ...