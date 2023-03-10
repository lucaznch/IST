/* iaed-23 - ist1102637 - project1 */
#include <stdio.h>
#include <string.h>

#define MAX_NUM_BUSES 200
#define MAX_NUM_STOPS 10000
#define MAX_NUM_LINKS 30000

#define MAX_NAME_BUS 21
#define MAX_BYTES_NAME_BUS 20
#define MAX_NAME_STOP 51
#define MAX_BYTES_NAME_STOP 50
#define MAX_NAME_INVERSE 8

#define TRUE 1
#define FALSE 0

/*
    melhor input way? scanf, getchar, fg
    tamanho dos nomes?
    p p1 != p p1 \n
    qualidade do codigo
    usar struct em structs? ou indices?

*/

/* sort nomeCarreira alfabeticamente | sort inverso | carreiras circulares!!! byte name*/

typedef struct
{
    char name[MAX_NAME_STOP];
    int buses_of_this_stop;
    int buses[MAX_NUM_BUSES];
    double latitude;
    double longitude;
} Stop;

typedef struct
{
    char name[MAX_NAME_BUS];
    int origin_stop_index;
    int destination_stop_index;
    int totalStops;
    int route[MAX_NUM_LINKS];
    double totalCost;
    double totalDuration;
} Bus;

typedef struct
{
    int bus;
    int origin_stop_index;
    int destination_stop_index;
    double cost;
    double duration;
} Link;


int number_of_buses = 0;
Bus allBuses[MAX_NUM_BUSES];

int number_of_stops = 0;
Stop allStops[MAX_NUM_STOPS];

int number_of_links = 0;
Link allLinks[MAX_NUM_LINKS];


/* reads till the end of line */
void reads()  {
	char c = getchar();
	while (c != '\n')
		c = getchar();
}

/* reads next word from input */
int readWord(char word[]) {
    char c = getchar();
    int i = 0;
    while (c == ' ' || c == '\t')
        c = getchar();

    if (c == '"') {
        c = getchar();
        while (c != '"') {
            word[i++] = c;
            c = getchar();
        }
        word[i] = '\0';
    }
    else {
        while (c != ' ' && c != '\t' && c != '\n') {
            word[i++] = c;
            c = getchar();
        }
        word[i] = '\0';
    }
    return (c == '\n');
}

/* checks if stop/bus name already exists */
int nameChecker(char str[], int is_stop_name) {
    int i;

    if (is_stop_name) {
        for (i = 0; i < number_of_stops; i++) {
            if (strcmp(allStops[i].name, str) == 0)
                return TRUE;
        }
        return FALSE;
    }
    else {
        for (i = 0; i < number_of_buses; i++) {
            if (strcmp(allBuses[i].name, str) == 0)
                return TRUE;
        }
        return FALSE;
    }
}

/* finds the index of stop/bus in the list. returns the index */
int finder(char str[], int is_stop_name) {
    int i;

    if (is_stop_name) {
        for (i = 0; i < number_of_stops; i++) {
            if (strcmp(allStops[i].name, str) == 0)
                return i;
        }
    }
    else {
        for (i = 0; number_of_buses; i++) {
            if (strcmp(allBuses[i].name, str) == 0)
                return i;
        }
    }
    return -1;
}



void stopFunction()  {
    char stop_name[MAX_NAME_STOP];
    int i, state;
    double latitude, longitude;
    state = readWord(stop_name);

    if (strlen(stop_name) == 0) {
        for (i = 0; i < number_of_stops; i++)
            printf("%s: %16.12f %16.12f %d\n", allStops[i].name, allStops[i].latitude,
                   allStops[i].longitude, allStops[i].buses_of_this_stop);
    }
    else {
        if (state) {
            if (nameChecker(stop_name, TRUE)) {
                i = finder(stop_name, TRUE);
                printf("%16.12f %16.12f\n", allStops[i].latitude, allStops[i].longitude);
            }    
            else
                printf("%s: no such stop.\n", stop_name);
        }
        else {
            if (nameChecker(stop_name, TRUE)) {
                printf("%s: stop already exists.\n", stop_name);
                reads();
            }
            else {
                scanf("%lf %lf", &latitude, &longitude);
                reads();
                strcpy(allStops[number_of_stops].name, stop_name);
                allStops[number_of_stops].latitude = latitude;
                allStops[number_of_stops].longitude = longitude;
                allStops[number_of_stops].buses_of_this_stop = 0;
                number_of_stops++;
            }
        }
    }
}

void listAllBuses() {
    int i, j, k, cicleBus;
    for (i = 0; i < number_of_buses; i++) {
        j = allBuses[i].origin_stop_index;
        k = allBuses[i].destination_stop_index;
        if (allBuses[i].totalStops == 0)
            printf("%s %d %.2f %.2f\n", allBuses[i].name, allBuses[i].totalStops, 
            allBuses[i].totalCost, allBuses[i].totalDuration);
        else
        {
            if (j == k)
                cicleBus = allBuses[i].totalCost - 1;
            else
                cicleBus = allBuses[i].totalCost;
            printf("%s %s %s %d %.2f %.2f\n", allBuses[i].name, allStops[j].name,
            allStops[k].name, cicleBus, allBuses[i].totalCost, allBuses[i].totalDuration);
        }
    }
}

/*  list route of bus (from origin stop to destination stop)
    from destination to origin stop if inverted == TRUE  */  
void showRouteOfBus(int bus_index, int inverted) {
    int i, j, n;
    n = allBuses[bus_index].totalStops;
    if (!inverted) {
        for (i = 0; i < n; i++) {
            j = allBuses[bus_index].route[i];
            if (i != n - 1)
                printf("%s, ", allStops[j].name);
            else
                printf("%s\n", allStops[j].name);
        }
    }
    else {
        for (i = n - 1; i >= 0; i--) {
            j = allBuses[bus_index].route[i];
            if (i != 1)
                printf("%s, ", allStops[j].name);
            else
                printf(", %s\n", allStops[j].name);
        }
    }
}

void busFunction() {
    char bus_name[MAX_NAME_BUS], inverse[MAX_NAME_INVERSE];
    int state; 
    state = readWord(bus_name);

    if (strlen(bus_name) == 0)
        listAllBuses();
    else {
        if (state) {
            if (!nameChecker(bus_name, FALSE)) {
                strcpy(allBuses[number_of_buses].name, bus_name);
                allBuses[number_of_buses].totalStops = 0;
                number_of_buses++;
            }
            else
                showRouteOfBus(finder(bus_name, FALSE), FALSE);
        }
        else {
            readWord(inverse);
            if (strcmp(inverse, "inverso") == 0 || strcmp(inverse, "i") == 0 || strcmp(inverse, "in") == 0 || strcmp(inverse, "inv") == 0) 
                showRouteOfBus(finder(bus_name, FALSE), TRUE);
            else 
                printf("incorrect sort option.\n");
        }
    }
}

void updateRoute(int bus, int oStop, int dStop, double c, double d) {
    int i, n, temp;

    if (allBuses[bus].destination_stop_index == oStop) { /* if destOld = OrigNew */
        /* check for ciclo !! */
        i = allBuses[bus].totalStops; /* get total stops */
        allBuses[bus].route[i] = dStop; /* add destination to route */
        allBuses[bus].destination_stop_index = dStop; /* updt destination */
        allBuses[bus].totalStops++; /* updt total stops */
        allBuses[bus].totalCost += c; /* updt total cost */
        allBuses[bus].totalDuration += d; /* updt total duration */
    }
    else { /* if origOld = DestNew */
        /* shift elements to the right one position and add element in the beginning */
        n = allBuses[bus].totalStops;
        temp = allBuses[bus].route[n - 1];
        for (i = n - 1; i > 0; i--) 
            allBuses[bus].route[i] = allBuses[bus].route[i - 1];
        allBuses[bus].route[0] = oStop;
        allBuses[bus].route[n] = temp;

        allBuses[bus].origin_stop_index = oStop;
        allBuses[bus].totalStops++;
        allBuses[bus].totalCost += c;
        allBuses[bus].totalDuration += d;
    }
}

/* checks if bus is already in the list of buses of respective stop */
int busInStopList(int busIndex, int stopIndex) {
    int i;
    for (i = 0; i < allStops[stopIndex].buses_of_this_stop; i++) {
        if (allStops[stopIndex].buses[i] == busIndex)
            return TRUE;
    }
    return FALSE;
}

void addLink(char busName[], char oStop[], char dStop[], double c, double d) {
    int origin, destination, bus; /* indexes */
    int i;
    origin = finder(oStop, TRUE);
    destination = finder(dStop, TRUE);
    bus = finder(busName, FALSE);

    if (allBuses[bus].totalStops == 0) { /* if bus doesnt have route yet */
        allBuses[bus].route[0] = origin; 
        allBuses[bus].route[1] = destination; /* start route */
        allBuses[bus].totalStops = 2; /* update total stops to 2 */
        allBuses[bus].origin_stop_index = origin; /* updt originS */
        allBuses[bus].destination_stop_index = destination; /* updt destinationS */
        allBuses[bus].totalCost = c; /* updt total cost */
        allBuses[bus].totalDuration = d; /* updt total duration */
    }
    else {
        updateRoute(bus, origin, destination, c, d);
    }
    if (!busInStopList(bus, origin)) { 
        i = allStops[origin].buses_of_this_stop;
        allStops[origin].buses[i] = bus;
        allStops[origin].buses_of_this_stop++;

    }
    if (!busInStopList(bus, destination)) {
        i = allStops[destination].buses_of_this_stop;
        allStops[destination].buses[i] = bus;
        allStops[destination].buses_of_this_stop++;
    }
}

int notValidLink(char busName[], char oStop[], char dStop[]) {
    int bus, origin, destination;
    bus = finder(busName, FALSE);
    if (allBuses[bus].totalStops == 0)
        return FALSE;
    
    origin = finder(oStop, TRUE);
    destination = finder(dStop, TRUE);

    if (allBuses[bus].destination_stop_index == origin || allBuses[bus].origin_stop_index == destination)
        return FALSE;
    return TRUE;
}

void linkFunction() {
    char busName[MAX_NAME_BUS], origin_stopName[MAX_NAME_STOP], destination_stopName[MAX_NAME_STOP];
    double cost, duration;

    readWord(busName);
    readWord(origin_stopName);
    readWord(destination_stopName);
    scanf("%lf %lf", &cost, &duration);
    reads();

    if (!nameChecker(busName, FALSE))
        printf("%s: no such line.\n", busName);
    else if (!nameChecker(origin_stopName, TRUE))
        printf("%s: no such stop.\n", origin_stopName);
    else if (!nameChecker(destination_stopName, TRUE))
        printf("%s: no such stop.\n", destination_stopName);
    else if (notValidLink(busName, origin_stopName, destination_stopName))
        printf("link cannot be associated with bus line.\n");
    else if (cost < 0 || duration < 0)
        printf("negative cost or duration.\n");
    else 
        addLink(busName, origin_stopName, destination_stopName, cost, duration);
}

void intersectionFunction() {
    int i, j, k;
    /* <nome-de-paragem> <número-de-carreiras>: <nome-de-carreira> ... */
    for (i = 0; i < number_of_stops; i++) {
        if (allStops[i].buses_of_this_stop == 1)
            ;
        else {
            printf("%s %d: ", allStops[i].name, allStops[i].buses_of_this_stop);
            for (j = 0; j < allStops[i].buses_of_this_stop; j++) {
                if (j == allStops[i].buses_of_this_stop - 1) {
                    k = allStops[i].buses[j];
                    printf("%s\n", allBuses[k].name);
                }
                else {
                    k = allStops[i].buses[j];
                    printf("%s ", allBuses[k].name);
                }
            }
        }
    }
    reads();
}

int main() {
    int c;

    while ((c = getchar()) != EOF) {
        switch (c) {
        case 'q':
            return 0;
        case 'c':
            busFunction();
            break;
        case 'p':
            stopFunction();
            break;
        case 'l':
            linkFunction();
            break;
        case 'i':
            intersectionFunction();
            break;
        default:
            printf("Invalid command: %c\n", c);
        }
    }
    return 0;
}