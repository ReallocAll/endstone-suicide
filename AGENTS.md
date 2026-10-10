# Development guidelines

- Keep the plugin focused on the player-only \`/suicide\` command; do not add confirmation screens, scheduling, storage, or configuration without a specific requirement.
- Preserve the command, its \`suicide.command.suicide\` permission, the Endstone entry point, and the \`0.11\` API version when making packaging-only changes.
- Support the declared Python range (\`>=3.10\`); avoid syntax or APIs requiring a newer Python release.
- Use uv, Hatchling, Ruff, and pytest. Run \`uv run ruff check .\`, \`uv run pytest -q\`, and \`uv build\` before commits when the tools are available.
- Keep Endstone imports at the public API surface and test command dispatch with isolated stubs; tests must not require a running BDS server.
- Never add server data, secrets, build artifacts, caches, or unrelated project files to the repository.
