function qrScan() {
    let scanner = new Instascan.Scanner({ video: document.stream });
    scanner.addListener('scan', function (content) {
        document.getElementById('data').value=content;
    });
    Instascan.Camera.getCameras().then(function (cameras) {
        if (cameras.length > 0) {
        scanner.start(cameras[0]);
        } else {
        console.error('No cameras found.');
        }
    }).catch(function (e) {
        console.error(e);
    });
}