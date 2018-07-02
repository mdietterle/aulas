from pyroutelib3 import Router # Import the router
router = Router("car") # Initialise it

start = router.data.findNode(-26.4900373, -49.0784009) # Find start and end nodes
end = router.data.findNode(-26.5052854, -49.090583)

status, route = router.doRoute(start, end) # Find the route - a list of OSM nodes

if status == 'success':
    routeLatLons = list(map(router.nodeLatLon, route)) # Get actual route coordinates
    print(routeLatLons)