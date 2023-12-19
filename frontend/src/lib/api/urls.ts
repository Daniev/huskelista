
import { FLASK_URL } from "$env/static/private"
import type { User } from "$lib/types/user";

const BASE_URL = FLASK_URL;
export const API_URL = `${BASE_URL}/api/v1`


export const getTasksURl = (user: User) => {
    return `${API_URL}/${user.toLowerCase()}/tasks`
}
