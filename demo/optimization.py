import sys


def c_style_f_style_formatting() -> None:
    # F style formatting
    f'{"word"!a}{"word"!r}{"word"!s}'
    # C style formatting
    "%a%r%s" % ("word", "word", "word")
    # f string => ~169 ns ± 7 ns
    # c string => ~209ns ± 10 ns

def demo_dict_hash() -> None:
    d = {
        "a": "b",
        "c": "d",
        "e": "f"
    }
    print(sys.getsizeof(d))
    # python 3.11 => 184
    # python 3.10 => 232


def try_except() -> None:
    try:
        1/1
    except ZeroDivisionError as e:
        print(e)
        raise
    # python 3.11 => 8.93 ns
    # python 3.10 => 17.6 ns
