<script>
	/** General button component for call to action buttons and other buttons*/
	import { user } from '$lib/stores';

	export let callToAction = false;
	export let title = '';

	let isUserMia = false;
	$: isUserMia = $user === 'Mia';
</script>

<button class="button" class:call-to-action={callToAction} class:mia={isUserMia} on:click {title}>
	<slot>Text Here</slot>
</button>

<style lang="scss">
	.button {
		--_button-color: var(--button-background, var(--light-grey));
		--_button-text: var(--button-text, var(--text-color));
		--_hover-color: var(--hover-color, var(--green));
		--_hover-text: var(--hover-text, var(--white-text-color));
		--_border-radius: var(--button-border-radius, var(--bo-big));
		background-color: var(--_button-color);
		border-radius: var(--_border-radius);
		display: flex;
		align-items: center;
		justify-content: center;
		color: var(--_button-text);
		font-size: var(--fo-small);
		padding: var(--pa-small) var(--pa);
		margin: var(--ma) 0;
		&:hover,
		&:focus-visible {
			background-color: var(--_hover-color);
			color: var(--_hover-text);
			font-weight: 500;
		}
	}

	.call-to-action {
		--button-background: var(--new-blue);
	}
	.mia {
		--_hover-color: var(--hover-color, var(--mia-profile-color));
		--_hover-text: var(--hover-text, var(--white-text-color));
	}
</style>
