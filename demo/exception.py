def demo_exception_group() -> None:
    try:
        raise ExceptionGroup(
            "g",
            [
                TypeError(""),
                ExceptionGroup(
                    "s",
                    [
                        TypeError("mistyped"),
                        ValueError("")
                    ]),
                ValueError("misconfigured")
            ]
        )
    except* TypeError as e:
        # e will be:
        #   ExceptionGroup(
        #       'g',
        #       [
        #           TypeError(''),
        #           ExceptionGroup('s', [TypeError('mistyped')])
        #       ]
        #   )
        print(f"exception {e!r}")
        raise e
    except* ValueError as e:
        # e will be:
        #   ExceptionGroup(
        #       'g', [
        #           ExceptionGroup('s', [ValueError('')]),
        #           ValueError('misconfigured')
        #       ]
        #   )
        print(f'expcetion {e!r}')
        raise

def demo_exception_with_note() -> None:
    try:
        raise ValueError("Value can't be negative")
    except Exception as e:
        e.add_note("result from demo_exception_with_note without args")
        raise
