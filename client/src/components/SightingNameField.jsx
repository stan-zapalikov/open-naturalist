import {React, useRef, useEffect} from 'react'

export default function SightingNameField({sightingName, setSightingName, onSubmit}) {
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