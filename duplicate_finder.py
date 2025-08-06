
items = [11,8,8]

def find_duplicates(items):
    s = set()
    duplicates = set()

    for item in items:
        if item in s:
            duplicates.add(item)
        else:
            s.add(item)
    if duplicates:
        return list(duplicates)
    else:
        return "No dublicats found"
    

duplicate = find_duplicates(items)

print("Duplicate Values : ",duplicate)



