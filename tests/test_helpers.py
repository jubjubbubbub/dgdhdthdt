import pytest
import discord

from dictator.objects import (
    CharacterName,
    GameUsername,
    PlayerID,
    InvalidNameFormat,
)
from dictator.helpers import validate_username_identifier, validate_whowas_identifier

@pytest.mark.parametrize(
    "identifider, expected_result",
    [
        ("", InvalidNameFormat),
        ("a", InvalidNameFormat),
        ("aa", InvalidNameFormat),
        ("12.0", InvalidNameFormat),
        ("an invalid sentence", InvalidNameFormat),
        ("aaa", GameUsername),
        ("Colin-9391", GameUsername),
        ("TanyaB-2264", GameUsername),
        ("noahboi", GameUsername),
        ("beetleapple24498", GameUsername),
        ("133369377230684160", discord.User),
        ("878215080058175539", discord.User),
    ],
)
def test_validate_username_identifier(identifider, expected_result):
    assert isinstance(validate_username_identifier(identifider), expected_result)


@pytest.mark.parametrize(
    "identifier, expected_result",
    [
        ("", InvalidNameFormat),
        ("a", InvalidNameFormat),
        ("12.0", InvalidNameFormat),
        ("an invalid username", InvalidNameFormat),
        ("28564", PlayerID),
        ("571259", PlayerID),
        ("Hera Tidd", CharacterName),
        ("Maddie Pumpkin", CharacterName),
        ("Hope", CharacterName),
        ("Eve", CharacterName),
        ("Vy", CharacterName),
        ("Eve An", CharacterName),
    ],
)
def test_validate_whowas_identifier(identifier, expected_result):
    assert isinstance(validate_whowas_identifier(identifier), expected_result)
