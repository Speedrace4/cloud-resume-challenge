var apiUrl = 'https://cajxprauif.execute-api.us-east-2.amazonaws.com/default/cloud-resume-increment-view-count';

let headers = new Headers();

headers.append('Content-Type', 'application/json');
headers.append('Accept', 'application/json');
headers.append('Origin','http://cloud-resume-challenge44.s3-website.us-east-2.amazonaws.com/');

let viewCount = document.getElementById("viewCount");

fetch(apiUrl, {
    mode: 'cors',
    credentials: 'include',
    method: 'GET',
    origin: 'http://cloud-resume-challenge44.s3-website.us-east-2.amazonaws.com/'
  }).then(response => {
    return response.json();
}).then(data => {
    // Work with JSON data here
    viewCount.innerHTML = "Resume View Count: " + data.count;
}).catch(err => {
    // Do something for an error here
    viewCount.innerHTML = "Resume View Count: API Down";
});


