import type { Task } from "$lib/types/tasks";
import { writable } from "svelte/store";


const defaultList = [
    {
        id: 1,
        title: 'vask bad',
        description: 'vask bad',
        completed: false,
    },
    {
        id: 2,
        title: 'klesvask',
        description: 'klesvask',
        completed: false,
    },
    {
        id: 3,
        title: 'støvsuger og tørke støv',
        description: 'støvsuger og tørke støv',
        completed: false,
    },
    {
        id: 4,
        title: 'sofa',
        description: 'sofa',
        completed: true,
    }
];



export const list = writable<Task[]>(defaultList);



