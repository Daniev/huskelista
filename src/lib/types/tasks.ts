import type { User } from "./user";

export interface Task {
    id: number;
    title: string;
    description: string;
    assignee: User;
    completed: boolean;
}
