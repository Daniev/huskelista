export interface Task {
	id: number;
	title: string;
	description: string;
	completed: boolean;
}

/** Metadata used by the database... */
export interface metaData {
	storedWeek: number;
	dataStored: boolean;
}
