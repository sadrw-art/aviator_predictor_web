function choosePlatform(name) { 
  document.getElementById("platform-message").innerText 
  = "Selected: " + name;
}
function updatePrediction() { fetch("/predict") 
    .then(res => res.text()) .then(data => {
      document.getElementById("prediction").innerText 
      = data + "x";
      
      // ✈️ Restart plane animation
      const plane = 
      document.getElementById("plane"); 
      plane.style.animation = 'none'; void 
      plane.offsetWidth; // Force reflow 
      plane.style.animation = 'fly 5s linear';
    });
}
// Call once when page loads
window.onload = updatePrediction;
// Update prediction every 10 seconds
setInterval(updatePrediction, 10000);
