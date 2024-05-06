from abc import ABC, abstractmethod


class Analyser(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def launch(self, player_id: int) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass

    @abstractmethod
    def restart(self, player_id: int) -> None:
        pass

    @abstractmethod
    def react(self, data: str) -> str:
        pass

    @abstractmethod
    def hash(self) -> str:
        pass

    @abstractmethod
    def state(self):
        pass
