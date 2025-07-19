import re

def is_valid_name(name: str) -> bool:
    if not name:
        return False
    if len(name) < 2 or len(name) > 50:
        return False
    if not re.match(r"^[A-Za-z\s\-]+$", name):
        return False
    return True
