#Convert all strings in a tuple to uppercase.
def to_uppercase(tpl):
    return tuple(s.upper() if isinstance(s, str) else s for s in tpl)

print(to_uppercase(("hello", "world", 123)))  # Output: ('HELLO', 'WORLD', 123)
