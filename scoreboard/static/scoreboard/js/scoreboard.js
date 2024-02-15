function blk (n, b, tag) {
    console.log(n, b, tag)
    if (b == 0) {
        document.getElementById(n).style.animation='ok';
    }
    else {
        if(tag == 'Scheduled') {
            document.getElementById(n).style.animation='blink 1s infinite';
            document.querySelector(`[id="${n}"]`).setAttribute('class', 'card  bg-danger text-center mt-3')
            console.log("in Scheduled if")
        }
        else {
            document.getElementById(n).style.animation='ok';
            console.log("in Scheduled else")
        }
    }
}


function tagChange(id) {
    const tag = ['Scheduled', 'Not Scheduled', 'No Operator', 'No Material', 'Machine Issue', 'Mold Issue']

    if(document.querySelector(`[id="${id}"]`).classList[1] !== 'text-bg-success' ) {
        x = document.querySelectorAll(`[id="${id}"] div div h4`)[1].innerText
        y = tag.indexOf(x)
        document.querySelectorAll(`[id="${id}"] div div h4`)[1].innerText=tag[(y + 1) % tag.length]
        
        console.log(tag[(y + 1) % tag.length])
        if(tag[(y + 1) % tag.length] == 'Scheduled'){
            document.querySelector(`[id="${id}"]`).setAttribute('class', 'card  bg-danger text-center mt-3')
            blk(id, 1, 'Scheduled')
        }
        else if(tag[(y + 1) % tag.length] == "Not Scheduled") {
            document.querySelector(`[id="${id}"]`).setAttribute('class', 'card  bg-secondary-subtle text-center mt-3')
            blk(id, 0, 'ok')
        }
        else {
            document.querySelector(`[id="${id}"]`).setAttribute('class', 'card  bg-warning text-center mt-3')
            blk(id, 0, 'ok')
        }
    }
}
