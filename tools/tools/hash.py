from passlib.context import CryptContext


class Hash:
    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def hash(self, value: str) -> str:
        return self.pwd_context.hash(value)

    def verify_hash(self, not_hash: str, hash: str) -> bool:
        return self.pwd_context.verify(not_hash, hash)