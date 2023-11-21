<script lang="ts">
	import { user, users } from '$lib/stores/user';
	import type { User } from '$lib/types/user';
	import Dropdown from './Dropdown.svelte';

	export let selectedUser: User;
	let isOpen = false;

	const changeUser = (user: User) => {
		selectedUser = user;
	};
</script>

<Dropdown bind:isOpen placeBelow>
	<button class="clicker" slot="button">{selectedUser}</button>

	<div slot="content" class="content">
		{#each $users as user}
			<button class="user" on:click={() => changeUser(user)}>{user}</button>
		{/each}
	</div>
</Dropdown>

<style lang="scss">
	.clicker {
		padding: 0.5rem;
		width: 6rem;
	}

	.content {
		padding: 0.5rem 0;
		background-color: var(--subtle-button-color);
		border-radius: 0 0 0.7rem;
	}
	.user {
		display: block;
		border-radius: 0;
		text-align: left;
		padding: 0.3rem 0.8rem;
		background-color: transparent;
		width: 6rem;
		height: 1.2rem;
		margin: 0;
		&:hover {
			background-color: var(--subtle-button-hover-color);
		}
	}
</style>
