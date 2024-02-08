<slot />

<style lang="scss">
	:global(h1),
	:global(h2),
	:global(h3) {
		margin: var(--ma-big) 0;
		font-family: var(--header-font);
		letter-spacing: var(--header-letter-spacing);
		line-height: var(--header-line-height);
	}
	:global(h1) {
		font-size: var(--fo-large);
		font-weight: normal;
	}

	:global(h2) {
		font-size: var(--fo-medium);
		font-weight: normal;
	}

	:global(h3) {
		font-size: var(--fo-medium);
		font-weight: normal;
	}

	:global(a) {
		text-decoration: none;
		font-size: var(--fo-small);
		font-weight: normal;
	}

	:global(p) {
		font-size: var(--fo-small);
		font-weight: normal;
		margin: none;
	}

	:global(body) {
		height: 100svh;
		width: 100svw;
		margin: 0;
		padding: 0;
		background-color: var(--bg-color);
		color: var(--text-color);
		font-family: var(--body-font);
		font-size: var(--fo-small);
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
		border: 0;
		cursor: pointer;
		outline: none;
		border-radius: var(--bo);
	}
</style>
