import type { User } from './user';

export interface Task {
	slug: string;
	title: string;
	assignee: User;
	completed: boolean;
}
