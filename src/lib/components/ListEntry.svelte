<script lang="ts">
	import type { Task } from '$lib/types/tasks';

	export let classes: 'mia' | 'completed' | 'daniel' = 'completed';
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
		background-image: var(--gradient-blue);
		color: var(--text-color);

		&:hover {
			background-image: none;
			background-color: var(--green);
			color: var(--white-text-color);
			font-weight: 600;
		}
	}

	.completed {
		background-color: var(--light-grey);
		color: var(--text-color);
		border: var(--border-small);

		&:hover {
			background-color: var(--green);
		}
	}

	.mia {
		background-image: var(--gradient-blue);
		color: var(--text-color);
		&:hover {
			background-image: none;
			background-color: var(--mia-highlight-color);
			font-weight: 600;
		}
	}
</style>
