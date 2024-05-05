from bot import Bot


class Impl(Bot):
    def __init__(self):
        super().__init__()

    def launch_bot(self, player_id: int) -> None:
        pass

    def delete_bot(self) -> None:
        pass

    def restart_bot(self, player_id: int) -> None:
        pass

    def react(self, data: str) -> str:
        pass
