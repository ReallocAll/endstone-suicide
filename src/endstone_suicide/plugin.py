from endstone import Player
from endstone.command import Command, CommandSender
from endstone.plugin import Plugin


class SuicidePlugin(Plugin):
    api_version = "0.11"

    commands = {
        "suicide": {
            "description": "立即结束自己的生命。",
            "usages": ["/suicide"],
            "permissions": ["suicide.command.suicide"],
        }
    }

    permissions = {
        "suicide.command.suicide": {
            "description": "允许玩家使用 /suicide。",
            "default": True,
        }
    }

    def on_command(
        self, sender: CommandSender, command: Command, args: list[str]
    ) -> bool:
        if command.name != "suicide":
            return False

        if not isinstance(sender, Player):
            sender.send_error_message("只有玩家可以使用 /suicide。")
            return True

        sender.health = 0
        return True
