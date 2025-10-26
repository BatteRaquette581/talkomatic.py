from datetime import datetime, UTC
from json import dump, load
from pathlib import Path
from requests import post, Response


API_AUTH_HEADERS = {"x-api-key": "tK_public_key_4f8a9b2c7d6e3f1a5g8h9i0j4k5l6m7n8o9p"}
BOT_TOKEN_PATH = "BOT_TOKEN_DO_NOT_SHARE_OR_DELETE_OR_MODIFY"

def get_auth_bot_token() -> str:
    """
    Fetches the bot token and returns it, by requesting it from the server if expired
    or doesn't exist, but loads from a local file if it exists and isn't expired.
    """

    if Path(BOT_TOKEN_PATH).exists():
        with open(BOT_TOKEN_PATH, "r") as token_file:
            token_json: dict = load(token_file)
            token_expiry: datetime = datetime.fromisoformat(token_json["expiresAt"])
            if datetime.now(UTC) < token_expiry:
                return token_json["token"]

    token_res: Response = post("https://classic.talkomatic.co/api/v1/bot-tokens/request")
    if token_res.status_code != 201:
        raise Exception(str(token_res.json()))
    token: str = token_res.json()["token"]
    with open(BOT_TOKEN_PATH, "w") as token_file:
        dump(token_res.json(), token_file)
    return token
