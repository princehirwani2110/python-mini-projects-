def read_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    return content

def get_lines(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return lines