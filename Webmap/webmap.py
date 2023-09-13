import folium
import webbrowser

# Create a map centered at a specific location
map_center = [37.7749, -122.4194]  # San Francisco, CA
m = folium.Map(location=map_center, zoom_start=12)

# Add a marker to the map
marker_location = [37.7749, -122.4194]  # San Francisco, CA
folium.Marker(location=marker_location, popup='San Francisco').add_to(m)

# Get the HTML source of the map
map_html = m.get_root().render()

# Save the HTML source to a temporary file
with open('temp_map.html', 'w') as f:
    f.write(map_html)

# Open the temporary map HTML file in the default web browser
webbrowser.open('temp_map.html')
