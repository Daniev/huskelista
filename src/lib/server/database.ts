import type { Task, metaData } from "$lib/types/tasks";
import { open } from "sqlite";
import sqlite3 from "sqlite3";

/** Handler for database related functionality */
export class DBHandler
{
    constructor() {
        const db = InitalizeSqliteDatabase();

        // singelton pattern
        
    }
    async init(): Promise<void> {
       
    }

    async updateTask(task: Task) {
        return true;
    }

    async getTasks(): Promise<Task[]> {
        return []; 
    }

    async getMetadata(): Promise<metaData> {
        return {} as metaData; 
    }

}


export async function InitalizeSqliteDatabase()  {
    return open({
        filename: "./data/database.db",
        driver: sqlite3.Database,
    });
};
