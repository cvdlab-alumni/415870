function pushToArray(n) {
    var a = [];
    for (var i = 0; i < n; i++)
        a.push(i + 1);
    return a;
}

function filterOdd(item, index, array) {
    return (item % 2 === 0);
}


function doubleN(item, index, array) {
    return item * 2;
}


function div4(item, index, array) {
    return (item % 4 === 0);
}

function sumAll(prev, cur) {
    return prev + cur;
}

function exercise01(n) {
    return pushToArray(n).
        filter(filterOdd).
        map(doubleN).
        filter(div4).
        reduce(sumAll);
}