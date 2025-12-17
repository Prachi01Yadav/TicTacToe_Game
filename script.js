let boxes=document.querySelectorAll(".box");
let reset=document.querySelector("#reset");

let turnO=true; //playerX , playerO

const winPatterns=[
     [0,1,2],
     [0,3,6],
     [0,4,8],
     [1,4,7],
     [2,5,8],
     [2,4,6],
     [3,4,5],
     [6,7,8],
];

boxes.forEach((box) => {
    box.addEventListener("click", () =>{
        console.log("Box was clicked");
        if(turnO){
            box.innerText="O";
            turnO=false;
        }else{
            box.innerText="X";
            turnO=true;
        }
        box.disabled=true;
       checkWinner();
   });
});

function showWinner(winner) {
  alert(`🎉 Winner is ${winner} !`);
  disableBoxes();
}

function showDraw() {
  alert("It's a Draw! 😐");
}


function disableBoxes() {
  boxes.forEach(box => box.disabled = true);
}

function checkWinner() {
  for (let pattern of winPatterns) {
    let pos1 = boxes[pattern[0]].innerText;
    let pos2 = boxes[pattern[1]].innerText;
    let pos3 = boxes[pattern[2]].innerText;

   
    if (pos1 !== "" && pos1 === pos2 && pos2 === pos3) {
      console.log("Winner:", pos1);
      showWinner(pos1);
      return;
    }
  }

  
  if ([...boxes].every(box => box.innerText !== "")) {
    console.log("It's a draw!");
    showDraw();
  }
}

reset.addEventListener("click", () => {
  boxes.forEach(box => {
    box.innerText = "";
    box.disabled = false;
  });
  turnO = true; // start again with O
});


