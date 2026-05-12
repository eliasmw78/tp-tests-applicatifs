"""PARTIE 3 - Tests d'INTEGRATION.

On teste que plusieurs modules cooperent correctement.
Ici : task_manager + storage (persistance JSON sur disque).
"""

import pytest
from src.task_manager import TaskManager
from src.storage import save_tasks, load_tasks


@pytest.mark.integration
def test_sauvegarder_puis_recharger_preserve_les_taches(tmp_path):
    fichier = tmp_path / "taches.json"
    mgr = TaskManager()
    mgr.create_task("Tache A", priority="low")
    mgr.create_task("Tache B", priority="high")

    save_tasks(str(fichier), mgr.list_tasks(sort_by="id"))

    rechargees = load_tasks(str(fichier))
    assert len(rechargees) == 2
    assert rechargees[0].title == "Tache A"
    assert rechargees[1].priority == "high"


@pytest.mark.integration
def test_chargement_depuis_fichier_inexistant_renvoie_liste_vide(tmp_path):
    fichier = tmp_path / "inexistant.json"
    assert load_tasks(str(fichier)) == []


@pytest.mark.integration
def test_modification_statut_persistee_sur_disque(tmp_path):
    """Cycle complet : création → modification → sauvegarde → rechargement."""
    # Arrange
    fichier = tmp_path / "taches.json"
    mgr1 = TaskManager()
    tache = mgr1.create_task("Rediger le rapport")
    mgr1.update_task(tache.id, status="doing")

    # Act — sauvegarde puis rechargement dans un manager vierge
    save_tasks(str(fichier), mgr1.list_tasks(sort_by="id"))
    mgr2 = TaskManager()
    mgr2.replace_all(load_tasks(str(fichier)))
    tache_rechargee = mgr2.get_task(tache.id)

    # Assert — le statut 'doing' a survécu au cycle disque
    assert tache_rechargee.status == "doing"


@pytest.mark.integration
def test_replace_all_remet_le_compteur_id_a_la_bonne_valeur(tmp_path):
    fichier = tmp_path / "taches.json"
    mgr1 = TaskManager()
    mgr1.create_task("Existante")
    save_tasks(str(fichier), mgr1.list_tasks(sort_by="id"))

    mgr2 = TaskManager()
    mgr2.replace_all(load_tasks(str(fichier)))
    nouvelle = mgr2.create_task("Suivante")
    assert nouvelle.id == 2
