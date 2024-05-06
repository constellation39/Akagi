import json

from analyser.analyser import Analyser
from analyser.module.kanachan._kanachan import Kanachan
from loguru import logger

from analyser.module.mortal_4p import bot


class Impl(Analyser):
    def __init__(self):
        self.player_id = None
        self.kanachan = None
        self.bot = None

    def launch(self, player_id: int) -> None:
        self.player_id = player_id
        self.kanachan = Kanachan()
        self.bot = bot.Bot(player_id)

    def close(self) -> None:
        self.kanachan = None

    def restart(self, player_id: int) -> None:
        self.close()
        self.launch()

    def react(self, events: str) -> str:
        if self.kanachan is None:
            raise ValueError("analyser is not running (3)")

        if self.bot is None:
            raise ValueError("analyser is not running (3)")

        try:
            input_data = events.encode("utf8")
            outs = self.bot.react(input_data)
        except Exception as e:
            raise RuntimeError(f"Error player_id={self.player_id} {e}")

        try:
            ins = json.loads(events)
            logger.debug(f"{self.player_id} <- {ins}")
            outs = self.kanachan.run(ins)
            logger.debug(f"{self.player_id} -> {outs}")
        except Exception as e:
            raise RuntimeError(f"Error player_id={self.player_id} ins {ins} outs {outs} e {e}")
        return json.dumps(outs)

    def state(self):
        return self.bot.state()

    def hash(self) -> str:
        return "kanachan"
