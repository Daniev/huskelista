<script lang="ts">
	import type { Task } from '$lib/types/tasks';
	import axios from 'axios';
	import ListEntry from './ListEntry.svelte';
	import { TASK_URL } from '$lib/api/urls';
	import { list } from '$lib/stores';

	export let task: Task;
	export let isMia: boolean;

	const handleClick = async () => {
		// quick add task to list.
		console.debug('Quick adding task!');
		await axios.post(`${TASK_URL}`, task).catch((error) => console.warn(error));
		$list = [...$list, task];
	};
</script>

<ListEntry {task} classes={isMia ? 'mia' : 'daniel'} {handleClick} />
