# Drone-Flight-Path-Checker-DE-
Programm analyses the Flight Logs of DJI Drones and cross checks the geographical data with German no-fly-zones to identify if a restricted airspace has been entered, it is created for a paper in a university course 

## TODO:

0. Find if someone has done similar stuff

1. Get Official Data in the standardized Format, Store it in a good way to compare it later

2. Check how in other Software, the Algorithm is written that extracts the GPS Data and builds the flight path

3. Find out, how you can identify if during the flight Path, a restricted Airspace has been enterd
    -> Idea: Store the extreme Edges (North, East, South, West) of all Airspaces and maybe find a way to minimze the zones we are checking against based on the start coordinates

4. if Time: Visualize it on a Map