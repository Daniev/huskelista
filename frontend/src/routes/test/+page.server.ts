import { getTasksURl } from '$lib/api/urls.js';
import axios from 'axios';

export async function load() {
    const url = getTasksURl('Mia');
    const response = await axios.get(url).catch((error) => console.log("Failed to get at " + url, error));
    if (response) {
        return {
            response: response.data
        };
    }

}
