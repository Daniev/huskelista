<script>
	/** General button component for call to action buttons and other buttons*/

	export let callToAction = false;
	export let title = '';
</script>

<button class="button" class:call-to-action={callToAction} on:click {title}>
	<slot>Text Here</slot>
</button>

<style lang="scss">
	.button {
		--_button-color: var(--button-background, var(--light-grey));
		background-color: var(--_button-color);
		border-radius: var(--bo-big);
		color: var(--text-color);
		font-size: var(--fo-small);
		padding: var(--pa-small) var(--pa);
		margin: var(--ma);
		&:hover {
			background-color: var(--green);
			color: var(--white-text-color);
		}
	}

	.call-to-action {
		--button-background: var(--new-blue);
	}
</style>
