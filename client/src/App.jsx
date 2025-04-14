import { useState, useEffect, useRef } from 'react'

function SightingNameField({sightingName, setSightingName, onSubmit}) {
  const inputRef = useRef()
  const handleSubmit = (event) => {
    event.preventDefault()
    setSightingName(inputRef.current.value)
    console.log(inputRef.current.value)
    onSubmit(inputRef.current.value)
  }
  useEffect(() => {
    console.log("sightingName changed: ", sightingName)
  }, [sightingName])
  return (
    <form onSubmit={handleSubmit}>
      <input type="text" ref={inputRef} />
      <button type="submit">Submit Sighting</button>

    </form>
  )
}

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
  
  const getUserLocation = () => {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        (position) => {
          const {latitude, longitude} = position.coords
          setUserLocation({latitude, longitude})
        }
      )
    } else {
      console.error("Geolocation not supported")
    }
  }

  const handleFormSubmit = (animalName) => {
    if (!userLocation) {
      console.error("No location data")
      return;
    }
    const payload = {
      animal_name: animalName,
      latitude: userLocation.latitude,
      longitude: userLocation.longitude
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
  }

  return (
  <>
    <button onClick={getUserLocation}>Get User Location</button>
    {userLocation && (
      <div>
        <h2>User Location</h2>
        <p>Latitude: {userLocation.latitude}</p>
        <p>Longitude: {userLocation.longitude}</p>
      </div>
      
    )}
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

  </>
)
}
