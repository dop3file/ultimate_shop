from fastapi import HTTPException


class UserException(HTTPException):
    ...


class UserNotFound(UserException):
    def __init__(self, detail: str):
        super().__init__(
            status_code=400,
            detail=detail
        )


class IncorrectPassword(UserException):
    def __init__(self, detail: str):
        super().__init__(
            status_code=400,
            detail=detail
        )


class UserExists(UserException):
    def __init__(self, detail: str):
        super().__init__(
            status_code=403,
            detail=detail
        )