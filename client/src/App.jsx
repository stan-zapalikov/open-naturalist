import { useState, useEffect, useRef } from 'react'
import SightingNameField from './components/SightingNameField'
import './App.css'

export default function App() {
  const [userLocation, setUserLocation] = useState(null)
  const [loc, setLoc] = useState(null)
  const [sightingName, setSightingName] = useState("")
  const [sightings, setSightings] = useState([])

  useEffect(() => {
    fetch("http://localhost:5000/sightings")
      .then(res => res.json())
      .then(data => setSightings(data))
      .catch(err => console.error("Fetch error: ", err))
  }, [])
  


  const handleFormSubmit = (animalName) => {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        (position) => {
          const {latitude, longitude} = position.coords

          const payload = {
          animal_name: animalName,
          latitude: latitude,
          longitude: longitude
          }
          
          fetch("http://localhost:5000/upload", { 
            method: "POST",
            headers: {
              "Content-Type": "application/json"
            },
            body: JSON.stringify(payload)
          })
            .then(res => res.json())
            .then(data => console.log("Success: ", data))
            .catch(err => console.error("Error: ", err))
        },
        (error) => {
          console.error("Geolocation error: ", error)
        }
      )
    } else {
      console.error("Geolocation not supported")
    }
  }

  return (
  <div class=""> 
    <SightingNameField 
      sightingName={sightingName} 
      setSightingName={setSightingName} 
      onSubmit={handleFormSubmit}
    />

    <h2>All sightings</h2>
    <ul>
      {sightings.map((sighting) => (
        <li key={sighting.id}>
          {sighting.animal_name} at ({sighting.latitude}, {sighting.longitude})
        </li>
      ))}
    </ul>

  </div>
)
}
