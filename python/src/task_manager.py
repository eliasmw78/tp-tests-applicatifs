"""Gestionnaire de taches : logique metier.

ATTENTION ELEVES : ce module contient au moins UN BUG volontaire.
Vous devez le decouvrir en Partie 4 (regression) en ecrivant un test qui echoue,
puis le corriger, puis garder le test pour blinder le code.
"""

from .task import Task
from .exceptions import TaskNotFoundError
from .validators import validate_status

PRIORITY_WEIGHT = {"low": 1, "medium": 2, "high": 3}


class TaskManager:
    def __init__(self):
        self._tasks = []
        self._next_id = 1

    def create_task(self, title, description="", priority="medium", due_date=None):
        task = Task(
            id=self._next_id,
            title=title,
            description=description,
            priority=priority,
            status="todo",
            due_date=due_date,
        )
        self._tasks.append(task)
        self._next_id += 1
        return task

    def list_tasks(self, status_filter=None, sort_by="priority"):
        result = list(self._tasks)
        if status_filter is not None:
            validate_status(status_filter)
            result = [t for t in result if t.status == status_filter]
        if sort_by == "priority":
            result.sort(key=lambda t: PRIORITY_WEIGHT[t.priority], reverse=True)
        elif sort_by == "id":
            result.sort(key=lambda t: t.id)
        elif sort_by == "due_date":
            result.sort(key=lambda t: (t.due_date is None, t.due_date or ""))
        return result

    def get_task(self, task_id):
        for task in self._tasks:
            if task.id == task_id:
                return task
        raise TaskNotFoundError(f"Aucune tache trouvee avec id={task_id}.")

    def update_task(self, task_id, **fields):
        task = self.get_task(task_id)
        for key, value in fields.items():
            if hasattr(task, key):
                setattr(task, key, value)
        # Revalidation complete pour garantir la coherence
        return Task(
            id=task.id,
            title=task.title,
            description=task.description,
            priority=task.priority,
            status=task.status,
            due_date=task.due_date,
            created_at=task.created_at,
        )

    def mark_done(self, task_id):
        task = self.get_task(task_id)
        task.status = "done"
        return task

    def delete_task(self, task_id):
        longueur_initiale = len(self._tasks)
        self._tasks = [t for t in self._tasks if t.id != task_id]
        
        if len(self._tasks) == longueur_initiale:
            raise TaskNotFoundError(f"Aucune tache trouvee avec id={task_id}.")
            
        return True

    def get_stats(self):
        stats = {"todo": 0, "doing": 0, "done": 0, "total": len(self._tasks)}
        for task in self._tasks:
            stats[task.status] += 1
        return stats

    def replace_all(self, tasks):
        """Recharge l'integralite des taches depuis une liste (utile au chargement disque)."""
        self._tasks = list(tasks)
        self._next_id = max((t.id for t in self._tasks), default=0) + 1
