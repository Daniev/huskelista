<script lang="ts">
	export let title = 'Set a title';
	export let color = 'grey';
</script>

<div class="{color} box">
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

		border-radius: $border-sm;
	}

	.header {
		display: flex;
		justify-content: left;
		align-items: center;
		padding: $padding-sm;
		height: 3rem;

		border-bottom: solid $border-color 1px;
	}

	.footer {
		border-top: solid $border-color 1px;
		display: flex;
		height: 1rem;
		justify-content: right;
		align-items: center;
		height: 10%;
	}

	.list-container {
		height: 21rem;
		display: flex;
		flex-direction: column;
		align-items: center;
		padding: $padding-sm;
	}

	.grey {
		background-color: $lightgrey1;
	}
</style>
