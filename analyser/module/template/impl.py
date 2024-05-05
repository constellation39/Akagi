from analyser import Analyser


class Impl(Analyser):
    def __init__(self):
        super().__init__()
        raise RuntimeError("Not implemented, Please import implement.")

    def launch(self, player_id: int) -> None:
        pass

    def close(self) -> None:
        pass

    def restart(self, player_id: int) -> None:
        pass

    def react(self, data: str) -> str:
        pass
