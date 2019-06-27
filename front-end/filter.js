let arr = [];

filterSelection("");
function filterSelection(c) {
  if (!arr.includes(c)) {
    arr.push(c);
  } else {
    var index = arr.indexOf(c);
    arr.splice(index, 1);
  }
  console.log("The list of filters is " + arr);
  var x, i;
  x = document.getElementsByClassName("emp");
  if (c == "all") c = "";
  // Add the "show" class (display:block) to the filtered elements, and remove the "show" class from the elements that are not selected
  for (i = 0; i < x.length; i++) {
    w3RemoveClass(x[i], "show");
    // if (x[i].className.indexOf(c) > -1) w3AddClass(x[i], "show");
    if (checkAllFilters(x[i])) w3AddClass(x[i], "show");
  }
}

function checkAllFilters(element) {
  for (var i = 0; i < arr.length; i++) {
    var filter = arr[i];
    if (!(element.className.indexOf(filter) > -1)) return false;
  }
  return true;
}

// Show filtered elements
function w3AddClass(element, name) {
  var i, arr1, arr2;
  arr1 = element.className.split(" ");
  arr2 = name.split(" ");
  for (i = 0; i < arr2.length; i++) {
    if (arr1.indexOf(arr2[i]) == -1) {
      element.className += " " + arr2[i];
    }
  }
}

// Hide elements that are not selected
function w3RemoveClass(element, name) {
  var i, arr1, arr2;
  arr1 = element.className.split(" ");
  arr2 = name.split(" ");
  for (i = 0; i < arr2.length; i++) {
    while (arr1.indexOf(arr2[i]) > -1) {
      arr1.splice(arr1.indexOf(arr2[i]), 1);
    }
  }
  element.className = arr1.join(" ");
}

// Add active class to the current control button (highlight it)
var btnContainer = document.getElementById("myBtnContainer");
var btns = btnContainer.getElementsByClassName("btn");
for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function() {
    this.classList.toggle("active");
  });
}
