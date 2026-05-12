"""PARTIE 1 - Premier test vert : tests UNITAIRES sur la classe Task.

Objectif : un test = une assertion sur UNE seule unite de comportement.
Pattern AAA : Arrange (preparer) / Act (executer) / Assert (verifier).
"""

import pytest
from src.task import Task


@pytest.mark.unitaire
def test_task_se_cree_avec_titre():
    # Arrange
    titre = "Faire les courses"
    # Act
    tache = Task(id=1, title=titre)
    # Assert
    assert tache.title == titre


@pytest.mark.unitaire
def test_task_a_un_id():
    tache = Task(id=42, title="Apprendre pytest")
    assert tache.id == 42


@pytest.mark.unitaire
def test_task_demarre_en_statut_todo_par_defaut():
    tache = Task(id=1, title="Demarrer le projet")
    assert tache.status == "todo"


@pytest.mark.unitaire
def test_task_priorite_par_defaut_est_medium():
    tache = Task(id=1, title="Une tache")
    assert tache.priority == "medium"


@pytest.mark.unitaire
def test_task_to_dict_renvoie_les_bons_champs():
    tache = Task(id=1, title="Voyager", priority="high")
    d = tache.to_dict()
    assert d["id"] == 1
    assert d["title"] == "Voyager"
    assert d["priority"] == "high"
    assert "created_at" in d


# ------------------------------------------------------------------
# Tests unitaires ajoutés — Pattern AAA
# ------------------------------------------------------------------


@pytest.mark.unitaire
def test_task_description_optionnelle_est_vide_par_defaut():
    # Arrange
    titre = "Tache sans description"

    # Act
    tache = Task(id=10, title=titre)

    # Assert
    assert tache.description == ""


@pytest.mark.unitaire
def test_task_description_optionnelle_est_conservee_quand_fournie():
    # Arrange
    titre = "Tache avec description"
    description = "Ceci est une description détaillée."

    # Act
    tache = Task(id=11, title=titre, description=description)

    # Assert
    assert tache.description == description


@pytest.mark.unitaire
def test_task_created_at_est_au_format_iso_8601():
    # Arrange
    import re
    # Regex correspondant au format ISO 8601 sans timezone (ex: 2026-05-12T09:15:00)
    pattern_iso = r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}$"

    # Act
    tache = Task(id=12, title="Vérifier la date")

    # Assert
    assert re.match(pattern_iso, tache.created_at), (
        f"created_at '{tache.created_at}' n'est pas au format ISO 8601"
    )


@pytest.mark.unitaire
def test_task_to_dict_contient_tous_les_champs_attendus():
    # Arrange
    tache = Task(
        id=13,
        title="Mission complète",
        description="Une vraie description",
        priority="low",
        status="done",
    )

    # Act
    resultat = tache.to_dict()

    # Assert
    assert resultat["id"] == 13
    assert resultat["title"] == "Mission complète"
    assert resultat["description"] == "Une vraie description"
    assert resultat["priority"] == "low"
    assert resultat["status"] == "done"
    assert resultat["due_date"] is None
    assert "created_at" in resultat
