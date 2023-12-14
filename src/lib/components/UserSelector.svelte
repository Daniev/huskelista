<script lang="ts">
	import type { User } from '$lib/types/user';
	import { users } from '$lib/stores';
	import Dropdown from './Dropdown.svelte';

	export let selectedUser: User;

	let isOpen = false;

	const changeUser = (user: User) => {
		selectedUser = user;
	};
</script>

<Dropdown bind:isOpen placeBelow disableAnimation>
	<button class="{selectedUser.toLowerCase()} clicker" slot="button">{selectedUser}</button>

	<div slot="content" class="content">
		{#each $users as user}
			<button class="user" on:click={() => changeUser(user)}>{user}</button>
		{/each}
	</div>
</Dropdown>

<style lang="scss">
	.daniel {
		background-color: var(--daniel-profile-color);
		color: var(--white);
	}
	.mia {
		background-color: var(--mia-profile-color);
		color: var(--text-color);
	}
	.clicker {
		padding: var(--pa-small) var(--pa);
		width: 5rem;
		margin: var(--ma) var(--ma-big);
	}

	.content {
		padding: var(--pa-small) 0;
		background-color: var(--white);
		border-radius: var(--bo-small);
	}
	.user {
		display: block;
		border-radius: 0;
		text-align: left;
		padding: var(--pa-mini) var(--pa);
		background-color: transparent;
		width: 5rem;
		margin: 0;
		&:hover {
			background-color: var(--light-grey);
		}
	}
</style>
