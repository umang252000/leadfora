"use client"

import { useState } from "react"
import axios from "axios"

export default function Home() {

  const [query, setQuery] = useState("")
  const [leads, setLeads] = useState([])
  const [activity, setActivity] = useState([])
  const [loading, setLoading] = useState(false)

  const searchLeads = async () => {

    setLoading(true)

    try {

      const res = await axios.post(
        "https://8000--019cc884-c11a-7f3c-9231-bf9c7a165a1c.us-east-1-01.gitpod.dev/search-leads",
        { query }
      )

      setLeads(res.data.results || [])
      setActivity(res.data.activity || [])

    } catch (error) {

      console.error(error)

    }

    setLoading(false)
  }

  return (
    <div className="min-h-screen bg-gray-100 p-10">

      <h1 className="text-4xl font-bold mb-8">
        Leadfora AI Sales Lead Hunter
      </h1>

      {/* Search + Buttons */}
      <div className="flex gap-4 mb-8">

        <input
          className="border p-3 w-96 rounded"
          placeholder="Find leads (ex: AI startups in Europe)"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />

        <button
          onClick={searchLeads}
          className="bg-blue-600 text-white px-6 py-3 rounded"
        >
          Run Agent
        </button>

        <a
          href="https://8000--019cc884-c11a-7f3c-9231-bf9c7a165a1c.us-east-1-01.gitpod.dev/export-leads"
          className="bg-green-600 text-white px-6 py-3 rounded"
        >
          Export CSV
        </a>

      </div>

      {loading && (
        <p className="text-blue-600 mb-4">
          Agent searching the web...
        </p>
      )}

      {/* Improved Agent Workflow UI */}
      <div className="bg-white shadow p-6 mb-6 rounded">

        <h2 className="text-xl font-semibold mb-4">
          AI Agent Workflow
        </h2>

        {activity.length === 0 && (
          <p className="text-gray-400">
            Run a search to start the AI workflow
          </p>
        )}

        <div className="space-y-2">

          {activity.map((item, index) => (

            <div
              key={index}
              className="flex items-center gap-2 text-green-700"
            >

              <span className="text-xl">🟢</span>

              <span>{item}</span>

            </div>

          ))}

        </div>

      </div>

      {/* Leads Table */}
      <table className="bg-white shadow w-full">

        <thead className="bg-gray-200">
          <tr>
            <th className="p-3 text-left">Name</th>
            <th className="p-3 text-left">Role</th>
            <th className="p-3 text-left">Company</th>
            <th className="p-3 text-left">Email</th>
            <th className="p-3 text-left">Score</th>
            <th className="p-3 text-left">Priority</th>
          </tr>
        </thead>

        <tbody>

          {leads.map((lead, index) => (
            <tr key={index} className="border-t">

              <td className="p-3">{lead.name}</td>
              <td className="p-3">{lead.role}</td>
              <td className="p-3">{lead.company}</td>
              <td className="p-3">{lead.email}</td>

              <td className="p-3 font-bold">
                {lead.score}
              </td>

              <td className="p-3">
                {lead.priority === "High" && "🔥 High"}
                {lead.priority === "Medium" && "⚡ Medium"}
                {lead.priority === "Low" && "Low"}
              </td>

            </tr>
          ))}

        </tbody>

      </table>

    </div>
  )
}