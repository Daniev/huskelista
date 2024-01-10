# Husansvar Backend FLASK API
Denne delen av applikasjonen håndterer lagring og interaksjoner mot lagringen av gjøremål for Husansvar.
Den har følgende endepunkt. For mer informasjon, se [dokumentasjon](docs/apidoc.md).

Både endepunktene og funksjonliteten til endpunktene er unit testet med pytest. Ettersom dette lille prosjektet ikke er laget for å kunne skalere til mange brukere, lagres gjøremålene i en jsonfil.



| URL (after base) | METHOD | Description          | Params | Return Success | Return failure |
| ---------------- | ------ | -------------------- | ------ | -------------- | -------------- |
| /tasks           | GET    | Get all tasks        | user   | 200            | 404            |
| /tasks           | POST   | Create a new task    |        | 200            | 404            |
| /tasks/{slug}    | GET    | Get a single task    |        | 200            | 404            |
| /tasks/{slug}    | PUT    | Edit a single task   |        | 200            | 404            |
| /tasks/{slug}    | DELETE | Delete a single task |        | 204            | 404            |

*The base is {domain}/api/v1*

## English
This part of the application handles the storage of tasks and the interactions with this storage through endpoints.
These endpoints are presented in the table above. For more details on the endpoints, see the [docs](docs/apidoc.md).

All endpoints and the functionality of the endpoints are unit tested with pytest. As the this is a small sized project that is not made to scale well, all tasks are stored in a jsonfile.

