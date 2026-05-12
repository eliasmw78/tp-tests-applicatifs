"""PARTIE 4 - Tests de REGRESSION.

But : capturer un bug SPECIFIQUE deja rencontre, pour qu'il ne revienne JAMAIS.
La regle : on nomme le test avec l'ID du bug et un resume.

A FAIRE PAR L'ELEVE :
1. Trouver le bug dans src/task_manager.py (indice : delete_task).
2. Ecrire ici le test qui demontre le bug -> il doit ECHOUER en l'etat.
3. Corriger le code dans src/task_manager.py.
4. Relancer pytest -> le test doit DESORMAIS passer.
5. Commit avec le message : "fix(bug-001): delete_task utilise l'id, plus l'index"
"""

import pytest
from src.task_manager import TaskManager
from src.exceptions import TaskNotFoundError


@pytest.mark.regression
def test_bug_001_delete_task_supprime_par_id_pas_par_index():
    """
    Bug initial : delete_task(task_id) appelait self._tasks.pop(task_id)
    et traitait l'argument comme un INDEX, pas comme un ID.

    Scenario qui revele le bug :
        - On cree 3 taches (ids 1, 2, 3)
        - On supprime celle d'id=2
        - Le manager doit contenir desormais SEULEMENT les taches 1 et 3
    """
    mgr = TaskManager()
    mgr.create_task("Tache id=1")
    mgr.create_task("Tache id=2 - a supprimer")
    mgr.create_task("Tache id=3")

    mgr.delete_task(2)

    ids_restants = sorted(t.id for t in mgr.list_tasks(sort_by="id"))
    assert ids_restants == [1, 3], (
        f"Bug-001 : delete_task(2) devrait supprimer la tache id=2, "
        f"mais il reste {ids_restants}"
    )


# ------------------------------------------------------------------
# Test de régression ajouté
# ------------------------------------------------------------------

@pytest.mark.regression
def test_bug_001_delete_task_id_inexistant_leve_erreur():
    """
    Vérifie qu'essayer de supprimer un ID qui n'existe pas
    lève bien l'erreur TaskNotFoundError au lieu d'un IndexError.
    """
    mgr = TaskManager()
    mgr.create_task("Tache id=1")
    
    with pytest.raises(TaskNotFoundError) as exc_info:
        mgr.delete_task(999)
        
    assert "999" in str(exc_info.value)
