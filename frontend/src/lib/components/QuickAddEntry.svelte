<script lang="ts">
	import type { QuickTask, Task } from '$lib/types/tasks';
	import axios from 'axios';
	import ListEntry from './ListEntry.svelte';
	import { TASK_URL } from '$lib/api/urls';
	import { list, user } from '$lib/stores';

	export let task: QuickTask;
	export let isMia: boolean;

	const newTask: Task = {
		title: task,
		complete: false,
		assignee: $user
	};

	const handleClick = async () => {
		// quick add task to list.
		console.debug('Quick adding task!');
		await axios.post(`${TASK_URL}`, newTask).catch((error) => console.warn(error));
		$list = [...$list, newTask];
	};
</script>

<ListEntry task={newTask} classes={isMia ? 'mia' : 'daniel'} {handleClick} />
