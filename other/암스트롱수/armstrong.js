for (let i=100; i<1000; i++) {
    let n = i;
    let sum = 0;

    while(n != 0) {
        sum += Math.pow(n%10, 3);
        n = Math.floor(n / 10);
    }
    if(sum == i) {
        console.log(i + " ");
    }
}

for (var i=1; i<10; ++i) {
    for (var j=0; j<10; ++j) {
        for (var k=0; k<10; ++k) {
            var pow = (Math.pow(i, 3) + Math.pow(j, 3) + Math.pow(k, 3));
            var plus = (i*100 + j*10 + k);

            if(pow == plus) {
                console.log(pow);
            }
        }
    }
}
