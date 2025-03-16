"use client";
import { useState } from 'react';
import axios from 'axios';

const Home = () => {
  const [query, setQuery] = useState('');
  const [response, setResponse] = useState('');

  const handleQueryChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setQuery(e.target.value);
  };

  const handleQuerySubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    const res = await axios.get('http://localhost:8000/api/generate_response/', {
      params: { query },
    });

    setResponse(res.data.response);
  };

  return (
    <StyledWrapper></StyledWrapper>
      <h1>Chatbot with GitHub Data</h1>
      <form onSubmit={handleQuerySubmit}>
        <input type="text" value={query} onChange={handleQueryChange} />
        <button type="submit">Ask</button>
      </form>
      <div>
        <p>{response}</p>
      </div>
    </div>
  );
};

export default Home;

