<script lang="ts">
	import { onMount } from 'svelte';

	let dropdownElement: HTMLElement;

	export let isOpen = false;

	onMount(() => {
		document.body.addEventListener('click', handleClickOutside);
	});

	function handleClickOutside(event: Event) {
		if (
			event.target instanceof Element &&
			!dropdownElement.contains(event.target) &&
			!event.defaultPrevented
		) {
			isOpen = false;
		}
	}

	function toggleDropdown() {
		isOpen = !isOpen;
	}
</script>

<div bind:this={dropdownElement}>
	<section>
		<div on:click={toggleDropdown} on:keydown={toggleDropdown} role="button" tabindex="0">
			<slot name="button">
				<button>Open</button>
			</slot>
		</div>
	</section>
	{#if isOpen}
		<section class="dropdown-section">
			<slot name="content">
				<span>Dropdown content</span>
			</slot>
		</section>
	{/if}
</div>

<style lang="scss">
	.button-section {
		position: relative;
	}
	.dropdown-section {
		position: absolute;
		top: 3;
		left: 2;
		transform: translate(-90%, -130%);
		background-color: var(--dropdown-bg);
		z-index: 2;
		border-radius: $border-sm;
		padding: $padding-sm;
	}
</style>
