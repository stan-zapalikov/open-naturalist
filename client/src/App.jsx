import { useState } from 'react'

export default function App() {
  const [userLocation, setUserLocation] = useState(null)
  
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
  </>
)
}
