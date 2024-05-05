import json

import requests

from analyser.module.mortal_4p import bot
from analyser.analyser import Analyser
from loguru import logger


class Impl(Analyser):
    def __init__(self):
        self.player_id = 0
        self.bot = None

    def launch(self, player_id: int) -> None:
        self.player_id = player_id
        self.bot = bot.Bot(player_id)

    def close(self) -> None:
        self.bot = None

    def restart(self, player_id: int) -> None:
        self.close()
        self.launch(player_id)

    def react(self, events: str) -> str:
        if self.bot is None:
            raise ValueError("analyser is not running (3)")

        try:
            input_data = events.encode("utf8")

            logger.debug(f"{self.player_id} <- {input_data}")
            outs = self.bot.react(input_data)
            logger.debug(f"{self.player_id} -> {outs}")

            if (
                json.loads(events)[-1]["type"] == "tsumo"
                and json.loads(events)[-1]["actor"] == self.player_id
            ):
                try:
                    json_data = json.loads(outs)
                except Exception:
                    raise RuntimeError(f"JSON parser error: {outs}")

                if json_data["type"] == "none":
                    raise RuntimeError(f"invalid response: {str(outs)}")

        except requests.Timeout:
            raise RuntimeError(f"Timeout player_id={self.player_id}")
        except Exception as e:
            raise RuntimeError(f"Error player_id={self.player_id} {e}")
        return outs

    def hash(self) -> str:
        return self.bot.model_hash
