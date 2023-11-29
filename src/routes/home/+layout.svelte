<header>
	<a href="/">
		<button class="round">Logg ut</button>
	</a>
</header>

<slot />

<style lang="scss">
	header {
		width: 100vw;
		height: 10vh;
		display: flex;
		justify-content: right;
		align-items: center;
	}

	.round {
		height: 2rem;
		width: 7rem;
		border-radius: 84px;
		font-size: 16px;
		background-color: var(--subtle-button-color);

		&:hover {
			background-color: var(--subtle-button-hover-color);
		}
	}
</style>
