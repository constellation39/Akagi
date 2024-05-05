from os import path


def load_model(model_path: str) -> bytes:
    full_model_path = get_model_path(model_path)

    with open(full_model_path, "rb") as model_file:
        model_data = model_file.read()

    return model_data


def get_model_path(model_path: str) -> str:
    return path.join(path.dirname(__file__), "model", model_path)
