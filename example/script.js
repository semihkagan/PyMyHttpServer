window.onload = function() {
    var a = document.createElement('a');
    a.href = './hello.txt'; // İndirilecek dosyanın yolu
    a.download = 'hello.txt'; // İndirilen dosyanın adı
    a.style.display = 'none';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
}