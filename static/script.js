const form = document.getElementById("uploadForm");
const statusDiv = document.getElementById("status");

form.addEventListener("submit", function(e) {
    e.preventDefault();
    const data = new FormData(form);
    statusDiv.textContent = "Processing... This may take a few minutes.";
    fetch("/upload", { method: "POST", body: data })
        .then(res => res.json())
        .then(resp => {
            if(resp.video){
                statusDiv.innerHTML = `✅ Upload complete! <a href="/watch/${resp.video}">Watch Video</a>`;
            } else {
                statusDiv.textContent = "Error processing video";
            }
        })
        .catch(err => {
            statusDiv.textContent = "Error uploading video";
        });
});
