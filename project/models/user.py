import uuid


class User:
    def __init__(self, name: str) -> None:
        self.id = uuid.uuid4()
        self.edit_name(name)
        self.comments_count = 0
        self.rate = 0
        self.is_banned = False

    def edit_name(self, new_name: str) -> None:
        if not new_name.strip():
            raise ValueError("name should not be empty")
        self.name = new_name

    def increment_rate(self) -> None:
        self.rate += 1

    def ban_user(self) -> None:
        self.is_banned = True

    def unban_user(self) -> None:
        self.is_banned = False

    def __repr__(self) -> str:
        return f"User: id={self.id}, " \
                f"name={self.name}, comments_count={self.comments_count}, " \
                f"rate={self.rate}, is_banned={self.is_banned}"
