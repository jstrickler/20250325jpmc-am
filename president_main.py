from president import President

for term in 1, 16, 32, 37, 39:
    p = President(term)
    print(f"{p.first_name} {p.last_name} was born at {p.birth_place}, {p.birth_state} on {p.birth_date}")
