import React, { useState } from 'react';
import axios from 'axios'




function App() {
  const [name, setName] = useState('');
  const [submitted, setSubmitted] = useState(false);
  const [names, setNames] = useState([]);


  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:5000/names', {name: name});
      console.log('Server response:', response.data);
      await getNames();
      setName('')
      setSubmitted(true);
    } catch (error) {
      console.error('Error sending data:', error);
    }
  };

  const getNames = async () => {
    console.log('getNames called')
    try {
      const response =await axios.get('http://127.0.0.1:5000/names')
      console.log('response', response.data)
    } catch (error) {
      console.error('Error retrieving data:', error);
    }
  };

  return (
    <div>
      <h2>Basic Form</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="name">Name:</label>
          <input
            type="text"
            id="name"
            value={name}
            onChange={(e) => setName(e.target.value)}
            required
          />
        </div>
        <button type="submit">Submit</button>
      </form>
      {submitted && <p>Form submitted successfully!</p>}
      <List></List>
    </div>
  );
}

export default App;