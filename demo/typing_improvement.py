from typing import Any, Generic, LiteralString, Self, TypeVarTuple
import random

def demo_variadic_generic() -> None:
    VarGen = TypeVarTuple('VarGen')
    class Array(Generic[*VarGen]):
        def __init__(self, shape: tuple[*VarGen]) -> None:
            self._shape = shape

        @property
        def shape(self) -> tuple[*VarGen]:
            return self._shape

    x : Array[float, int, int] = Array((1., 12, 14))
    y : Array[int] = Array((14,))
    z : Array[*tuple[complex, ...]] = Array(tuple())


    class Plan(tuple[Array[*tuple[complex, ...]], ...]):
        def __init__(self, dims: tuple[Array[*tuple[complex, ...]], ...]):
            self._dims = dims

        @property
        def dims(self) -> tuple[Array[*tuple[complex, ...]]]:
            return self._dims
    Plan((x, y, z))


def demo_self_typing() -> None:
    class NewClass():
        def __enter__(self) -> Self:
            return self

        def __exit(self, *args: Any, **kwargs: Any):
            ...

    def Inheritance(NewClass):
        def __enter__(self) -> Self:
            print(self)
            return self

        def get_instance(cls: type[Self]) -> Self:
            return cls()


def demo_literal_string() -> None:

    def query_dsl(input_query: LiteralString) -> None:
        ...

    some_string: str = "".join(chr(random.randint(96, 120)) for _ in range(10))
    base_query_dsl: LiteralString = "input | get-value | sort"
    extract_alpha_key = "extract key | filter key = [a-zA-Z]"  # LiteralString

    query_dsl("input | get-value")
    query_dsl(some_string)  # type check will fail
    query_dsl(base_query_dsl)  # ok
    query_dsl(f"{base_query_dsl} | {some_string}")  # type check will fail
    query_dsl(base_query_dsl + " | " + extract_alpha_key)  # ok
