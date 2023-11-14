<script lang="ts">
	import type { DropdownColor } from '$lib/types/styleOptions';
	import { onMount } from 'svelte';

	let dropdownElement: HTMLElement;

	export let isOpen = false;
	export let color: DropdownColor = 'blue';

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
		<section class="dropdown-section {color}">
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
		z-index: 2;
		border-radius: $border-sm;
		padding: $padding-sm;

		&.blue {
			background-color: var(--dropdown-bg);
		}
		&.lightgrey {
			background-color: #a0acad;
		}
		&.green {
			background-color: #49a078;
		}
	}
</style>
