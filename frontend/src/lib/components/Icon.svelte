<script lang="ts">
	/** Use to render icons from iconify!
	 * Manipulate the colors by assigning the icon css variables
	 */
	import Icon from '@iconify/svelte';

	/** defaults to checkmark*/
	export let iconName = 'zondicons:checkmark-outline';
	/** Dont include the brackets in the style prop */
	export let style = 'color: var(--icon-fill-color); background-color: var(--icon-bg-color)';

	/** a valid string css height value*/
	export let height = '24px';
</script>

<Icon icon={iconName} {style} {height} />
