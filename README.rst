Decorator Helper
================

:Version: 0.0.2
:Download: https://pypi.org/project/deco-helper/
:Source: https://github.com/Kcheonwoong/deco_helper
:Keywords: decorator

- Python (3.6, 3.7, 3.8, 3.9)


    .. code-block:: python

        from deco_helper import helper

        @helper
        def my_decorator(func, f_args, f_kwargs, *deco_args, **deco_kwargs):
            print(deco_args, deco_kwargs)
            result = func(*f_args, **f_kwargs)
            return result


        @my_decorator('first', 'end', k='v')
        def my_function(a, b, c=None):
            print(a, b, c)
            return 'hello world'


        print(my_function(1, 2, 3))

- **Simple Declaration**

    You  don't need to check your decorator receive function when your decorator have some arguments.

    The helper wraps your function that have your decorator for meta(__name__, __doc__).

    The helper automatically delegate function args and decorator args.


Installation
============

You can install Celery either via the Python Package Index (PyPI)
or from source.

To install using ``pip``:

::

    $ pip install deco_helper


License
=======

MIT