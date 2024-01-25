<script lang="ts">
	import Dropdown from './Dropdown.svelte';
	import Icon from './Icon.svelte';
	import ListEntry from './ListEntry.svelte';
	import TaskBox from './taskBox.svelte';

	import { user } from '$lib/stores';

	const task = {
		title: 'test',
		complete: false,
		assignee: $user
	};

	const isMia = $user === 'Mia';

	let isOpen = false;
</script>

<Dropdown isSideMenu disableClickOutside bind:isOpen>
	<div class="button-section" class:isOpen slot="button">
		<Icon iconName="zondicons:menu" height="30px" />
	</div>

	<div class="content" slot="content">
		<div class="quick-add">
			<TaskBox title="Quick Add">
				<div slot="taskList">
					<ListEntry {task} classes={isMia ? 'mia' : 'daniel'} />
				</div>
			</TaskBox>
		</div>
	</div>
</Dropdown>

<style lang="scss">
	.button-section {
		padding: var(--pa-small);
		height: 2.6rem;
		width: 4rem;
		display: flex;
		justify-content: center;
		align-items: center;
		margin: 0;
		cursor: pointer;

		&:hover {
			background-color: var(--white-darker);
			color: var(--white-text-color);
			--icon-fill-color: var(--text-color);
		}
	}
	.isOpen {
		background-color: var(--white-darker);
	}

	.content {
		padding: var(--pa-small);
		height: 100svh;
		width: 20rem;
		background-color: var(--dark-green);
	}
	.quick-add {
		height: 20rem;
		width: 20rem;
		--list-width: 15rem;
		--box-height: 10rem;
		--box-color: none;
		--box-border: none;

		border-bottom: solid 1px var(--matt-green);
	}
</style>
