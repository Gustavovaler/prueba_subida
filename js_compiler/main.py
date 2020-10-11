


def query_selector(e_type, e_name):
    return f"document.querySelector(\'{e_type}{e_name}\');"

def open_label():
    return "<script>"

def close_label():
    return "</script>"




print(open_label())
print(query_selector('#', 'menu'))
print(query_selector('.', 'btn'))
print(close_label())