<script lang="ts">
	import axios from 'axios';
	import Button from './Button.svelte';
	import Icon from './Icon.svelte';
	import { TASK_URL } from '$lib/api/urls';
	import { list } from '$lib/stores';

	export let taskSlug: string;

	const trashTask = async () => {
		await axios.delete(`${TASK_URL}${taskSlug}`).catch((error) => console.warn(error));
		console.log('Trashing the task', taskSlug);
		list.update((tasks) => tasks.filter((task) => task.slug !== taskSlug));
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
