import importlib.util
import pathlib
import sys
import types


class FakeCommandSender:
    def __init__(self):
        self.errors = []

    def send_error_message(self, message):
        self.errors.append(message)


class FakePlayer(FakeCommandSender):
    def __init__(self):
        super().__init__()
        self.health = 20


class FakeCommand:
    def __init__(self, name):
        self.name = name


class FakePlugin:
    pass


endstone = types.ModuleType("endstone")
endstone.Player = FakePlayer
command_mod = types.ModuleType("endstone.command")
command_mod.Command = FakeCommand
command_mod.CommandSender = FakeCommandSender
plugin_mod = types.ModuleType("endstone.plugin")
plugin_mod.Plugin = FakePlugin
sys.modules["endstone"] = endstone
sys.modules["endstone.command"] = command_mod
sys.modules["endstone.plugin"] = plugin_mod

plugin_path = pathlib.Path(__file__).parents[1] / "src" / "endstone_suicide" / "plugin.py"
spec = importlib.util.spec_from_file_location("suicide_plugin", plugin_path)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


def test_player_suicide():
    player = FakePlayer()
    plugin = module.SuicidePlugin()
    assert plugin.on_command(player, FakeCommand("suicide"), []) is True
    assert player.health == 0


def test_console_rejected():
    sender = FakeCommandSender()
    plugin = module.SuicidePlugin()
    assert plugin.on_command(sender, FakeCommand("suicide"), []) is True
    assert sender.errors == ["只有玩家可以使用 /suicide。"]


def test_unknown_command_not_handled():
    player = FakePlayer()
    plugin = module.SuicidePlugin()
    assert plugin.on_command(player, FakeCommand("other"), []) is False
    assert player.health == 20


def test_metadata():
    plugin = module.SuicidePlugin
    assert plugin.api_version == "0.11"
    assert plugin.commands["suicide"]["usages"] == ["/suicide"]
    assert plugin.permissions["suicide.command.suicide"]["default"] is True
