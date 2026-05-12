"""PARTIE 3 - Tests FONCTIONNELS.

On verifie un comportement metier coherent du point de vue de l'utilisateur.
Pas de details d'implementation : seuls les RESULTATS observables comptent.
"""

import pytest
from src.task_manager import TaskManager
from src.exceptions import TaskNotFoundError


@pytest.mark.fonctionnel
def test_creer_une_tache_la_rend_listable():
    mgr = TaskManager()
    mgr.create_task("Aller a la salle de sport")
    titres = [t.title for t in mgr.list_tasks()]
    assert "Aller a la salle de sport" in titres


@pytest.mark.fonctionnel
def test_marquer_done_change_les_stats():
    mgr = TaskManager()
    mgr.create_task("A faire")
    mgr.create_task("Aussi a faire")
    mgr.mark_done(1)
    stats = mgr.get_stats()
    assert stats["done"] == 1
    assert stats["todo"] == 1


@pytest.mark.fonctionnel
def test_liste_triee_par_priorite_descendante(manager_with_3_tasks):
    triees = manager_with_3_tasks.list_tasks(sort_by="priority")
    priorites = [t.priority for t in triees]
    assert priorites == ["high", "medium", "low"]


@pytest.mark.fonctionnel
def test_get_task_inexistante_leve_une_erreur_explicite(empty_manager):
    with pytest.raises(TaskNotFoundError):
        empty_manager.get_task(999)


@pytest.mark.fonctionnel
def test_filtre_done_nexclut_aucune_tache_todo_ou_doing():
    # Arrange — on crée un mix de statuts pour rendre le filtre discriminant
    mgr = TaskManager()
    t1 = mgr.create_task("Tache todo")          # statut : todo
    t2 = mgr.create_task("Tache doing")         # statut : doing
    t3 = mgr.create_task("Tache done")          # statut : done
    mgr.update_task(t2.id, status="doing")
    mgr.update_task(t3.id, status="done")

    # Act
    taches_done = mgr.list_tasks(status_filter="done")

    # Assert — aucune tâche retournée ne doit avoir le statut 'todo' ou 'doing'
    statuts_obtenus = {t.status for t in taches_done}
    assert "todo" not in statuts_obtenus
    assert "doing" not in statuts_obtenus
    assert all(t.status == "done" for t in taches_done)
