<slot />

<style lang="scss">
	:global(h1) {
		font-size: var(--font-size-xlarge);
		font-family: var(--header-font);
		font-weight: normal;
	}

	:global(h2) {
		font-size: var(--font-size-large);
		font-family: var(--header-font);
		font-weight: normal;
	}

	:global(a) {
		text-decoration: none;
		font-weight: normal;
	}

	:global(body) {
		height: 100vh;
		width: 100vw;
		margin: 0;
		padding: 0;
		background-color: var(--bg-color);
		color: var(--text-color);
		font-family: var(--body-font);
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
		border-width: 0;
		cursor: pointer;
		outline: none;
		border-radius: $border-sm;
	}
</style>
