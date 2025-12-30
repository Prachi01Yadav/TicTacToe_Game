let boxes = document.querySelectorAll(".box");
let reset = document.querySelector("#reset");

// Backend API URL
const API = "http://localhost:8000";

const difficulty = document.querySelector("#difficulty");
difficulty.addEventListener("change", async () => {
  await fetch(`${API}/set-difficulty/${difficulty.value}`, { method: "POST" });
});


// Click event for all boxes
boxes.forEach((box, index) => {
  box.addEventListener("click", async () => {
    try {
      const res = await fetch(`${API}/move/${index}`, { method: "POST" });
      const data = await res.json();
      updateUI(data);
    } catch (err) {
      console.error("Error:", err);
    }
  });
});

// Update frontend UI based on backend state
function updateUI(data) {
  data.board.forEach((val, i) => {
    boxes[i].innerText = val;
    boxes[i].disabled = val !== "";
  });

  if (data.winner) {
    alert(
      data.winner === "Draw"
        ? "It's a Draw 😐"
        : `🎉 Winner is ${data.winner}!`
    );
  }
}

// Reset button
reset.addEventListener("click", async () => {
  try {
    await fetch(`${API}/reset`, { method: "POST" });
    boxes.forEach(box => {
      box.innerText = "";
      box.disabled = false;
    });
  } catch (err) {
    console.error("Error resetting game:", err);
  }
});
