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
    console.log("Plates");
    var lot_number = scanned_barcode.substring(3, 8);
    var exp_date = scanned_barcode.substring(16, 24);
    var exp_year = scanned_barcode.substring(14, 16);
    var exp = exp_date + "" + exp_year;

    document.getElementById("id_lot_number").value = lot_number;
    document.getElementById("id_exp_date").value = exp;

    barcode = "";
  }

  // Remel Diluents
  if (document.getElementById("diluents").checked == true) {
    var lot_number = scanned_barcode.substring(26, 32);
    var exp_date = scanned_barcode.substring(20, 24);
    var exp_year = scanned_barcode.substring(18, 20);
    var exp = exp_date + "" + exp_year;

    document.getElementById("id_lot_number").value = lot_number;
    document.getElementById("id_exp_date").value = exp;

    barcode = "";
  }
};
