import { DBHandler } from '$lib/server/database';

export async function load() {
	const dbHandler = new DBHandler();
	dbHandler.resetDatabase();
	dbHandler.update();
}
