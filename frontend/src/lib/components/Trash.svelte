<script lang="ts">
	import Button from './Button.svelte';
	import Icon from './Icon.svelte';

	export let taskSlug: string;

	const trashTask = () => {
		console.log('Trashing the task', taskSlug);
	};

	const trashColor = 'color: var(--icon-hover, var(--red));';
</script>

<span>
	<Button on:click={trashTask}>
		<Icon iconName="zondicons:trash" style={trashColor} height="22px" /></Button
	>
</span>

<style lang="scss">
	span {
		--button-background: none;
		--hover-color: var(--red);
		&:hover {
			--icon-hover: var(--white-text-color);
		}
		margin: 0;
	}
</style>
