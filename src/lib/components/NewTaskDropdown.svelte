<script lang="ts">
	import { list, user } from '$lib/stores';
	import type { Task } from '$lib/types/tasks';
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

		isDropdownOpen = !isDropdownOpen;
	};
</script>

<Dropdown bind:isOpen={isDropdownOpen}>
	<button class="new" slot="button">Ny</button>
	<div class="dropdown-content" slot="content">
		<h2>Lag nytt gjøremål</h2>
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

		<button class="create" on:click={createTask}>Opprett gjøremål</button>
	</div>
</Dropdown>

<style lang="scss">
	.dropdown-content {
		display: block;
		width: 15rem;
		padding: $padding-sm;
		h2 {
			font-size: 20px;
		}
		input,
		textarea {
			border-radius: 1rem;
			font-size: 1rem;
			padding: 0.2rem 0.75rem;
			height: 2rem;
			width: 13rem;
			background-color: var(--blue);
			&::placeholder {
				color: var(--light-grey);
			}
			color: var(--white-text-color);
			border-width: 1px;
			border-style: none;
			&:focus-visible {
				outline: none;
			}
		}

		.create {
			padding: $padding-sm;
			margin: 0 1rem 0 0;
			font-size: 1.1rem;
			background-color: var(--button-color);
			margin: 0.6rem 0 0;
			color: var(--white-text-color);
			&:hover {
				background-color: var(--button-hover-color);
			}
		}

		.description-input {
			margin-top: 1rem;
			height: 5rem;
		}
		.center {
			display: flex;
			padding: 0 0.6rem;
			justify-content: flex-start;
			align-items: center;
		}
	}
	.new {
		border-radius: $border-lg;
		height: 3rem;
		width: 3rem;
		background-color: var(--button-color);
		color: var(--white-text-color);
		margin: 0.6rem 0.6rem 0 0;

		&:hover {
			background-color: var(--button-hover-color);
		}
	}
</style>
