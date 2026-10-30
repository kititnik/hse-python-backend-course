from models.user import User


def select_top_users_by_rate(users: list[User], top_size: int) -> list[User]:
    if top_size < 0:
        raise ValueError("top_size must be non-negative")
    ordered = sorted(users, key=lambda user: user.rate, reverse=True)
    return ordered[:top_size]
