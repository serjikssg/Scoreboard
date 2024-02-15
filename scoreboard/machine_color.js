
function mcolor (n){
    var x = document.getElementById(n).classList['value'];

    
    if(x == 'card bg-danger text-center mt-3') {
        document.getElementById(n).classList['value'] = 'card bg-warning text-center mt-3';
        console.log('if');
    }
    if(x == 'card bg-warning text-center mt-3') {
        document.getElementById(n).classList['value'] = 'card bg-success text-center mt-3';
        console.log('if');
    }
    if(x == 'card bg-success text-center mt-3') {
        document.getElementById(n).classList['value'] = 'card bg-danger text-center mt-3';
        console.log('if');
    }
    
    // x.classList['value']='card bg-success text-center mt-3'
    // x = 'card bg-success text-center mt-3';

    console.log(document.getElementById("one").classList['value']);
    console.log(x);
}

function blk (n) {
    // xx = document.querySelectorAll("div.container div#deviceTileBox"); 
    // xx = document.getElementById("two");
    if (document.getElementById(n).style.animation != '') {
        document.getElementById(n).style.animation='';
        console.log("if")
    }
    else {
        document.getElementById(n).style.animation='blink 1s infinite';
        console.log("else")
    }
    // xx.style.color='RED';
    // console.log(xx)
}