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


export const actions = {
    default: async ({ request, cookies }) => {
        const data = await request.formData();
        const cookieUser = cookies.get('user');
        const task = {
            title: data.get("title"),
            assignee: data.get("assignee"),
            complete: false
        }
        if (!cookieUser || cookieUser === "unknown") {
            throw redirect(307, "/");
        }
        const response = await axios.post(TASK_URL, task).catch((error) => console.warn("Failed to create task: " + error));
        if (!response) {
            return {
                error: "Failed to create task"
            }
        }
        return {
            response: response.data
        }
    }
}
