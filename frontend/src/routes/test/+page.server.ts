import { TASK_URL } from '$lib/api/urls.js';
import axios from 'axios';

export async function load() {
    const url = TASK_URL;
    const param = "?user=mia";
    const response = await axios.get(url + param).catch((error) => console.log("Failed to get at " + url, error));
    if (response) {
        return {
            response: response.data
        };
    }

}
