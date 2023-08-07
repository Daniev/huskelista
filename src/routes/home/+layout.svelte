<header>
	<div>Hus</div>
	<a href="/">
		<button class="round">Logg ut</button>
	</a>
</header>

<slot />

<style lang="scss">
	header {
		background-color: grey;
		width: 100vw;
		height: 10vh;
		display: flex;
		justify-content: space-between;
		align-items: center;
	}

	.round {
		height: 2rem;
		width: 7rem;
		border-radius: 84px;
		font-size: 16px;
	}
</style>
