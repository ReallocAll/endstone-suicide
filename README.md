# Endstone Suicide

A minimal \`/suicide\` command for Endstone servers. The command immediately sets the executing player's health to zero, using the standard game death and respawn flow.

## Features

- Player-only \`/suicide\` command with no confirmation or cooldown.
- Permission \`suicide.command.suicide\`, granted to all players by default.
- No event handlers, scheduled tasks, persistent data, or configuration files.

## Installation

Download or build \`endstone_suicide-0.1.0-py3-none-any.whl\`, copy it to the server's \`plugins/\` directory, and restart the server. This plugin targets the Endstone 0.11 API and declares Python 3.10 or newer, as in the original 0.1.0 release.

## Commands and permissions

| Command | Description | Permission | Default |
| --- | --- | --- | --- |
| \`/suicide\` | Immediately kills the executing player. | \`suicide.command.suicide\` | Everyone |

Console and other non-player senders cannot run the command. No configuration is required.

## Development

Install [uv](https://docs.astral.sh/uv/), then run:

\`\`\`sh
uv sync --extra dev
uv run ruff check .
uv run pytest -q
uv build
\`\`\`

The wheel contains the \`suicide\` Endstone entry point, exported as \`endstone_suicide:SuicidePlugin\`.

## License

GPL-3.0-only. See [LICENSE](LICENSE). The Endstone API is provided by the Endstone project under Apache-2.0 and is not bundled with this plugin.
