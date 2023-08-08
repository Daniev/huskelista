<script lang="ts">
	export let color: 'grey' | 'lightgrey' = 'grey';
</script>

<button class={color}>
	<p><slot /></p>
</button>

<style lang="scss">
	button {
		margin: 0;
		margin-bottom: 3px;
		outline: none;
		text-align: left;
		border-radius: 20px 20px 20px 0;
	}
	p {
		text-decoration: none;
		margin: 0;
		width: 18.5rem;
		height: 1rem;
		padding: $padding-sm;
	}

	.grey {
		background-color: $grey1;
		color: $white;

		&:hover {
			background-color: $grey;
		}
	}

	.lightgrey {
		background-color: $grey2;
		color: $white;

		&:hover {
			background-color: $grey1;
		}
	}
</style>
