from typing import Type
import importlib.util

from analyser.analyser import Analyser


def load_bot(module_name) -> Analyser:
    try:
        module_path = f"analyser.module.{module_name}.impl"
        module = importlib.import_module(module_path)
        Impl = getattr(module, "Impl")
        print(f'Loaded module {module_name} Success.')
        return Impl()
    except ModuleNotFoundError:
        raise ValueError(f"Module {module_name} not found.")
    except AttributeError:
        raise ValueError(f"Class Impl not found in module {module_name}.impl.")


if __name__ == "__main__":
    bot = load_bot("template")
    print(bot)
