const input = document.getElementById("formInput")
const formFileName = document.getElementById("formFileName")
input.addEventListener("change", function(){
    let name = this.value;
    name = name.replace(/C:\\fakepath\\/i, "");
    formFileName.textContent = name;
})
var selectedFile;
    document
      .getElementById("formInput")
      .addEventListener("change", function(event) {
        selectedFile = event.target.files[0];
      });
    document
      .getElementById("formButton")
      .addEventListener("click", function() {
        formFileName.textContent = "";
        if (selectedFile) {
          var fileReader = new FileReader();
          fileReader.onload = function(event) {
            var data = event.target.result;
            var workbook = XLSX.read(data, {
              type: "binary"
            });
            workbook.SheetNames.forEach(sheet => {
              let rowObject = XLSX.utils.sheet_to_row_object_array(
                workbook.Sheets[sheet]
              );
              let jsonObject = JSON.stringify(rowObject);
              console.log(jsonObject);
            });
          };
          fileReader.readAsBinaryString(selectedFile);
        }
      });