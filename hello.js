
console.log("This is working")
a = 50
b = 30
c = 20
d = 10

function calculateOutput(a,b,c,d){
  if (a === null) {
    a = 0
    console.log("Step 1")
    if(b == null) {
    b = 0
    console.log("Step 2")
     if(c == null) {
    c = 0
    console.log("Step 3")
      if(d == null) {
    d = 0
  } else {
   output =  a + b + c + d
    console.log(output)
  }
}
    }
  }
}
calculateOutput(6,12,10)