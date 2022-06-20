// Handle Barcode Scan Event
var barcode = "";
var interval;
document.addEventListener("keydown", function (evt) {
  if (interval) clearInterval(interval);
  if (evt.code == "Enter") {
    if (barcode) handleBarcode(barcode);
    barcode = "";
    return;
  }
  if (evt.key != "Shift") barcode += evt.key;
  interval = setInterval(() => (barcode = ""), 20);
});

// Parses barcode and inserts values into respective inputs
const handleBarcode = (scanned_barcode) => {
  // TSA plates (fallout and contact)
  if (document.getElementById("plates").checked == true) {
    let lotNumber = scanned_barcode.substring(3, 9);

    let expMonth = scanned_barcode.substring(16, 18);
    let expDay = scanned_barcode.substring(18, 21);
    let expYear = scanned_barcode.substring(14, 16);

    let exp = expMonth + "/" + expDay + "/" + expYear;

    document.getElementById("id_lot_number").value = lotNumber;
    document.getElementById("id_exp_date").value = exp;

    barcode = "";
  }

  // Remel Diluents
  if (document.getElementById("diluents").checked == true) {
    let lotNumber = scanned_barcode.substring(26, 32);

    let expMonth = scanned_barcode.substring(20, 22);
    let expDay = scanned_barcode.substring(22, 24);
    let expYear = scanned_barcode.substring(18, 20);

    let exp = expMonth + "/" + expDay + "/" + expYear;

    document.getElementById("id_lot_number").value = lotNumber;
    document.getElementById("id_exp_date").value = exp;

    barcode = "";
  }
};
