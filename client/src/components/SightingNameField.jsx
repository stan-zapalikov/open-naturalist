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
    <form onSubmit={handleSubmit} className="">
      <input className="w-64 bg-transparent placeholder:text-slate-400 text-slate-700 text-sm border border-slate-200 rounded-md px-3 py-2 transition duration-300 ease focus:outline-none focus:border-slate-400 hover:border-slate-300 shadow-sm focus:shadow" type="text" ref={inputRef} />
      <button className="relative inline-flex items-center justify-center p-0.5 mb-2 me-2 overflow-hidden text-sm font-medium text-gray-900 rounded-lg group bg-gradient-to-br from-green-400 to-blue-600 group-hover:from-green-400 group-hover:to-blue-600 hover:text-white focus:ring-4 focus:outline-none focus:ring-green-200" type="submit">
      <span className="relative px-5 py-2.5 transition-all ease-in duration-75 bg-white rounded-md group-hover:bg-transparent">
      Submit Sighting
      </span>
      </button>

    </form>
  )
}