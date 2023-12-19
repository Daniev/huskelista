# Run docker compose in dev mode for all or one of the services. Useful when working on the frontend or backend.

# note that the docker images dont refresh when making changes.. If needing to make changes to both front and back at the same time,
# run them locally in two terminals.

BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

if [[ $1 == "f" ]];
then
    echo -e "${BLUE}[INFO] Running frontend only...${NC}"
    sudo docker-compose up --build frontend
elif [[ $1 == "b" ]];
then
    echo -e "${BLUE}[INFO] Running backend only...${NC}"
    sudo docker-compose up --build backend

elif [[ $1 == "a" ]];
then
    echo -e "${BLUE} [INFO] Running both frontend and backend...${NC}"
    sudo docker-compose up --build
else
    echo -e "${RED}[ERROR] Please select f(rontend) or b(ackend) or a(ll)...${NC}"
fi


