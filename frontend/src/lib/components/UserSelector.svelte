<script lang="ts">
	import type { User } from '$lib/types/user';
	import { users } from '$lib/stores';
	import Icon from './Icon.svelte';

	export let selectedUser: User;
	const changeUser = (user: User) => {
		selectedUser = user;
	};
</script>

<section>
	{#each $users as user}
		<div
			class:selected={user === selectedUser}
			class={user.toLowerCase()}
			on:click={() => changeUser(user)}
			on:keypress={() => changeUser(user)}
			role="button"
			tabindex="0"
		>
			<Icon iconName="zondicons:user" />
			{user}
		</div>
	{/each}
</section>

<style lang="scss">
	section {
		display: flex;
		justify-content: space-evenly;
		align-items: center;
		width: 12.6rem;
	}
	div {
		background-color: var(--light-grey);
		border-radius: var(--bo);
		padding: var(--pa) var(--pa-small);
		cursor: pointer;
		justify-content: center;
		align-items: center;

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
			color: var(--white-text-color);
		}
		&.mia {
			background-color: var(--mia-profile-color);
			color: var(--white-text-color);
		}
	}
</style>
