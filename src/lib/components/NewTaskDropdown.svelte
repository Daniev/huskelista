<script lang="ts">
	import { list, user } from '$lib/stores';
	import type { Task } from '$lib/types/tasks';
	import Button from './Button.svelte';
	import Dropdown from './Dropdown.svelte';
	import UserSelector from './UserSelector.svelte';

	let isDropdownOpen = false;
	let taskTitle = '';
	let taskDescription = '';
	let selectedUser = $user;

	const createTask = () => {
		const newTask: Task = {
			id: Math.random(),
			title: taskTitle,
			description: taskDescription,
			assignee: selectedUser,
			completed: false
		};
		const taskList = $list;
		taskList.push(newTask);
		list.set(taskList);
		// reset the form
		taskTitle = '';
		taskDescription = '';
		selectedUser = $user;

		isDropdownOpen = !isDropdownOpen;
	};
</script>

<Dropdown bind:isOpen={isDropdownOpen}>
	<Button callToAction slot="button">Ny</Button>
	<div class="dropdown-content" slot="content">
		<h3>Lag nytt gjøremål</h3>
		<!-- svelte-ignore a11y-autofocus because I want autofocus -->
		<input
			class="title-input"
			type="text"
			placeholder="Gjøremål"
			bind:value={taskTitle}
			autofocus
		/>

		<textarea
			class="description-input"
			placeholder="Beskrivelse (valgfritt)"
			bind:value={taskDescription}
		/>

		<div class="center">
			<span>Ansvarlig:</span>
			<UserSelector bind:selectedUser />
		</div>
		<Button callToAction on:click={createTask}>Opprett gjøremål</Button>
	</div>
</Dropdown>

<style lang="scss">
	.dropdown-content {
		display: block;
		width: 15rem;
		padding: var(--pa);
		h3 {
			font-size: var(--fo-medium);
			font-weight: 400;
			margin: 0 0 var(--ma) 0;
		}
		input,
		textarea {
			border-radius: var(--bo);
			font-size: var(--fo-small);
			padding: var(--pa-mini) var(--pa-small);
			height: 2rem;
			width: 13rem;
			background-color: var(--light-blue-trans);
			&::placeholder {
				color: var(--dark-grey);
			}
			color: var(--text-color);
			border-style: none;
			&:focus-visible {
				outline: none;
			}
		}

		.description-input {
			margin-top: var(--ma-medium);
			height: 5rem;
		}
		.center {
			display: flex;
			justify-content: flex-start;
			align-items: center;
		}
	}
</style>
