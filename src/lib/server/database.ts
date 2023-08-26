import type { Task, metaData } from '$lib/types/tasks';
import sqlite3 from 'sqlite3';

/** Handler for database related functionality */
export class DBHandler {
	name: string;

	constructor(name = 'houseTasks') {
		// singelton pattern
		this.name = name;
	}
	/**Checks if the database needs to update its data and refills it with new tasks
	 * if a week has passed..
	 */
	async update(): Promise<void> {}

	/** Updates the provided task in the database */
	async updateTask(task: Task): Promise<boolean> {
		return true;
	}

	/** Gets a list of all tasks belonging to the user. */
	async getTasks(): Promise<Task[]> {
		return [];
	}

	async getMetadata(): Promise<metaData> {
		return {} as metaData;
	}
	/** Resets the database, wiping all data and adding inital values and tables...
	 * Used in development..
	 */
	async resetDatabase(): Promise<void> {
		const db = this.GetDb();
		db.serialize(() => {
			db.all('DROP TABLE IF EXISTS tasks');
			db.all('DROP TABLE IF EXISTS metadata');

			db.all(
				'CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, title TEXT, description TEXT, completed BOOLEAN)',
				(err) => err && console.error('error while creating tasks table', err.message)
			);
			db.run(
				'CREATE TABLE IF NOT EXISTS metadata (storedWeek INTEGER, dataStored BOOLEAN)',
				(err) => err && console.error('error while creating metadata table', err.message)
			);

			db.run('INSERT INTO metadata (storedWeek, dataStored) VALUES (1, 1)', (err) => {
				if (err) {
					console.error('error while creating metadata data', err.message);
				}
			});
			db.run("INSERT INTO tasks (title, description, completed) VALUES ('vask bad', 'vask bad', 0)", (err) => {
				if (err) {
					console.error('error while creating tasks data', err.message);
				}
			});
		});

		this.closeDb(db);
	}

	/** Creates the database file and initializes the datbase object. */
	GetDb() {
		const databasePath = './database.sqlite';
		const db = new sqlite3.Database(databasePath, (err) => {
			if (err) {
				console.error('error while opening database:', err.message);
			}
		});
		return db;
	}

	closeDb(db: sqlite3.Database) {
		db.close((err) => {
			if (err) {
				console.error('error while closing database:', err.message);
			}
		});
	}
}
