<script lang="ts">
	import { onMount } from 'svelte';

	let dropdownElement: HTMLElement;

	/** export value to let the parent know if the dropdown is open */
	export let isOpen = false;
	/** Place the dropdown below instaed of above*/
	export let placeBelow = false;

	onMount(() => {
		document.body.addEventListener('click', handleClickOutside);
	});

	function handleClickOutside(event: Event) {
		if (!dropdownElement) {
			return;
		}
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
		<section class="dropdown-section" class:placeBelow>
			<slot name="content">
				<span>Dropdown content</span>
			</slot>
		</section>
	{/if}
</div>

<style lang="scss">
	.dropdown-section {
		position: absolute;
		top: 3;
		left: 2;
		transform: translate(-90%, -130%);
		z-index: 2;
		border-radius: $border-sm;
		background-color: var(--dropdown-bg);
	}
	.placeBelow {
		top: -1;
		right: 5;
		transform: translate(15%, -30%);
	}
</style>
