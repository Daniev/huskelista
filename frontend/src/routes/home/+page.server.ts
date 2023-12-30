import { redirect } from "@sveltejs/kit";
import type { User } from "$lib/types/user.js";
import type { Task } from "$lib/types/tasks.js";
import axios from "axios";
import { TASK_URL } from "$lib/api/urls.js";

export async function load({ cookies }) {
    const cookieUser = cookies.get('user');
    if (!cookieUser || cookieUser === "unknown") {
        throw redirect(307, "/");
    }
    const params = "?user=" + cookieUser;
    const response = await axios.get(TASK_URL + params).catch((error) => console.warn("Failed to get tasks: " + error));
    if (response) {
        return {
            user: cookieUser as User,
            response: response.data as Task[]
        }
    }
    return {
        user: cookieUser as User,
        response: [] as Task[]
    }
}
