# -*- coding: utf-8 -*-


def unsafe_perform_io(wrapped_in_io):
    """
    Compatibility utility and escape mechanism from ``IO`` world.

    Just unwraps the internal value
    from :py:class:`IO <returns.io.IO>` container.
    Should be used with caution!
    Since it might be overused by tired developers.

    It is recommended to have only one place (module / file)
    in your program where you allow unsafe operations.

    We recommend to use ``import-linter`` to enforce this rule:

    - https://github.com/seddonym/import-linter

    """
    return wrapped_in_io._inner_value  # noqa: Z441