function searchJournals() {
  const searchTerm = document.getElementById('searchInput').value;
  const apiUrl = `https://api.crossref.org/journals?query=${searchTerm}`;

  fetch(apiUrl)
    .then(response => response.json())
    .then(data => {
      const journalResults = document.getElementById('journalResults');
      journalResults.innerHTML = '';

      data.message.items.forEach(journal => {
        const journalElement = document.createElement('div');
        journalElement.innerHTML = `
          <h3>${journal.title}</h3>
          <p>ISSN: ${journal.ISSN.join(', ')}</p>
          <p>Publisher: ${journal.publisher}</p>
          <p>Subject Areas: ${journal.subject}</p>
        `;
        journalResults.appendChild(journalElement);
      });
    })
    .catch(error => {
      console.error('Error:', error);
      const journalResults = document.getElementById('journalResults');
      journalResults.innerHTML = '<p>Error: Unable to fetch journal data.</p>';
    });
}
