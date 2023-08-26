import moment from 'moment';
import type { DBHandler } from './server/database';

/**
 * Determines the current week number using the ISO week numbering system.
 *
 * @return  The week number.
 */
export function determineWeek(): number {
	const today = moment();
	return today.isoWeek();
}

/** Determines whether or not a new week has occured since the last week */
export async function isNewWeek(db: DBHandler): Promise<boolean> {
	const current = determineWeek();
	const metdata = await db.getMetadata();
	const stored = metdata.storedWeek;
	return current !== stored;
}
