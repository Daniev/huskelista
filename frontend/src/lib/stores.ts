import type { Task } from '$lib/types/tasks';
import type { User } from '$lib/types/user';
import { writable } from 'svelte/store';

const defaultList = [
	{
		id: 1,
		title: 'vask bad',
		description: 'vask bad',
		assignee: 'Mia' as User,
		complete: false
	},
	{
		id: 2,
		title: 'klesvask',
		description: 'klesvask',
		assignee: 'Daniel' as User,
		complete: false
	},
	{
		id: 3,
		title: 'støvsuger og tørke støv',
		description: 'støvsuger og tørke støv',
		assignee: 'Mia' as User,
		complete: false
	},
	{
		id: 4,
		title: 'sofa',
		description: 'sofa',
		assignee: 'Daniel' as User,
		complete: true
	}
];

export const user = writable<User>('unknown');
export const users = writable<User[]>(['Mia', 'Daniel']);
export const list = writable<Task[]>(defaultList);
