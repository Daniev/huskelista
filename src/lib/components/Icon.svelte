<script lang="ts">
    /** Use to render icons from iconify!
     * Manipulate the colors by assigning the icon css variables
    */
    import Icon from "@iconify/svelte";

    /** defaults to checkmark*/
    export let iconName: string = "zondicons:checkmark-outline";
    /** Dont include the brackets in the style prop */
    export let style : string = "color: var(--icon-fill-color); background-color: var(--icon-bg-color)";
</script>

<Icon icon={iconName} style={style} height="24px"/>
