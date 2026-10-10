# Development guidelines

- Keep the plugin focused on the player-only `/suicide` command; do not add confirmation screens, scheduling, storage, or configuration without a specific requirement.
- Preserve the command, its `suicide.command.suicide` permission, the Endstone entry point, and the `0.11` API version when making packaging-only changes.
- Support Python 3.11 and newer; run CI tests across Python 3.11–3.15 and avoid syntax or APIs that would break Python 3.11.
- Use uv, Hatchling, Ruff, and pytest. Run `uv run ruff check .`, `uv run pytest -q`, and `uv build` before commits when the tools are available.
- Keep Endstone imports at the public API surface and test command dispatch with isolated stubs; tests must not require a running BDS server.
- Never add server data, secrets, build artifacts, caches, or unrelated project files to the repository.
