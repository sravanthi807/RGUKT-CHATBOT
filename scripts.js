document.getElementById('feedback-form').addEventListener('submit', function(event) {
    event.preventDefault();
    var feedback = document.getElementById('feedback').value;

    fetch('/submit_feedback', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ feedback: feedback })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        document.getElementById('feedback').value = '';
        loadFeedbacks();
    })
    .catch(error => console.error('Error:', error));
});

function loadFeedbacks() {
    fetch('/feedbacks')
        .then(response => response.json())
        .then(data => {
            var feedbackList = document.getElementById('feedbacks');
            feedbackList.innerHTML = '';
            data.feedbacks.forEach(feedback => {
                var li = document.createElement('li');
                li.textContent = feedback;
                feedbackList.appendChild(li);
            });
        })
        .catch(error => console.error('Error:', error));
}

// Load feedbacks on page load
window.onload = loadFeedbacks;
