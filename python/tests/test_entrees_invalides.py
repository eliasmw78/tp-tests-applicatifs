"""PARTIE 2 - Tests des ENTREES INVALIDES.

On verifie que le code REJETTE proprement les mauvaises entrees,
en levant une exception explicite (et pas en crashant n'importe comment).
"""

import pytest
from src.task import Task
from src.exceptions import InvalidInputError
from src.validators import (
    validate_title,
    validate_priority,
    validate_status,
    validate_due_date,
    TITLE_MAX,
)


@pytest.mark.invalides
def test_titre_vide_rejete():
    with pytest.raises(InvalidInputError):
        validate_title("")


@pytest.mark.invalides
def test_titre_uniquement_espaces_rejete():
    with pytest.raises(InvalidInputError):
        validate_title("   ")


@pytest.mark.invalides
def test_titre_trop_long_rejete():
    with pytest.raises(InvalidInputError):
        validate_title("x" * (TITLE_MAX + 1))


@pytest.mark.invalides
def test_titre_non_string_rejete():
    with pytest.raises(InvalidInputError):
        validate_title(42)


@pytest.mark.invalides
def test_priorite_inconnue_rejetee():
    with pytest.raises(InvalidInputError):
        validate_priority("urgent")


@pytest.mark.invalides
def test_statut_inconnu_rejete():
    with pytest.raises(InvalidInputError):
        validate_status("en_pause")


@pytest.mark.invalides
def test_date_non_iso_rejetee():
    with pytest.raises(InvalidInputError):
        validate_due_date("31/12/2026")


@pytest.mark.invalides
def test_date_inexistante_rejetee():
    with pytest.raises(InvalidInputError):
        validate_due_date("2026-02-30")


@pytest.mark.invalides
def test_task_avec_titre_invalide_rejete():
    with pytest.raises(InvalidInputError):
        Task(id=1, title="")


# ------------------------------------------------------------------
# Tests d'entrées invalides ajoutés — Pattern AAA
# ------------------------------------------------------------------


@pytest.mark.invalides
def test_priorite_fantaisiste_ultra_high_leve_invalid_input_error():
    # Arrange
    priorite_invalide = "ultra-high"

    # Act / Assert
    with pytest.raises(InvalidInputError) as exc_info:
        validate_priority(priorite_invalide)

    assert "ultra-high" in str(exc_info.value)
