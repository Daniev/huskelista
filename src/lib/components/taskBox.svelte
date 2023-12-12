<script lang="ts">
	export let title = 'Set a title';
</script>

<div class="box">
	<div class="header">
		<h2>{title}</h2>
	</div>
	{#if $$slots.taskList}
		<div class="list-container">
			<slot name="taskList" />
		</div>
	{/if}

	{#if $$slots.bottom}
		<div class="footer">
			<slot name="bottom" />
		</div>
	{/if}
</div>

<style lang="scss">
	.box {
		width: 22rem;
		max-height: 32rem;
		padding: var(--pa-small) var(--pa);

		background-color: var(--white);
		border-radius: var(--bo);
	}

	.header {
		display: flex;
		justify-content: left;
		align-items: center;
		padding: var(--pa) var(--pa) var(--pa);
		height: 2rem;

		border-bottom: solid var(--border-color) 1px;
		h2 {
			margin: 0;
		}
	}

	.footer {
		border-top: solid var(--border-color) 1px;
		display: flex;
		justify-content: right;
		align-items: center;
	}

	.list-container {
		height: 21rem;
		display: flex;
		flex-direction: column;
		align-items: center;
		padding: var(--pa);
		margin-top: var(--ma);
	}
</style>
