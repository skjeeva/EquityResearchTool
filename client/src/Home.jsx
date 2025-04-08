import { useState } from "react";

const Home = () => {
  const [query, setQuery] = useState("");
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");

  const handleSearch = async (e) => {
    e.preventDefault();
    setError("");
    setResult(null);

    try {
      const response = await fetch("http://localhost:5000/api/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query }),
      });

      const data = await response.json();

      if (response.ok) {
        setResult(data);
      } else {
        setError(data.message || "Something went wrong");
      }
    } catch (err) {
      setError("Error contacting the server");
    }
  };

  return (
    <div className="container py-5">
      <h1 className="text-center mb-4">Finance Insight Search</h1>

      <form onSubmit={handleSearch} className="d-flex mb-4">
        <input
          type="text"
          className="form-control me-2"
          placeholder="Search company (e.g., Tesla, Apple)"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          required
        />
        <button type="submit" className="btn btn-success">
          Search
        </button>
      </form>

      {error && <div className="alert alert-danger">{error}</div>}

      {result && (
        <div className="card shadow p-3">
          <h3 className="card-title mb-3">{result.Company}</h3>
          <ul className="list-group">
            <li className="list-group-item"><strong>Sector:</strong> {result.Sector}</li>
            <li className="list-group-item"><strong>Market Cap:</strong> {result["Market Cap"]}</li>
            <li className="list-group-item"><strong>Current Price:</strong> {result["Current Price"]}</li>
            <li className="list-group-item"><strong>52 Week High:</strong> {result["52 Week High"]}</li>
            <li className="list-group-item"><strong>52 Week Low:</strong> {result["52 Week Low"]}</li>
            <li className="list-group-item"><strong>Revenue:</strong> {result.Revenue}</li>
            <li className="list-group-item"><strong>Net Income:</strong> {result["Net Income"]}</li>
            <li className="list-group-item"><strong>PE Ratio:</strong> {result["PE Ratio"]}</li>
            <li className="list-group-item"><strong>EPS:</strong> {result.EPS}</li>
          </ul>
        </div>
      )}
    </div>
  );
};

export default Home;
