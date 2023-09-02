import discord
from dictator.objects import CharacterName, GameUsername, PlayerID, InvalidNameFormat


def validate_username_identifier(
    identifider: str,
) -> GameUsername | discord.User | InvalidNameFormat:
    #return GameUsername(username="xyz")
    return NotImplementedError


def validate_whowas_identifier(
    identifier: str,
) -> CharacterName | PlayerID | InvalidNameFormat:
    #return CharacterName(name="xyz")
    return NotImplementedError