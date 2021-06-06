from functools import wraps, partial
import inspect

__all__ = ['helper']


def helper(user_deco=None):
    """
    Example:
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
    """
    if user_deco is None:
        return helper

    if not callable(user_deco):
        raise TypeError('Delper.deco accept only 1 argument that is callable')

    @wraps(user_deco)
    def __user_deco(*d_args, **d_kwargs):
        if len(d_args) == 0 or not callable(d_args[-1]):
            return partial(__user_deco, *d_args, **d_kwargs)

        @wraps(d_args[-1])
        def wrapper(*f_args, **f_kwargs):
            return user_deco(d_args[-1], f_args, f_kwargs, *d_args[:-1], **d_kwargs)

        return wrapper

    sig_user_deco = inspect.signature(user_deco)
    __user_deco.__signature__ = sig_user_deco.replace(parameters=list(sig_user_deco.parameters.values())[3:])
    return __user_deco
