import moment from "moment";

/**
 * Determines the current week number using the ISO week numbering system.
 *
 * @return  The week number.
 */
export function determineWeek() : number {
    const today = moment();
    return today.isoWeek();
}

