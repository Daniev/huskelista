import { writable } from "svelte/store";
import type { User } from "$lib/types/user";

export const user = writable<User>("unknown");
export const users = writable<User[]>(["Mia", "Daniel"]);