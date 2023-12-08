import { redirect } from "@sveltejs/kit";
import type { User } from "$lib/types/user.js";

export function load({ cookies }) {
    const cookieUser = cookies.get('user');
    if (!cookieUser || cookieUser === "unknown") {
        throw redirect(307, "/");
    }
    return {
        user: cookieUser as User,
    }
}
