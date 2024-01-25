<script lang="ts">
	import type { Task } from '$lib/types/tasks';
	import Icon from '$lib/components/Icon.svelte';
	import axios from 'axios';
	import { TASK_URL } from '$lib/api/urls';

	export let classes: 'mia' | 'completed' | 'daniel' = 'completed';
	export let task: Task;

	async function handleClick() {
		task.complete = !task.complete;
		task = task;
		await axios.put(`${TASK_URL}${task.slug}`, task).catch((error) => console.warn(error));
	}
</script>

<button class={classes} on:click={handleClick}>
	<p>{task.title}</p>
	<Icon iconName="zondicons:checkmark-outline" />
</button>

<style lang="scss">
	button {
		margin: var(--ma);
		display: flex;
		justify-content: center;
		align-items: center;
		outline: none;
		text-align: left;
		border-radius: var(--bo) var(--bo) var(--bo) 0;
		--icon-fill-color: var(--green);
	}
	p {
		text-decoration: none;
		margin: 0;
		width: 18.5rem;
		height: 1rem;
		padding: var(--pa-small);
	}

	.daniel {
		background-image: var(--gradient-blue);
		color: var(--text-color);

		&:hover {
			background-image: none;
			background-color: var(--green);
			color: var(--white-text-color);
			font-weight: 600;
			--icon-fill-color: var(--white-text-color);
		}
	}

	.completed {
		background-color: var(--light-grey);
		color: var(--text-color);
		border: var(--border-small);

		&:hover {
			background-color: var(--new-blue);
			color: var(--white-text-color);
		}
	}

	.mia {
		background-image: var(--gradient-blue);
		color: var(--text-color);
		&:hover {
			background-image: none;
			background-color: var(--mia-highlight-color);
			color: var(--white-text-color);
			--icon-fill-color: var(--white-text-color);
			font-weight: 600;
		}
	}
</style>
