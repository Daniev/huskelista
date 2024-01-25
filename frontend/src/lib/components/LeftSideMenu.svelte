<script lang="ts">
	import Dropdown from './Dropdown.svelte';
	import Icon from './Icon.svelte';

	let isOpen = false;
</script>

<Dropdown isSideMenu disableClickOutside bind:isOpen>
	<div class="button-section" class:isOpen slot="button">
		<Icon iconName="zondicons:menu" height="30px" />
	</div>

	<div class="content" slot="content" />
</Dropdown>

<style lang="scss">
	.button-section {
		padding: var(--pa-small);
		height: 2.5rem;
		width: 4rem;
		display: flex;
		justify-content: center;
		align-items: center;
		margin: 0;
		cursor: pointer;

		&:hover {
			background-color: var(--green);
			color: var(--white-text-color);
		}
	}
	.isOpen {
		background-color: var(--green);
		// color: var(--white-text-color);
	}

	.content {
		padding: var(--pa-small);
		height: 100svh;
		width: 20rem;
	}
</style>
