/**
 * Gestionnaire de taches (version STARTER).
 *
 * ATTENTION ELEVES : ce module contient au moins UN BUG volontaire (deleteTask).
 * Vous le decouvrirez en Partie 4 (regression) du TP.
 */

import { Task } from "./task.js";
import { TaskNotFoundError } from "./errors.js";
import { validateStatus, type Priority, type Status } from "./validators.js";

const PRIORITY_WEIGHT: Record<Priority, number> = { low: 1, medium: 2, high: 3 };

export class TaskManager {
  private tasks: Task[] = [];
  private nextId = 1;

  createTask(params: {
    title: string;
    description?: string;
    priority?: Priority;
    dueDate?: string | null;
  }): Task {
    const task = new Task({
      id: this.nextId,
      title: params.title,
      description: params.description,
      priority: params.priority ?? "medium",
      status: "todo",
      dueDate: params.dueDate ?? null,
    });
    this.tasks.push(task);
    this.nextId += 1;
    return task;
  }

  listTasks(options?: {
    statusFilter?: Status;
    sortBy?: "priority" | "id" | "dueDate";
  }): Task[] {
    let result = [...this.tasks];
    if (options?.statusFilter !== undefined) {
      validateStatus(options.statusFilter);
      result = result.filter((t) => t.status === options.statusFilter);
    }
    const sortBy = options?.sortBy ?? "priority";
    if (sortBy === "priority") {
      result.sort((a, b) => PRIORITY_WEIGHT[b.priority] - PRIORITY_WEIGHT[a.priority]);
    } else if (sortBy === "id") {
      result.sort((a, b) => a.id - b.id);
    } else if (sortBy === "dueDate") {
      result.sort((a, b) => (a.dueDate ?? "9999").localeCompare(b.dueDate ?? "9999"));
    }
    return result;
  }

  getTask(taskId: number): Task {
    const task = this.tasks.find((t) => t.id === taskId);
    if (!task) throw new TaskNotFoundError(`Aucune tache trouvee avec id=${taskId}.`);
    return task;
  }

  markDone(taskId: number): Task {
    const task = this.getTask(taskId);
    task.status = "done";
    return task;
  }

  deleteTask(taskId: number): boolean {
    const initialLength = this.tasks.length;
    this.tasks = this.tasks.filter((t) => t.id !== taskId);
    
    if (this.tasks.length === initialLength) {
      throw new TaskNotFoundError(`Aucune tache trouvee avec id=${taskId}.`);
    }
    return true;
  }

  getStats(): { todo: number; doing: number; done: number; total: number } {
    const stats = { todo: 0, doing: 0, done: 0, total: this.tasks.length };
    for (const t of this.tasks) {
      stats[t.status] += 1;
    }
    return stats;
  }

  replaceAll(tasks: Task[]): void {
    this.tasks = [...tasks];
    this.nextId = tasks.length > 0 ? Math.max(...tasks.map((t) => t.id)) + 1 : 1;
  }
}
