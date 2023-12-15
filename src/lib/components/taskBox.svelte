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
		max-height: 33rem;
		background-color: var(--white);
		border-radius: var(--bo);
		border: var(--border-small);
	}

	.header {
		display: flex;
		justify-content: left;
		align-items: center;
		padding: var(--pa-big) var(--pa-big) var(--pa-big);
		height: 2rem;
		border-bottom: solid var(--border-color) 1px;
		h2 {
			margin: 0;
		}
	}

	.footer {
		border-top: solid var(--border-color) 1px;
		padding: 0 var(--pa) var(--pa);
		display: flex;
		justify-content: right;
		align-items: center;
	}

	.list-container {
		height: 20rem;
		display: flex;
		flex-direction: column;
		align-items: center;
		padding: var(--pa);
		margin-top: var(--ma);
	}
</style>
