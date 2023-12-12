<script lang="ts">
	import type { Task } from '$lib/types/tasks';

	export let classes: 'mia' | 'green' | 'daniel' = 'green';
	export let task: Task;

	function handleClick() {
		task.completed = !task.completed;
		task = task;
	}
</script>

<button class={classes} on:click={handleClick}>
	<p>{task.title}</p>
</button>

<style lang="scss">
	button {
		margin: 0;
		margin-bottom: var(--ma);
		outline: none;
		text-align: left;
		border-radius: var(--bo) var(--bo) var(--bo) 0;
	}
	p {
		text-decoration: none;
		margin: 0;
		width: 18.5rem;
		height: 1rem;
		padding: var(--pa-small);
	}

	.daniel {
		background-color: var(--daniel-task-color);
		color: var(--text-color);

		&:hover {
			background-color: var(--daniel-highlight-color);
		}
	}

	.green {
		background-color: var(--matt-green);
		color: var(--white-text-color);

		&:hover {
			background-color: var(--green);
		}
	}

	.mia {
		background-color: var(--mia-task-color);
		color: var(--text-color);
		&:hover {
			background-color: var(--mia-highlight-color);
		}
	}
</style>
