import asyncio
import contextlib
import re
import unittest
import os


def demo_asyncio_taskgroup() -> None:
    async def square(x: int):
        print(y:=x*x)
        return y

    async def asyncio_taskgroup() -> None:
        # old way
        # futures = map(square, range(5))
        # await asyncio.gather(*futures)
        # => less readable, less adaptable

        async with asyncio.TaskGroup() as task_group:
            for x in range(5):
                task_group.create_task(square(x))
    asyncio.run(asyncio_taskgroup())


def demo_contextlib_chdir() -> None:
    # change dynamicly the current directory
    # then go back to the old one when exiting
    # the context manager
    current_dir = os.getcwd()
    print(f'{current_dir=}')
    with contextlib.chdir('../..'):
        new_current_dir = os.getcwd()
        assert new_current_dir != current_dir
        print(f'{new_current_dir=}')

    final_dir = os.getcwd()
    print(f'{final_dir=}')
    assert final_dir == current_dir

def demo_re_atomic() -> None:
    # for abcc:
    #    -> match first 'a', then match 'bc', then match 'c'
    # for abc:
    #    -> match 'a', then match 'bc', then failed
    #    But the non atomic version go back to 'b', then match 'c'
    # => reduce regex exec time
    # (failed if the first generate expression not match, no retry with other sub part)

    atomic_regex = re.compile('a(?>bc|b)c')
    non_atomic_regex = re.compile("a(bc|b)c")
    for text in ['abcc', 'abc']:
        print(f'atomic match {text}?:', atomic_regex.match(text))
        print(f'non atomic match {text}?:', non_atomic_regex.match(text))

def demo_re_possessive_quantifier() -> None:
    # for 'bb':
    #   for possessive quantifier:
    #       -> (?:a|b) match b, then (?:a|b) match b, then b match nothing => failed
    #   for non possessive quantifier:
    #       -> (?:a|b) match b, (?:a|b) match b, then b match nothing => backtracking
    #                         , b match b => succes
    possessive_regex = re.compile('(?:a|b)*+b')
    non_possessive_regex = re.compile('(?:a|b)*b')
    for text in ['b', 'ab', 'bb', 'abc']:
        print(f'atomic match {text}?:', possessive_regex.match(text))
        print(f'non atomic match {text}?:', non_possessive_regex.match(text))


# demo unittest
class TestSomeThing(unittest.TestCase):
    def setUp(self) -> None:
        self.current_dir = os.getcwd()
        self.enterContext(contextlib.chdir(".."))

    def test_something(self) -> None:
        assert os.getcwd() == os.path.dirname(self.current_dir)
