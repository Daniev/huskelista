<script lang="ts">
	import type { Task } from '$lib/types/tasks';

	export let color: 'blue' | 'green' | 'yellow' = 'blue';
	export let task: Task;

	function handleClick() {
		task.completed = !task.completed;
		task = task;
	}
</script>

<button class={color} on:click={handleClick}>
	<p>{task.title}</p>
</button>

<style lang="scss">
	button {
		margin: 0;
		margin-bottom: 5px;
		outline: none;
		text-align: left;
		border-radius: 20px 20px 20px 0;
	}
	p {
		text-decoration: none;
		margin: 0;
		width: 18.5rem;
		height: 1rem;
		padding: $padding-sm;
	}

	.blue {
		background-color: var(--light-blue-trans);
		color: var(--text-color);

		&:hover {
			background-color: var(--light-blue);
		}
	}

	.green {
		background-color: var(--matt-green);
		color: var(--white-text-color);

		&:hover {
			background-color: var(--green);
		}
	}

	.yellow {
		background-color: var(--yellow-trans);
		color: var(--text-color);
		&:hover {
			background-color: var(--yellow);
		}
	}
</style>
