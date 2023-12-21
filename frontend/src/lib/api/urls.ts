
import { FLASK_URL } from "$env/static/private"
import type { User } from "$lib/types/user";

const BASE_URL = FLASK_URL;
export const API_URL = `${BASE_URL}/api/v1`
export const TASK_URL = `${API_URL}/tasks/`

