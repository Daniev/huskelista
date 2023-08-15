
export interface Task {
    id: number;
    title: string;
    description: string;
    completed: boolean;
}

/** Metadata used to function the database... */
export interface metaData {
    storedWeek: number;
}