<script lang="ts">
	import ListEntry from '$lib/components/ListEntry.svelte';
	import TaskBox from '$lib/components/taskBox.svelte';
	import { user } from '$lib/stores/user';

	import { list } from '$lib/stores/lists';
	import type { Task } from '$lib/types/tasks';

	const todo: Task[] = [];
	const done: Task[] = [];

	function sortTaskList(list: Task[]) {
		list.forEach((task) => {
			if (task.completed) {
				done.push(task);
			} else {
				todo.push(task);
			}
		});
	}

	$: sortTaskList($list);
</script>

<div class=" center">
	<h1 class="centerDown">Velkommen {$user}</h1>

	<section>
		<TaskBox title="Gjøremål">
			<div slot="taskList">
				{#each todo as task}
					<ListEntry {task} />
				{/each}
			</div>
			<div slot="bottom">
				<button class="new">Ny</button>
			</div>
		</TaskBox>

		<TaskBox title="Fullført">
			<div slot="taskList">
				{#each done as task}
					<ListEntry color="lightgrey" {task} />
				{/each}
			</div>
		</TaskBox>
	</section>
</div>

<style lang="scss">
	section {
		height: 100vh;
		width: 100vw;
		display: flex;
		flex-direction: row;
		justify-content: space-around;
	}

	.new {
		border-radius: $border-lg;
		height: 2rem;
		width: 2rem;
		background-color: $button-color;
		color: $white;
		&:hover {
			background-color: $button-hover-color;
		}
	}
</style>
