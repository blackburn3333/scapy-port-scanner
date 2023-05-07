import os


def out(data):
    if list == type(data):
        for line in data:
            print(line)
    else:
        print(data)


def title_container(title, sub_title=""):
    padding = 30
    _padding = padding * " "
    _title = "##" + _padding + title + _padding + "##"
    _sub_title = "##" + _padding + sub_title + _padding + "##"
    _sub_title_len = (len(_sub_title))
    title_len = len(_title)
    _seperator = title_len * "#"
    _new_line = "##" + (title_len - 4) * " " + "##"
    out([_seperator, _title, _seperator])
    return title_len


def menu_container(texts, window_width):
    titles = []
    for text in texts:
        _text = "## " + text
        _len = len(_text)
        rest = (window_width - _len) - 2
        rend = _text + rest * " " + "##"
        titles.append(rend)
    titles.append("#" * window_width)
    out(titles)


def check_choice_input(menu_input, input_group, input_text):
    if menu_input in input_group:
        return menu_input
    else:
        print("> Invalid input")
        _menu_input = input(input_text + " ")
        return check_choice_input(_menu_input, input_group, input_text)


def exit_terminal():
    print("> Good Bye.")
    exit()


def clean_terminal():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')
