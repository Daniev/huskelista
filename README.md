# Husansvar

Husansvar er en komplett liten todo webapp for å fordele husoppgavene mellom meg og kona. Den tilbyr en simpel frontend laget med SvelteKit
og en enkel webapi som håndterer lagring.


https://github.com/Daniev/husansvar/assets/81805034/c56c2a7f-f873-435d-8bed-316e4f061bc2


## Prøv det selv
For å kjøre lokalt, clone repositoriet, start docker og kjør følgende kommandoer i bash fra repository mappen:
```(bash)
chmod 700 spinup.sh
source spinup.sh # kjører både frontend og backend, b eller f som parameter kjører kun en av dem.
```
Du finner frontend in http://localhost:5173 or flask api i http://localhost:5000


## Teknisk
Hovedformålet med projektet er å demonstrere grunnleggende ferdigheter i Git (med squash merge i dette tilfelle), Docker, testing og webapi.
Arbeidet er ryddig organisert i feature brancher, og commit beskjedene er tydelige.


I mappen backend ligger et lite python WebAPI i Flask som håndterer lagring og interaksjoner mot lagringen av gjøremål for Husansvar.
Både endepunktene og funksjonliteten til endpunktene er unit testet med pytest. Ettersom dette lille prosjektet ikke er laget for å kunne skalere til mange brukere, lagres gjøremålene i en jsonfil.
Dokumentasjon for webapiet fås [her](backend/docs/apidoc.md)

| URL (after base) | METHOD | Description          | Params | Return Success | Return failure |
| ---------------- | ------ | -------------------- | ------ | -------------- | -------------- |
| /tasks           | GET    | Get all tasks        | user   | 200            | 404            |
| /tasks           | POST   | Create a new task    |        | 200            | 404            |
| /tasks/{slug}    | GET    | Get a single task    |        | 200            | 404            |
| /tasks/{slug}    | PUT    | Edit a single task   |        | 200            | 404, 400       |
| /tasks/{slug}    | DELETE | Delete a single task |        | 204            | 404, 405       |

# English
Husanvar is a complete small todo app for assigning house chores for me and my wife. If comprises of a simple frontend written with SvelteKit and a small
webapi that handles the storage of tasks.

To run locally, clone the repository, start docker and run the following commands in bash from within the repository folder:
```(bash)
chmod 700 spinup.sh
source spinup.sh # starts up both frontend and backend. Add a b or an f at the end of the command to just run one of them.
```

The main purpose of this project is to demonstrate basic skills and knowhow of Git, Docker, testing and webapis.
The work in Git is neatly organized into feature branches and merged using squash merge, with clear commit messages.

## Technical
The backend folder contains a small WebAPI written with Flask and Python, and serves to store the tasks and handles the interactions with this storage through endpoints.
All endpoints and the functionality of the endpoints are unit tested with pytest. As the this is a small sized project that is not made to scale well, all tasks are stored in a jsonfile.
The documentation for the webapi is avaiable [here](backend/docs/apidoc.md), and a short overview of the endpoints are below.

| URL (after base) | METHOD | Description          | Params | Return Success | Return failure |
| ---------------- | ------ | -------------------- | ------ | -------------- | -------------- |
| /tasks           | GET    | Get all tasks        | user   | 200            | 404            |
| /tasks           | POST   | Create a new task    |        | 200            | 404            |
| /tasks/{slug}    | GET    | Get a single task    |        | 200            | 404            |
| /tasks/{slug}    | PUT    | Edit a single task   |        | 200            | 404, 400       |
| /tasks/{slug}    | DELETE | Delete a single task |        | 204            | 404, 405       |

