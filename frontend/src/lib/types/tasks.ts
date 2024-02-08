import type { User } from './user';

export interface Task {
	slug?: string;
	title: string;
	assignee: User;
	complete: boolean;
}

/** The quick task as it comes from the backend (Title only) */
export type QuickTask = string;
