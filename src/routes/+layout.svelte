<slot />

<style lang="scss">
	:global(h1) {
		font-size: $font-xl;
	}

	:global(h2) {
		font-size: $font-lg;
	}

	:global(a) {
		text-decoration: none;
	}

	:global(body) {
		height: 100vh;
		width: 100vw;
		margin: 0;
		padding: 0;
		background-color: $bg-color;
		color: $text-color;
	}

	:global(.centerDown) {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
	}

	:global(.centerSide) {
		display: flex;
		flex-direction: row;
		justify-content: center;
		align-items: center;
	}

	:global(button) {
		margin: 1rem;
		border-width: 0;
		outline: none;
		border-radius: $border-sm;

		&:hover {
			cursor: pointer;
		}
	}
</style>
