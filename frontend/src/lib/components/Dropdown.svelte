<script lang="ts">
	import { onMount } from 'svelte';
	import { fly } from 'svelte/transition';

	let dropdownElement: HTMLElement;

	/** export value to let the parent know if the dropdown is open */
	export let isOpen = false;
	/** Place the dropdown below instaed of above*/
	export let placeBelow = false;

	/**styles content as a side menu*/
	export let isSideMenu = false;

	/** disables click outside*/
	export let disableClickOutside = false;

	/** Disable popup animation*/
	export let disableAnimation = false;

	onMount(() => {
		document.body.addEventListener('click', handleClickOutside);
	});

	function handleClickOutside(event: Event) {
		if (!dropdownElement) {
			return;
		}
		if (disableClickOutside) {
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

	const transitionSettings = disableAnimation ? {} : { y: 100, duration: 200 };
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
		<section
			class="dropdown-section"
			class:placeBelow
			class:isSideMenu
			transition:fly={transitionSettings}
		>
			<slot name="content">
				<span>Dropdown content</span>
			</slot>
		</section>
	{/if}
</div>

<style lang="scss">
	.dropdown-section {
		position: absolute;
		transform: translate(-90%, -115%);
		z-index: 2;
		border-radius: var(--bo);
		border: var(--border-small);
		background-color: var(--dropdown-bg);
	}
	.placeBelow {
		top: -1;
		right: 5;
		transform: translate(15%, -30%);
	}
	.isSideMenu {
		top: 0;
		right: 5;
		transform: translate(0%, 6.8%);
		border-radius: 0;
	}
</style>
