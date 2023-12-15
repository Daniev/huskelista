<script lang="ts">
	import type { User } from '$lib/types/user';
	import { users } from '$lib/stores';
	import Dropdown from './Dropdown.svelte';
	import Icon from './Icon.svelte';

	export let selectedUser: User;
	const changeUser = (user: User) => {
		selectedUser = user;
	};
</script>

<div class="content">
	{#each $users as user}
		<button
			class:selected={user === selectedUser}
			class={user.toLowerCase()}
			on:click={() => changeUser(user)}
		>
			<Icon iconName="zondicons:user" />
			{user}</button
		>
	{/each}
</div>

<style lang="scss">
	button {
		padding: var(--pa-small);

		&:hover,
		&:focus {
			background-color: var(--new-blue);
		}
	}

	.daniel {
		margin: var(--ma) 0 var(--ma) var(--ma-big);
	}
	.selected {
		&.daniel {
			background-color: var(--daniel-profile-color);
			color: var(--white);
		}
		&.mia {
			background-color: var(--mia-profile-color);
			color: var(--text-color);
		}
	}
</style>
