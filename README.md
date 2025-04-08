<div align="center">
<a href="#">
    <img src="assets/images/logo.png" alt="Logo" width="125" height="125" />
</a>

<h3 align="center">Gigs By Bob</h3>
<p align="center">
    Bob will send you alerts on discord so that you can place bids on projects faster than other users on freelancer platform.
</p>
</div>

<br />

## Features

- Fetches the project details from [Freelancer.com](https://freelancer.com) website and sends alerts in discord.
- Details fetched from a project are:
    - Owner
    - Title
    - Description
    - URL
    - Type
    - Bidding Period
    - Currency
    - Min. Budget
    - Max. Budget
    - Bids Count
    - Required Skills
    - Attachments

<br />

## Built With

[![Python][Python]][Python-url]&nbsp; &nbsp;[![Discord][Discord]][Discord-url]&nbsp; &nbsp;[![Freelancer][Freelancer]][Freelancer-url]

<br />

## Prerequisites

- [Docker](https://docs.docker.com/engine/install/ubuntu/)

<br />

## Docker Setup

- Copy the `.env.sample` file to `.env`
```
cp .env.sample .env
```

- Fill up the environment variable values in the `.env` file
    - `DISCORD_TOKEN`: Follow [these](https://github.com/reactiflux/discord-irc/wiki/creating-a-discord-bot-&-getting-a-token) steps to generate discord bot token.
    - `GUILD_ID`: Enable **developer mode** and right click on the channel in your discord server to copy channel ID and paste it.
    - `FR_API_TOKEN`: Go to [this](https://accounts.freelancer.com/settings/develop) URL to generate API token for your freelancer account.

- Make sure `docker-compose.yml` and `.env` file are in the same folder.

- Start docker
```
docker compose up -d
```

<br />

# References

- https://developers.freelancer.com/docs
- https://discordpy.readthedocs.io/en/stable/discord.html

[Python]: https://img.shields.io/badge/python-FFE467?style=for-the-badge&logo=python&logoColor=blue
[Python-url]: https://www.python.org/
[Discord]: https://img.shields.io/badge/discord-5563EA?style=for-the-badge&logo=discord&logoColor=white
[Discord-url]: https://discord.com/
[Freelancer]: https://img.shields.io/badge/freelancer-ffffff?style=for-the-badge&logo=freelancer&logoColor=2AB1FB
[Freelancer-url]: https://freelancer.com/