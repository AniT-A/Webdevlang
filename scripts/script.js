function fetchData(dataFile, imageUrl) {
    fetch(dataFile + '.txt')
        .then(response => response.text())
        .then(data => {
            document.getElementById('text-container').innerHTML = data;
            const imageElement = document.getElementById('image');
            imageElement.src = imageUrl;
            imageElement.style.display = 'block';
        })
        .catch(error => document.getElementById('text-container').innerText = 'Error: ' + error.message);
}

