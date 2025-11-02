# Discord Stroke Assistant Bot

On the long road to recovery from a stroke, this bot is intended to provide the affected individual with several helpful tools.

## Features
- Provides a configurable medication reminder.
- Configurable alerting and logging.

## Requirements
- A Discord application and bot token
- Python 3.8+ (depends on implementation in this repo)
- Environment to host the bot (VM, container, or serverless)

## Installation
1. Clone the repository:

   git clone https://github.com/behrensger/discord_stroke_support_bot.git
   cd discord_stroke_support_bot

2. Install dependencies for Python (if applicable):

   pip install -r requirements.txt

## Configuration
Create a .env file or set environment variables with the following values:

- DISCORD_TOKEN: Your Discord bot token
- GUILD_ID: (Optional) Guild/server ID to restrict commands during development
- EMERGENCY_CONTACT: (Optional) Local emergency number to display
- LOG_LEVEL: (Optional) logging verbosity (info, debug, warn)

Example .env:

DISCORD_TOKEN=your_discord_token_here
GUILD_ID=123456789012345678
EMERGENCY_CONTACT=911
LOG_LEVEL=info

## Usage
Start the bot for Python:

   python bot.py

Once running, invite the bot to your server using the OAuth2 URL with appropriate bot permissions (sending messages, reading message history).

## Contributing
Contributions are welcome. Please open an issue to discuss changes or submit a pull request with tests and documentation.

## Security
Never commit your bot token or other secrets to the repository. Use environment variables or a secrets manager.

## License
Specify a license for the project (e.g., MIT).

---

This README was added by GitHub Copilot to provide an initial project overview. Please edit to reflect the repository's actual implementation details.
