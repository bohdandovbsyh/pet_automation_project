import inspect

import allure


def auto_steps(cls):
    """
    Decorator to automatically add allure.step decorator to all methods inside class
    Args:
        cls: Class
    """
    for name, method in inspect.getmembers(cls):
        if (not inspect.isfunction(method)) or inspect.isbuiltin(method) and method.name.startswith("__"):
            continue
        setattr(cls, name, allure.step(method))
    return cls
